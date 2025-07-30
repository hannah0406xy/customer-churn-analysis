import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def correlation_analysis():
    # Load processed data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'processed_data.csv')
    df = pd.read_csv(data_path)
    
    # Exclude ID and target columns
    drop_cols = ['Customer_ID', 'churn']
    features = [col for col in df.columns if col not in drop_cols]
    df_features = df[features]
    
    # Compute correlation matrix
    corr_matrix = df_features.corr()
    
    # Find highly correlated pairs (|r| > 0.9)
    high_corr_pairs = []
    corr_threshold = 0.9
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            corr_val = corr_matrix.iloc[i, j]
            if abs(corr_val) > corr_threshold:
                high_corr_pairs.append((col1, col2, corr_val))
    
    # Suggest features to drop (keep only one from each highly correlated pair)
    to_drop = set()
    for col1, col2, _ in high_corr_pairs:
        # Drop the second feature in the pair (arbitrary, could use other logic)
        to_drop.add(col2)
    
    # Generate heatmap
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed')
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr_matrix, cmap='coolwarm', center=0, cbar_kws={'shrink': 0.5})
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()
    
    # Generate markdown report
    report = '# Correlation Analysis Report\n\n'
    report += '## Highly Collinear Feature Pairs (|r| > 0.9)\n'
    report += '| Feature 1 | Feature 2 | Correlation |\n'
    report += '|-----------|-----------|-------------|\n'
    for col1, col2, corr_val in high_corr_pairs:
        report += f'| {col1} | {col2} | {corr_val:.3f} |\n'
    
    report += '\n## Suggested Features to Drop\n'
    report += ', '.join(sorted(to_drop)) if to_drop else 'None'
    
    with open(os.path.join(output_dir, 'correlation_analysis.md'), 'w') as f:
        f.write(report)
    
    print('Correlation analysis completed. Check the data/processed directory for the heatmap and report.')

if __name__ == '__main__':
    correlation_analysis() 