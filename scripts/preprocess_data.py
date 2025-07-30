import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import os

def preprocess_data():
    # Read the data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'Cell1.csv')
    df = pd.read_csv(data_path)
    
    # Create output directory for processed data
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a copy for analysis
    df_analysis = df.copy()
    
    # 1. Analyze missing values
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    
    # Save missing value analysis
    missing_analysis = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage': missing_percentage
    })
    missing_analysis = missing_analysis[missing_analysis['Missing Values'] > 0].sort_values('Percentage', ascending=False)
    
    # 2. Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Remove target variable and ID columns from numerical columns
    numerical_cols = numerical_cols.drop(['churn', 'Customer_ID'])
    
    # 3. Handle missing values
    # Strategy 1: Remove columns with >80% missing values
    high_missing_cols = missing_analysis[missing_analysis['Percentage'] > 80].index
    df = df.drop(columns=high_missing_cols)
    
    # Update categorical and numerical columns after dropping high missing columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    numerical_cols = numerical_cols.drop(['churn', 'Customer_ID'])
    
    # Strategy 2: Handle numerical missing values
    # For columns with <20% missing values, use median imputation
    low_missing_numerical = missing_analysis[
        (missing_analysis['Percentage'] <= 20) & 
        (missing_analysis.index.isin(numerical_cols))
    ].index
    
    if len(low_missing_numerical) > 0:
        numerical_imputer = SimpleImputer(strategy='median')
        df[low_missing_numerical] = numerical_imputer.fit_transform(df[low_missing_numerical])
    
    # For columns with >20% missing values, use mean imputation
    high_missing_numerical = missing_analysis[
        (missing_analysis['Percentage'] > 20) & 
        (missing_analysis['Percentage'] <= 80) & 
        (missing_analysis.index.isin(numerical_cols))
    ].index
    
    if len(high_missing_numerical) > 0:
        numerical_imputer = SimpleImputer(strategy='mean')
        df[high_missing_numerical] = numerical_imputer.fit_transform(df[high_missing_numerical])
    
    # Strategy 3: Handle categorical missing values
    # For columns with <20% missing values, use mode imputation
    low_missing_categorical = missing_analysis[
        (missing_analysis['Percentage'] <= 20) & 
        (missing_analysis.index.isin(categorical_cols))
    ].index
    
    if len(low_missing_categorical) > 0:
        categorical_imputer = SimpleImputer(strategy='most_frequent')
        df[low_missing_categorical] = categorical_imputer.fit_transform(df[low_missing_categorical])
    
    # For columns with >20% missing values, use 'Unknown' category
    high_missing_categorical = missing_analysis[
        (missing_analysis['Percentage'] > 20) & 
        (missing_analysis.index.isin(categorical_cols))
    ].index
    
    if len(high_missing_categorical) > 0:
        df[high_missing_categorical] = df[high_missing_categorical].fillna('Unknown')
    
    # 4. Handle categorical variables
    categorical_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        categorical_encoders[col] = le
    
    # 5. Scale numerical features
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    # 6. Create new features
    # Revenue and Usage Features
    df['revenue_per_minute'] = df['rev_Mean'] / (df['mou_Mean'] + 1)
    df['care_per_month'] = df['custcare_Mean'] / (df['months'] + 1)
    df['avg_monthly_revenue'] = df['totrev'] / df['months']
    df['avg_monthly_minutes'] = df['totmou'] / df['months']
    df['avg_monthly_calls'] = df['totcalls'] / df['months']
    
    # Service Quality Features
    df['drop_rate'] = df['drop_vce_Mean'] / (df['plcd_vce_Mean'] + 1)
    df['block_rate'] = df['blck_vce_Mean'] / (df['plcd_vce_Mean'] + 1)
    df['service_quality_score'] = 1 - (df['drop_rate'] + df['block_rate'])
    
    # Usage Pattern Features
    df['peak_usage_ratio'] = df['peak_vce_Mean'] / (df['mou_Mean'] + 1)
    df['off_peak_usage_ratio'] = df['opk_vce_Mean'] / (df['mou_Mean'] + 1)
    df['weekend_usage_ratio'] = df['owylis_vce_Mean'] / (df['mou_Mean'] + 1)
    
    # Customer Service Features
    df['care_intensity'] = df['custcare_Mean'] / (df['months'] + 1)
    df['care_quality'] = df['complete_Mean'] / (df['attempt_Mean'] + 1)
    
    # Plan and Device Features
    df['price_per_minute'] = df['totmrc_Mean'] / (df['mou_Mean'] + 1)
    df['device_age_months'] = df['eqpdays'] / 30
    df['price_change_ratio'] = df['hnd_price'] / (df['pre_hnd_price'] + 1)
    
    # Usage Trend Features
    df['mou_trend'] = df['change_mou'] / (df['mou_Mean'] + 1)
    df['rev_trend'] = df['change_rev'] / (df['rev_Mean'] + 1)
    df['usage_volatility'] = df['mou_Range'] / (df['mou_Mean'] + 1)
    
    # Customer Profile Features
    df['household_size'] = df['adults'] + df['children'].fillna(0)
    df['income_per_adult'] = df['income'] / (df['adults'] + 1)
    df['cars_per_adult'] = df['numbcars'] / (df['adults'] + 1)
    
    # 7. Create interaction features
    # Revenue and Usage Interactions
    df['revenue_usage_efficiency'] = df['avg_monthly_revenue'] * df['avg_monthly_minutes']
    df['revenue_care_ratio'] = df['avg_monthly_revenue'] * df['care_intensity']
    df['usage_care_ratio'] = df['avg_monthly_minutes'] * df['care_intensity']
    
    # Service Quality Interactions
    df['quality_revenue_impact'] = df['service_quality_score'] * df['avg_monthly_revenue']
    df['quality_usage_impact'] = df['service_quality_score'] * df['avg_monthly_minutes']
    df['drop_block_interaction'] = df['drop_rate'] * df['block_rate']
    
    # Usage Pattern Interactions
    df['peak_off_peak_ratio'] = df['peak_usage_ratio'] / (df['off_peak_usage_ratio'] + 1)
    df['weekday_weekend_ratio'] = (1 - df['weekend_usage_ratio']) / (df['weekend_usage_ratio'] + 1)
    df['usage_pattern_score'] = df['peak_usage_ratio'] * df['off_peak_usage_ratio'] * df['weekend_usage_ratio']
    
    # Customer Service Interactions
    df['care_quality_intensity'] = df['care_quality'] * df['care_intensity']
    df['service_care_impact'] = df['service_quality_score'] * df['care_quality']
    df['care_trend_impact'] = df['care_intensity'] * df['mou_trend']
    
    # Plan and Device Interactions
    df['price_quality_ratio'] = df['price_per_minute'] * df['service_quality_score']
    df['device_price_impact'] = df['device_age_months'] * df['price_change_ratio']
    df['plan_usage_efficiency'] = df['price_per_minute'] * df['avg_monthly_minutes']
    
    # Usage Trend Interactions
    df['trend_volatility'] = df['mou_trend'] * df['usage_volatility']
    df['revenue_usage_trend'] = df['rev_trend'] * df['mou_trend']
    df['quality_trend_impact'] = df['service_quality_score'] * df['mou_trend']
    
    # Customer Profile Interactions
    df['household_income_ratio'] = df['household_size'] * df['income_per_adult']
    df['lifestyle_score'] = df['cars_per_adult'] * df['income_per_adult']
    df['demographic_usage_impact'] = df['household_size'] * df['avg_monthly_minutes']
    
    # Composite Features
    df['customer_value_score'] = (
        df['avg_monthly_revenue'] * 
        df['service_quality_score'] * 
        (1 - df['care_intensity'])
    )
    
    df['churn_risk_score'] = (
        df['drop_rate'] * 
        df['block_rate'] * 
        df['care_intensity'] * 
        (1 - df['service_quality_score'])
    )
    
    df['loyalty_score'] = (
        df['months'] * 
        df['service_quality_score'] * 
        (1 - df['care_intensity']) * 
        (1 - abs(df['mou_trend']))
    )
    
    # 8. Feature Importance Analysis
    # Prepare data for feature importance analysis
    X = df.drop(['churn', 'Customer_ID'], axis=1)
    y = df['churn']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest classifier
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # Get feature importance scores
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf.feature_importances_
    })
    feature_importance = feature_importance.sort_values('Importance', ascending=False)
    
    # Create feature importance plot
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance.head(20))
    plt.title('Top 20 Most Important Features for Churn Prediction')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'feature_importance.png'))
    plt.close()
    
    # 9. Save processed data
    df.to_csv(os.path.join(output_dir, 'processed_data.csv'), index=False)
    
    # 10. Generate preprocessing report
    report = "# Data Preprocessing Report\n\n"
    
    # Missing values section
    report += "## Missing Values Analysis\n"
    report += "| Column | Missing Values | Percentage | Imputation Strategy |\n"
    report += "|--------|---------------|------------|-------------------|\n"
    
    for idx, row in missing_analysis.iterrows():
        strategy = "Removed" if row['Percentage'] > 80 else \
                  "Median" if idx in low_missing_numerical else \
                  "Mean" if idx in high_missing_numerical else \
                  "Mode" if idx in low_missing_categorical else \
                  "Unknown category" if idx in high_missing_categorical else \
                  "No missing values"
        report += f"| {idx} | {row['Missing Values']:,} | {row['Percentage']:.2f}% | {strategy} |\n"
    
    # Categorical variables section
    report += "\n## Categorical Variables\n"
    report += "| Column | Unique Values | Encoded |\n"
    report += "|--------|--------------|----------|\n"
    for col in categorical_cols:
        encoded = "Yes" if col in categorical_encoders else "No"
        report += f"| {col} | {df_analysis[col].nunique()} | {encoded} |\n"
    
    # Numerical variables section
    report += "\n## Numerical Variables\n"
    report += "| Column | Mean | Std | Min | Max |\n"
    report += "|--------|------|-----|-----|-----|\n"
    for col in numerical_cols:
        stats = df_analysis[col].describe()
        report += f"| {col} | {stats['mean']:.2f} | {stats['std']:.2f} | {stats['min']:.2f} | {stats['max']:.2f} |\n"
    
    # New features section
    report += "\n## New Engineered Features\n"
    report += "| Feature | Description |\n"
    report += "|---------|-------------|\n"
    report += "| revenue_per_minute | Average revenue per minute of usage |\n"
    report += "| care_per_month | Average customer care calls per month |\n"
    report += "| avg_monthly_revenue | Average monthly revenue |\n"
    report += "| avg_monthly_minutes | Average monthly minutes of usage |\n"
    report += "| avg_monthly_calls | Average monthly number of calls |\n"
    report += "| drop_rate | Ratio of dropped calls to placed calls |\n"
    report += "| block_rate | Ratio of blocked calls to placed calls |\n"
    report += "| service_quality_score | Overall service quality score |\n"
    report += "| peak_usage_ratio | Ratio of peak time usage to total usage |\n"
    report += "| off_peak_usage_ratio | Ratio of off-peak time usage to total usage |\n"
    report += "| weekend_usage_ratio | Ratio of weekend usage to total usage |\n"
    report += "| care_intensity | Customer care calls per month |\n"
    report += "| care_quality | Ratio of completed calls to attempted calls |\n"
    report += "| price_per_minute | Average price per minute of usage |\n"
    report += "| device_age_months | Age of device in months |\n"
    report += "| price_change_ratio | Ratio of current to previous handset price |\n"
    report += "| mou_trend | Change in minutes of usage |\n"
    report += "| rev_trend | Change in revenue |\n"
    report += "| usage_volatility | Variability in usage patterns |\n"
    report += "| household_size | Total number of adults and children |\n"
    report += "| income_per_adult | Average income per adult |\n"
    report += "| cars_per_adult | Average number of cars per adult |\n"
    
    # Interaction features section
    report += "\n## Interaction Features\n"
    report += "| Feature | Description |\n"
    report += "|---------|-------------|\n"
    report += "| revenue_usage_efficiency | Interaction between revenue and usage |\n"
    report += "| revenue_care_ratio | Interaction between revenue and customer care |\n"
    report += "| usage_care_ratio | Interaction between usage and customer care |\n"
    report += "| quality_revenue_impact | Impact of service quality on revenue |\n"
    report += "| quality_usage_impact | Impact of service quality on usage |\n"
    report += "| drop_block_interaction | Interaction between drop and block rates |\n"
    report += "| peak_off_peak_ratio | Ratio of peak to off-peak usage |\n"
    report += "| weekday_weekend_ratio | Ratio of weekday to weekend usage |\n"
    report += "| usage_pattern_score | Combined usage pattern score |\n"
    report += "| care_quality_intensity | Interaction between care quality and intensity |\n"
    report += "| service_care_impact | Impact of service quality on customer care |\n"
    report += "| care_trend_impact | Impact of customer care on usage trends |\n"
    report += "| price_quality_ratio | Interaction between price and service quality |\n"
    report += "| device_price_impact | Impact of device age on price changes |\n"
    report += "| plan_usage_efficiency | Efficiency of plan usage |\n"
    report += "| trend_volatility | Interaction between trends and volatility |\n"
    report += "| revenue_usage_trend | Combined revenue and usage trends |\n"
    report += "| quality_trend_impact | Impact of service quality on trends |\n"
    report += "| household_income_ratio | Interaction between household size and income |\n"
    report += "| lifestyle_score | Combined lifestyle indicators |\n"
    report += "| demographic_usage_impact | Impact of demographics on usage |\n"
    
    # Composite features section
    report += "\n## Composite Features\n"
    report += "| Feature | Description |\n"
    report += "|---------|-------------|\n"
    report += "| customer_value_score | Overall customer value metric |\n"
    report += "| churn_risk_score | Overall churn risk metric |\n"
    report += "| loyalty_score | Overall customer loyalty metric |\n"
    
    # Feature importance section
    report += "\n## Feature Importance Analysis\n"
    report += "| Feature | Importance Score |\n"
    report += "|---------|-----------------|\n"
    for _, row in feature_importance.head(20).iterrows():
        report += f"| {row['Feature']} | {row['Importance']:.4f} |\n"
    
    # Save report
    with open(os.path.join(output_dir, 'preprocessing_report.md'), 'w') as f:
        f.write(report)
    
    print("Data preprocessing completed. Check the 'data/processed' directory for results.")

if __name__ == "__main__":
    preprocess_data() 