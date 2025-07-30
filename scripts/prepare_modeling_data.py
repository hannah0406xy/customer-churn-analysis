import pandas as pd
import os

def prepare_modeling_data():
    # Load processed data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'processed_data.csv')
    df = pd.read_csv(data_path)
    
    # List of features to drop (from correlation analysis)
    features_to_drop = [
        'adjmou', 'adjqty', 'adjrev', 'attempt_Mean', 'attempt_Range',
        'avg3mou', 'avg3qty', 'avg3rev', 'avg6mou', 'avg6qty',
        'avg_monthly_calls', 'blck_dat_Range', 'care_intensity',
        'care_quality', 'cc_mou_Mean', 'cc_mou_Range', 'comp_dat_Mean',
        'comp_dat_Range', 'comp_vce_Mean', 'comp_vce_Range',
        'complete_Mean', 'complete_Range', 'customer_value_score',
        'datovr_Range', 'device_age_months', 'drop_block_interaction',
        'inonemin_Mean', 'inonemin_Range', 'mailresp', 'mou_opkd_Mean',
        'mou_opkd_Range', 'off_peak_usage_ratio', 'opk_dat_Mean',
        'opk_dat_Range', 'ovrrev_Mean', 'ovrrev_Range', 'peak_dat_Mean',
        'peak_vce_Mean', 'price_per_minute', 'price_quality_ratio',
        'roam_Range', 'service_care_impact', 'service_quality_score',
        'totmou', 'trend_volatility', 'unan_dat_Range', 'usage_volatility',
        'vceovr_Mean', 'vceovr_Range', 'weekend_usage_ratio'
    ]
    
    # Create modeling dataset by dropping highly collinear features
    modeling_df = df.drop(columns=features_to_drop, errors='ignore')
    
    # Save modeling dataset
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed')
    modeling_df.to_csv(os.path.join(output_dir, 'modeling_data.csv'), index=False)
    
    # Generate report of remaining features
    remaining_features = modeling_df.columns.tolist()
    remaining_features.remove('Customer_ID')  # Remove ID column from count
    remaining_features.remove('churn')  # Remove target column from count
    
    report = '# Modeling Dataset Preparation Report\n\n'
    report += f'## Dataset Overview\n'
    report += f'- Original number of features: {len(df.columns) - 2}\n'  # -2 for ID and target
    report += f'- Number of features after removing collinear features: {len(remaining_features)}\n'
    report += f'- Number of samples: {len(modeling_df)}\n\n'
    
    report += '## Remaining Features\n'
    report += '| Feature | Type |\n'
    report += '|---------|------|\n'
    
    # Categorize remaining features
    categorical_features = modeling_df.select_dtypes(include=['object', 'category']).columns
    numerical_features = modeling_df.select_dtypes(include=['int64', 'float64']).columns
    numerical_features = [col for col in numerical_features if col not in ['Customer_ID', 'churn']]
    
    for feature in sorted(remaining_features):
        feature_type = 'Categorical' if feature in categorical_features else 'Numerical'
        report += f'| {feature} | {feature_type} |\n'
    
    # Save report
    with open(os.path.join(output_dir, 'modeling_preparation_report.md'), 'w') as f:
        f.write(report)
    
    print('Modeling dataset preparation completed. Check the data/processed directory for the new dataset and report.')

if __name__ == '__main__':
    prepare_modeling_data() 