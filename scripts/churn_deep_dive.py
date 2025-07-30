import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_churn_deep_dive():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'Cell1.csv')
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs')
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(data_path)

    # Binning
    tenure_bins = [0, 6, 12, 24, 36, 48, 60, df['months'].max()]
    tenure_labels = ['<=6', '7-12', '13-24', '25-36', '37-48', '49-60', '>60']
    df['tenure_bin'] = pd.cut(df['months'], bins=tenure_bins, labels=tenure_labels, right=True, include_lowest=True)

    revenue_bins = [0, 20, 40, 60, 80, 100, df['rev_Mean'].max()]
    revenue_labels = ['<=20', '21-40', '41-60', '61-80', '81-100', '>100']
    df['revenue_bin'] = pd.cut(df['rev_Mean'], bins=revenue_bins, labels=revenue_labels, right=True, include_lowest=True)

    care_bins = [0, 1, 2, 3, 5, 10, df['custcare_Mean'].max()]
    care_labels = ['0', '1', '2', '3-5', '6-10', '>10']
    df['care_bin'] = pd.cut(df['custcare_Mean'], bins=care_bins, labels=care_labels, right=True, include_lowest=True)

    # Helper for markdown
    def make_table(title, group_col):
        grouped = df.groupby(group_col)['churn'].value_counts().unstack().fillna(0)
        grouped['Total'] = grouped.sum(axis=1)
        grouped['Churn Rate (%)'] = grouped.get(1, 0) / grouped['Total'] * 100
        md = f"## {title}\n| Bin | Churn=0 | Churn=1 | Churn Rate (%) |\n|-----|---------|---------|----------------|\n"
        for idx, row in grouped.iterrows():
            c0 = int(row.get(0, 0))
            c1 = int(row.get(1, 0))
            rate = row['Churn Rate (%)']
            md += f"| {idx} | {c0:,} | {c1:,} | {rate:.2f} |\n"
        md += "\n"
        return md

    md = "# Churn Deep Dive Analysis (Pandas)\n\n"
    md += make_table("Churn by Tenure (months)", 'tenure_bin')
    md += make_table("Churn by Average Monthly Revenue (rev_Mean)", 'revenue_bin')
    md += make_table("Churn by Customer Care Calls (custcare_Mean)", 'care_bin')

    with open(os.path.join(output_dir, 'churn_deep_dive.md'), 'w') as f:
        f.write(md)

    # Plots
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='tenure_bin', y='churn', estimator=lambda x: 100 * x.mean(), ci=None)
    plt.ylabel('Churn Rate (%)')
    plt.xlabel('Tenure (months)')
    plt.title('Churn Rate by Tenure')
    plt.savefig(os.path.join(output_dir, 'churn_by_tenure.png'))
    plt.close()

    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='revenue_bin', y='churn', estimator=lambda x: 100 * x.mean(), ci=None)
    plt.ylabel('Churn Rate (%)')
    plt.xlabel('Average Monthly Revenue')
    plt.title('Churn Rate by Revenue')
    plt.savefig(os.path.join(output_dir, 'churn_by_revenue.png'))
    plt.close()

    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='care_bin', y='churn', estimator=lambda x: 100 * x.mean(), ci=None)
    plt.ylabel('Churn Rate (%)')
    plt.xlabel('Customer Care Calls')
    plt.title('Churn Rate by Customer Care Calls')
    plt.savefig(os.path.join(output_dir, 'churn_by_care.png'))
    plt.close()

if __name__ == "__main__":
    analyze_churn_deep_dive() 