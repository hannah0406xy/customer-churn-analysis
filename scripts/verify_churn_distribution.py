import csv
import os
from collections import Counter

def analyze_churn_distribution():
    # Read the data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'Cell1.csv')
    
    # Initialize counter for churn values
    churn_counter = Counter()
    total_rows = 0
    
    # Read CSV file
    with open(data_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            churn_counter[row['churn']] += 1
            total_rows += 1
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate markdown report
    report = "# Churn Distribution Analysis\n\n"
    report += "## Raw Counts\n"
    report += "| Churn Status | Count |\n"
    report += "|-------------|--------|\n"
    for status, count in sorted(churn_counter.items()):
        report += f"| {status} | {count:,} |\n"
    
    report += "\n## Percentages\n"
    report += "| Churn Status | Percentage |\n"
    report += "|-------------|------------|\n"
    for status, count in sorted(churn_counter.items()):
        percentage = (count / total_rows) * 100
        report += f"| {status} | {percentage:.2f}% |\n"
    
    # Write report to file
    with open(os.path.join(output_dir, 'churn_distribution.md'), 'w') as f:
        f.write(report)

if __name__ == "__main__":
    analyze_churn_distribution() 