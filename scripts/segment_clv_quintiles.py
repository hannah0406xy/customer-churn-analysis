import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def segment_clv_quintiles():
    """
    Segment customers into CLV quintiles and analyze the characteristics of each segment.
    """
    # Load data with CLV values
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_clv.csv')
    df = pd.read_csv(data_path)
    
    # Ensure expected_clv column exists
    if 'expected_clv' not in df.columns:
        print("Error: expected_clv column not found in the dataset.")
        return
    
    # Create CLV quintiles
    df['clv_quintile'] = pd.qcut(df['expected_clv'], q=5, labels=['Q1 (Lowest)', 'Q2', 'Q3', 'Q4', 'Q5 (Highest)'])
    
    # Analyze CLV distribution by quintile
    quintile_stats = df.groupby('clv_quintile')['expected_clv'].agg(['count', 'min', 'mean', 'median', 'max'])
    print("CLV Statistics by Quintile:")
    print(quintile_stats)
    
    # Visualize CLV distribution by quintile
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='clv_quintile', y='expected_clv')
    plt.title('CLV Distribution by Quintile')
    plt.xlabel('CLV Quintile')
    plt.ylabel('Expected CLV ($)')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'clv_distribution_by_quintile.png'))
    plt.close()
    
    # Identify key features for analysis
    key_features = [
        'revenue_segment', 'age_segment', 'service_segment',
        'rev_Mean', 'mou_Mean', 'totcalls', 'custcare_Mean',
        'age1', 'age2', 'change_mou', 'drop_vce_Mean', 'churn'
    ]
    features_to_analyze = [f for f in key_features if f in df.columns]
    
    # Analyze categorical features by quintile
    categorical_features = ['revenue_segment', 'age_segment', 'service_segment', 'churn']
    categorical_features = [f for f in categorical_features if f in features_to_analyze]
    
    for feature in categorical_features:
        plt.figure(figsize=(12, 6))
        # Create cross-tabulation and convert to percentage
        crosstab = pd.crosstab(
            df['clv_quintile'], 
            df[feature], 
            normalize='index'
        ) * 100
        
        # Plot stacked bar chart
        crosstab.plot(kind='bar', stacked=True)
        plt.title(f'Percentage of {feature} Categories by CLV Quintile')
        plt.xlabel('CLV Quintile')
        plt.ylabel('Percentage (%)')
        plt.legend(title=feature)
        plt.tight_layout()
        plt.savefig(os.path.join(base_dir, 'models', f'clv_quintile_by_{feature}.png'))
        plt.close()
    
    # Analyze numerical features by quintile
    numerical_features = [f for f in features_to_analyze if f not in categorical_features]
    
    # Create a figure with multiple subplots for numerical features
    n_features = len(numerical_features)
    n_cols = 2
    n_rows = (n_features + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4 * n_rows))
    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    axes = axes.flatten()
    
    for i, feature in enumerate(numerical_features):
        if i < len(axes):
            sns.boxplot(data=df, x='clv_quintile', y=feature, ax=axes[i])
            axes[i].set_title(f'{feature} by CLV Quintile')
            axes[i].set_xlabel('CLV Quintile')
            axes[i].set_ylabel(feature)
    
    # Hide unused subplots
    for i in range(n_features, len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'clv_quintile_numerical_features.png'))
    plt.close()
    
    # Generate report
    report = '# Customer Segmentation by CLV Quintiles\n\n'
    
    # Overall statistics
    report += '## CLV Statistics by Quintile\n'
    report += quintile_stats.to_markdown() + '\n\n'
    
    # Key characteristics of each quintile
    report += '## Key Characteristics by Quintile\n\n'
    
    # Analyze each quintile and its distinct characteristics
    for quintile in df['clv_quintile'].unique():
        quintile_df = df[df['clv_quintile'] == quintile]
        
        report += f'### {quintile}\n\n'
        
        # CLV range
        min_clv = quintile_df['expected_clv'].min()
        max_clv = quintile_df['expected_clv'].max()
        mean_clv = quintile_df['expected_clv'].mean()
        median_clv = quintile_df['expected_clv'].median()
        
        report += f'- **CLV Range**: ${min_clv:.2f} to ${max_clv:.2f}\n'
        report += f'- **Mean CLV**: ${mean_clv:.2f}\n'
        report += f'- **Median CLV**: ${median_clv:.2f}\n'
        report += f'- **Number of Customers**: {len(quintile_df):,}\n\n'
        
        # Categorical characteristics
        report += '**Segment Distribution:**\n\n'
        
        for feature in categorical_features:
            if feature in df.columns:
                feature_dist = quintile_df[feature].value_counts(normalize=True) * 100
                report += f'*{feature}*\n'
                for category, percentage in feature_dist.items():
                    report += f'- {category}: {percentage:.1f}%\n'
                report += '\n'
        
        # Numerical characteristics
        report += '**Key Metrics (median values):**\n\n'
        
        for feature in numerical_features:
            if feature in df.columns:
                median_value = quintile_df[feature].median()
                report += f'- {feature}: {median_value:.2f}\n'
        
        report += '\n'
    
    # Visualizations
    report += '## Visualizations\n\n'
    report += '### CLV Distribution by Quintile\n'
    report += '![CLV Distribution by Quintile](clv_distribution_by_quintile.png)\n\n'
    
    for feature in categorical_features:
        report += f'### {feature} Distribution by Quintile\n'
        report += f'![{feature} by Quintile](clv_quintile_by_{feature}.png)\n\n'
    
    report += '### Numerical Features by Quintile\n'
    report += '![Numerical Features by Quintile](clv_quintile_numerical_features.png)\n\n'
    
    # Business Recommendations for each quintile
    report += '## Business Recommendations by Quintile\n\n'
    
    report += '### Q5 (Highest CLV)\n'
    report += '- **Strategy**: Loyalty and retention focus\n'
    report += '- **Actions**: Premium service offerings, personalized engagement, loyalty rewards\n'
    report += '- **Goal**: Maintain long-term relationship and maximize share of wallet\n\n'
    
    report += '### Q4\n'
    report += '- **Strategy**: Growth and cross-selling\n'
    report += '- **Actions**: Targeted upgrade offers, premium service trials, expanded engagement\n'
    report += '- **Goal**: Increase usage and move customers to highest CLV segment\n\n'
    
    report += '### Q3\n'
    report += '- **Strategy**: Engagement and value enhancement\n'
    report += '- **Actions**: Usage incentives, feature education, mid-tier offerings\n'
    report += '- **Goal**: Increase product usage and customer engagement\n\n'
    
    report += '### Q2\n'
    report += '- **Strategy**: Service improvement and satisfaction\n'
    report += '- **Actions**: Satisfaction surveys, service quality improvements, targeted offers\n'
    report += '- **Goal**: Address pain points and improve retention\n\n'
    
    report += '### Q1 (Lowest CLV)\n'
    report += '- **Strategy**: Cost-effective management and selective retention\n'
    report += '- **Actions**: Digital self-service options, basic service improvements, selective win-back campaigns\n'
    report += '- **Goal**: Improve profitability and identify potential for upward migration\n\n'
    
    # Save report
    with open(os.path.join(base_dir, 'models', 'clv_quintile_analysis_report.md'), 'w') as f:
        f.write(report)
    
    # Save updated dataset with CLV quintiles
    df.to_csv(os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_clv_quintiles.csv'), index=False)
    
    print('CLV quintile segmentation complete. See models/clv_quintile_analysis_report.md for the full report.')

if __name__ == '__main__':
    segment_clv_quintiles() 