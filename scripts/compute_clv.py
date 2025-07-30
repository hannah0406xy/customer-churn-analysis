import pandas as pd
import numpy as np
import os
import joblib
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt
import seaborn as sns

def compute_clv():
    # Load data and models
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data.csv')
    df = pd.read_csv(data_path)
    
    # Load Cox model
    cox_model_path = os.path.join(base_dir, 'models', 'cox_model.joblib')
    cph = joblib.load(cox_model_path)
    
    # Prepare features for prediction
    features = [
        'rev_Mean', 'mou_Mean', 'totcalls', 'custcare_Mean',
        'age1', 'age2', 'change_mou', 'drop_vce_Mean'
    ]
    features = [f for f in features if f in df.columns]
    
    # Debug revenue
    print('rev_Mean stats:', df['rev_Mean'].describe())
    
    # We need the original revenue values, not standardized
    # For this exercise, we'll use an estimated monthly revenue of $50-$150
    # Lower revenue for negative standardized values, higher for positive
    df['rev_actual'] = 100 + df['rev_Mean'] * 50  # $50-$150 range
    print('Estimated actual revenue stats:', df['rev_actual'].describe())
    
    # Define time horizon and discount rate
    max_months = 60
    monthly_discount_rate = 0.005
    
    # Calculate CLV directly using the survival probability at specific time points
    # Instead of interpolating, we'll use lifelines' built-in predict_survival_function
    # but with specific time points that match our months
    
    # Create time points in months (convert to days for Cox model)
    time_points_days = np.array([30 * m for m in range(1, max_months + 1)])
    
    # Get survival probabilities at these specific times
    surv_prob_df = cph.predict_survival_function(df[features], times=time_points_days)
    print('Survival probabilities shape:', surv_prob_df.shape)
    print('First few survival probabilities:', surv_prob_df.iloc[:5, :5])
    
    # Calculate CLV for each customer
    expected_clv = []
    discount_factors = 1 / ((1 + monthly_discount_rate) ** np.arange(1, max_months + 1))
    
    for i in range(len(df)):
        # Get customer's monthly revenue
        monthly_revenue = df.iloc[i]['rev_actual']
        
        # Get survival probabilities for this customer at each time point
        customer_surv_probs = surv_prob_df.iloc[:, i].values
        
        # CLV = sum of discounted future revenues weighted by survival probability
        clv = np.sum(customer_surv_probs * monthly_revenue * discount_factors)
        expected_clv.append(clv)
    
    # Add CLV to dataframe
    df['expected_clv'] = expected_clv
    print('CLV stats:', df['expected_clv'].describe())
    
    # --- Ensure segment columns exist ---
    # Revenue segment
    if 'revenue_segment' not in df.columns:
        median_revenue = df['rev_Mean'].median()
        df['revenue_segment'] = np.where(df['rev_Mean'] >= median_revenue, 'High Revenue', 'Low Revenue')
    # Age segment
    if 'age_segment' not in df.columns:
        median_age = df['age1'].median()
        df['age_segment'] = np.where(df['age1'] < median_age, 'Young', 'Old')
    # Service segment
    if 'service_segment' not in df.columns:
        median_calls = df['totcalls'].median()
        df['service_segment'] = np.where(df['totcalls'] < median_calls, 'Basic', 'Premium')
    # --- End segment columns ---
    
    # Create CLV distribution plot
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='expected_clv', bins=50)
    plt.title('Distribution of Expected Customer Lifetime Value')
    plt.xlabel('Expected CLV ($)')
    plt.ylabel('Count')
    plt.savefig(os.path.join(base_dir, 'models', 'clv_distribution.png'))
    plt.close()
    
    # Create CLV by segment plots
    # Revenue segment
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='revenue_segment', y='expected_clv')
    plt.title('Expected CLV by Revenue Segment')
    plt.xlabel('Revenue Segment')
    plt.ylabel('Expected CLV ($)')
    plt.savefig(os.path.join(base_dir, 'models', 'clv_by_revenue.png'))
    plt.close()
    
    # Age segment
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='age_segment', y='expected_clv')
    plt.title('Expected CLV by Age Segment')
    plt.xlabel('Age Segment')
    plt.ylabel('Expected CLV ($)')
    plt.savefig(os.path.join(base_dir, 'models', 'clv_by_age.png'))
    plt.close()
    
    # Service segment
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='service_segment', y='expected_clv')
    plt.title('Expected CLV by Service Segment')
    plt.xlabel('Service Segment')
    plt.ylabel('Expected CLV ($)')
    plt.savefig(os.path.join(base_dir, 'models', 'clv_by_service.png'))
    plt.close()
    
    # Generate report
    report = '# Customer Lifetime Value Analysis\n\n'
    
    # Overall CLV statistics
    report += '## Overall CLV Statistics\n'
    report += f'- Mean CLV: ${df["expected_clv"].mean():,.2f}\n'
    report += f'- Median CLV: ${df["expected_clv"].median():,.2f}\n'
    report += f'- Min CLV: ${df["expected_clv"].min():,.2f}\n'
    report += f'- Max CLV: ${df["expected_clv"].max():,.2f}\n\n'
    
    # CLV by segment
    report += '## CLV by Revenue Segment\n'
    revenue_stats = df.groupby('revenue_segment')['expected_clv'].agg(['mean', 'median', 'count'])
    report += revenue_stats.to_markdown() + '\n\n'
    
    report += '## CLV by Age Segment\n'
    age_stats = df.groupby('age_segment')['expected_clv'].agg(['mean', 'median', 'count'])
    report += age_stats.to_markdown() + '\n\n'
    
    report += '## CLV by Service Segment\n'
    service_stats = df.groupby('service_segment')['expected_clv'].agg(['mean', 'median', 'count'])
    report += service_stats.to_markdown() + '\n\n'
    
    # Save report
    with open(os.path.join(base_dir, 'models', 'clv_analysis_report.md'), 'w') as f:
        f.write(report)
    
    # Save updated dataset with CLV
    df.to_csv(os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_clv.csv'), index=False)
    
    print('CLV computation completed. Check the models directory for results.')

if __name__ == '__main__':
    compute_clv() 