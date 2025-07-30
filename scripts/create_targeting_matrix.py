import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def create_targeting_matrix():
    """
    Create a targeting matrix that combines CLV quintiles with churn risk
    to provide strategic targeting recommendations.
    """
    # Load data with CLV quintiles
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_clv_quintiles.csv')
    df = pd.read_csv(data_path)
    
    # Ensure required columns exist
    required_cols = ['expected_clv', 'clv_quintile', 'churn']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Error: Missing required columns: {missing_cols}")
        return
    
    # Create binary churn risk category
    # If we already have churn predictions, use those (assuming 'churn_prob' column exists)
    # Otherwise, use actual churn as a proxy
    if 'churn_prob' in df.columns:
        # Use median as threshold for high/low churn risk
        churn_median = df['churn_prob'].median()
        df['churn_risk'] = np.where(df['churn_prob'] >= churn_median, 'High Risk', 'Low Risk')
    else:
        # Use actual churn as proxy for risk
        df['churn_risk'] = np.where(df['churn'] == 1, 'High Risk', 'Low Risk')
    
    # Create targeting matrix segments (combinations of CLV quintile and churn risk)
    df['targeting_segment'] = df['clv_quintile'] + ' | ' + df['churn_risk']
    
    # Count customers in each segment
    segment_counts = df['targeting_segment'].value_counts().sort_index()
    print("Customer counts by targeting segment:")
    print(segment_counts)
    
    # Calculate average CLV and churn probability by segment
    segment_stats = df.groupby('targeting_segment').agg({
        'expected_clv': ['mean', 'median', 'count'],
        'churn': ['mean']
    })
    segment_stats.columns = ['CLV_Mean', 'CLV_Median', 'Count', 'Churn_Rate']
    segment_stats = segment_stats.sort_index()
    print("\nSegment statistics:")
    print(segment_stats)
    
    # Create matrix visualization of customer counts
    plt.figure(figsize=(12, 8))
    # Reshape data for heatmap
    matrix_data = pd.crosstab(
        df['clv_quintile'], 
        df['churn_risk'],
        values=df['expected_clv'],
        aggfunc='count'
    )
    # Ensure consistent order of quintiles (ascending)
    quintile_order = ['Q1 (Lowest)', 'Q2', 'Q3', 'Q4', 'Q5 (Highest)']
    matrix_data = matrix_data.reindex(quintile_order)
    
    # Plot heatmap
    sns.heatmap(matrix_data, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Number of Customers'})
    plt.title('Customer Targeting Matrix: CLV Quintile × Churn Risk')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'targeting_matrix_counts.png'))
    plt.close()
    
    # Create matrix visualization of average CLV
    plt.figure(figsize=(12, 8))
    # Reshape data for heatmap
    matrix_clv = pd.crosstab(
        df['clv_quintile'], 
        df['churn_risk'],
        values=df['expected_clv'],
        aggfunc='mean'
    )
    # Ensure consistent order of quintiles (ascending)
    matrix_clv = matrix_clv.reindex(quintile_order)
    
    # Plot heatmap
    sns.heatmap(matrix_clv, annot=True, fmt=".2f", cmap="YlGnBu", cbar_kws={'label': 'Average CLV ($)'})
    plt.title('Average CLV by Targeting Segment')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'targeting_matrix_clv.png'))
    plt.close()
    
    # Visualize CLV distribution by targeting segment
    plt.figure(figsize=(14, 10))
    # Use boxplot for distribution
    ax = sns.boxplot(x='targeting_segment', y='expected_clv', data=df, palette='viridis')
    plt.title('CLV Distribution by Targeting Segment')
    plt.xlabel('Targeting Segment')
    plt.ylabel('Expected CLV ($)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'targeting_segment_clv_distribution.png'))
    plt.close()
    
    # Generate report
    report = '# Customer Targeting Matrix: CLV × Churn Risk\n\n'
    
    # Overall approach
    report += '## Approach\n'
    report += 'This targeting matrix combines Customer Lifetime Value (CLV) quintiles with churn risk '
    report += 'to create a strategic framework for customer targeting and retention efforts. '
    report += 'The matrix allows for prioritization of resources based on both customer value and risk level.\n\n'
    
    # Matrix visualization
    report += '## Customer Targeting Matrix\n'
    report += '![Targeting Matrix](targeting_matrix_counts.png)\n\n'
    report += '### Average CLV by Segment\n'
    report += '![Average CLV by Segment](targeting_matrix_clv.png)\n\n'
    report += '### CLV Distribution by Segment\n'
    report += '![CLV Distribution by Segment](targeting_segment_clv_distribution.png)\n\n'
    
    # Segment statistics
    report += '## Segment Statistics\n'
    report += segment_stats.to_markdown() + '\n\n'
    
    # Strategic recommendations by segment
    report += '## Strategic Recommendations by Segment\n\n'
    
    # High-value, high-risk
    report += '### Q5 (Highest) | High Risk\n'
    report += '- **Priority**: ★★★★★ (Highest priority)\n'
    report += '- **Strategy**: Proactive retention and service recovery\n'
    report += '- **Actions**: \n'
    report += '  - Immediate outreach by dedicated account managers\n'
    report += '  - Premium retention offers with high-value incentives\n'
    report += '  - Personalized service quality improvements\n'
    report += '  - Executive attention for service recovery if needed\n'
    report += '- **Investment Level**: High - these customers represent the highest potential revenue loss\n\n'
    
    # High-value, low-risk
    report += '### Q5 (Highest) | Low Risk\n'
    report += '- **Priority**: ★★★★☆\n'
    report += '- **Strategy**: Loyalty cultivation and share of wallet expansion\n'
    report += '- **Actions**: \n'
    report += '  - Loyalty recognition and rewards program\n'
    report += '  - Cross-sell and upsell premium services\n'
    report += '  - Proactive communication about new services\n'
    report += '  - Exclusive customer appreciation events\n'
    report += '- **Investment Level**: Medium-high - focus on deepening already strong relationships\n\n'
    
    # Q4 high-risk
    report += '### Q4 | High Risk\n'
    report += '- **Priority**: ★★★★☆\n'
    report += '- **Strategy**: Targeted retention and relationship strengthening\n'
    report += '- **Actions**: \n'
    report += '  - Personalized retention offers\n'
    report += '  - Service quality review and improvement\n'
    report += '  - Tailored communications addressing pain points\n'
    report += '  - Contract renewal incentives\n'
    report += '- **Investment Level**: Medium-high - significant value at risk\n\n'
    
    # Q4 low-risk
    report += '### Q4 | Low Risk\n'
    report += '- **Priority**: ★★★☆☆\n'
    report += '- **Strategy**: Growth and value enhancement\n'
    report += '- **Actions**: \n'
    report += '  - Usage incentives for additional services\n'
    report += '  - Educational content about premium features\n'
    report += '  - Periodic check-ins and relationship development\n'
    report += '  - Community building and engagement\n'
    report += '- **Investment Level**: Medium - focus on steady growth\n\n'
    
    # Q3 segments
    report += '### Q3 | High Risk\n'
    report += '- **Priority**: ★★★☆☆\n'
    report += '- **Strategy**: Selective retention and satisfaction improvement\n'
    report += '- **Actions**: \n'
    report += '  - Targeted retention offers based on usage patterns\n'
    report += '  - Satisfaction surveys and follow-up\n'
    report += '  - Service enhancements for key pain points\n'
    report += '- **Investment Level**: Medium - balance retention costs against customer value\n\n'
    
    report += '### Q3 | Low Risk\n'
    report += '- **Priority**: ★★☆☆☆\n'
    report += '- **Strategy**: Engagement and incremental growth\n'
    report += '- **Actions**: \n'
    report += '  - Engagement campaigns focusing on underutilized services\n'
    report += '  - Value-based upsell opportunities\n'
    report += '  - Digital relationship maintenance\n'
    report += '- **Investment Level**: Medium-low - efficient engagement\n\n'
    
    # Q2 segments
    report += '### Q2 | High Risk\n'
    report += '- **Priority**: ★★☆☆☆\n'
    report += '- **Strategy**: Efficiency-focused retention\n'
    report += '- **Actions**: \n'
    report += '  - Cost-effective retention offers\n'
    report += '  - Digital self-service improvements\n'
    report += '  - Automated satisfaction monitoring\n'
    report += '- **Investment Level**: Low-medium - automated approaches preferred\n\n'
    
    report += '### Q2 | Low Risk\n'
    report += '- **Priority**: ★☆☆☆☆\n'
    report += '- **Strategy**: Basic maintenance and selective growth\n'
    report += '- **Actions**: \n'
    report += '  - Automated engagement and education\n'
    report += '  - Entry-level service improvements\n'
    report += '  - Digital relationship building\n'
    report += '- **Investment Level**: Low - maintain through efficient systems\n\n'
    
    # Q1 segments
    report += '### Q1 (Lowest) | High Risk\n'
    report += '- **Priority**: ★☆☆☆☆\n'
    report += '- **Strategy**: Selective intervention based on potential\n'
    report += '- **Actions**: \n'
    report += '  - Automated retention for customers with growth potential\n'
    report += '  - Basic service quality maintenance\n'
    report += '  - Minimal intervention for others\n'
    report += '- **Investment Level**: Very low - minimal resources allocated\n\n'
    
    report += '### Q1 (Lowest) | Low Risk\n'
    report += '- **Priority**: ☆☆☆☆☆ (Lowest priority)\n'
    report += '- **Strategy**: Efficiency and self-service\n'
    report += '- **Actions**: \n'
    report += '  - Maintain basic service through efficient systems\n'
    report += '  - Digital-first approach to customer service\n'
    report += '  - Low-cost community support options\n'
    report += '- **Investment Level**: Minimal - focus on operational efficiency\n\n'
    
    # Implementation recommendations
    report += '## Implementation Recommendations\n\n'
    report += '1. **Prioritize Resources**: Allocate customer management resources according to the segment priority ratings\n'
    report += '2. **Test and Learn**: Implement targeted initiatives for each segment and measure effectiveness\n'
    report += '3. **Dynamic Updates**: Regularly update the targeting matrix as customer behavior and value changes\n'
    report += '4. **Cross-Functional Alignment**: Ensure marketing, sales, and customer service are aligned on segment strategies\n'
    report += '5. **ROI Tracking**: Monitor return on investment for each segment-specific initiative\n'
    
    # Save report
    with open(os.path.join(base_dir, 'models', 'targeting_matrix_report.md'), 'w') as f:
        f.write(report)
    
    # Save updated dataset with targeting segments
    df.to_csv(os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_targeting.csv'), index=False)
    
    print('Targeting matrix creation complete. See models/targeting_matrix_report.md for the full report.')

if __name__ == '__main__':
    create_targeting_matrix() 