import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import os

# Load data
base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data.csv')
df = pd.read_csv(data_path)

# Prepare features and target
X = df.drop(['Customer_ID', 'churn'], axis=1)
y = df['churn']

# Split data (same as before)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load best XGBoost model
model_path = os.path.join(base_dir, 'models', 'best_model.joblib')
model = joblib.load(model_path)

# Predict on test set
y_test_pred = model.predict(X_test)

# Identify misclassified cases
misclassified = X_test[y_test != y_test_pred].copy()
misclassified['actual'] = y_test[y_test != y_test_pred]
misclassified['predicted'] = y_test_pred[y_test != y_test_pred]

# Separate false positives and false negatives
false_positives = misclassified[misclassified['actual'] == 0]
false_negatives = misclassified[misclassified['actual'] == 1]

# Summarize misclassified cases
output_dir = os.path.join(base_dir, 'models')
os.makedirs(output_dir, exist_ok=True)
report = '# XGBoost Residual Analysis\n\n'
report += f'Total misclassified cases: {len(misclassified)}\n'
report += f'False positives: {len(false_positives)}\n'
report += f'False negatives: {len(false_negatives)}\n\n'

# Analyze key features for misclassified cases
for feature in X_test.columns:
    fp_mean = false_positives[feature].mean()
    fn_mean = false_negatives[feature].mean()
    report += f'Feature: {feature}\n'
    report += f'  False Positives mean: {fp_mean:.4f}\n'
    report += f'  False Negatives mean: {fn_mean:.4f}\n\n'

with open(os.path.join(output_dir, 'xgboost_residual_analysis.md'), 'w') as f:
    f.write(report)

print('Residual analysis completed. See models/xgboost_residual_analysis.md') 