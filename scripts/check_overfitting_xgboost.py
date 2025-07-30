import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
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

# Evaluate on training set
y_train_pred = model.predict(X_train)
y_train_proba = model.predict_proba(X_train)[:, 1]
train_metrics = {
    'Accuracy': accuracy_score(y_train, y_train_pred),
    'Precision': precision_score(y_train, y_train_pred),
    'Recall': recall_score(y_train, y_train_pred),
    'F1 Score': f1_score(y_train, y_train_pred),
    'ROC AUC': roc_auc_score(y_train, y_train_proba)
}

# Evaluate on test set
y_test_pred = model.predict(X_test)
y_test_proba = model.predict_proba(X_test)[:, 1]
test_metrics = {
    'Accuracy': accuracy_score(y_test, y_test_pred),
    'Precision': precision_score(y_test, y_test_pred),
    'Recall': recall_score(y_test, y_test_pred),
    'F1 Score': f1_score(y_test, y_test_pred),
    'ROC AUC': roc_auc_score(y_test, y_test_proba)
}

# Save report
output_dir = os.path.join(base_dir, 'models')
os.makedirs(output_dir, exist_ok=True)
report = '# XGBoost Overfitting Check\n\n'
report += '## Training Set Performance\n'
for k, v in train_metrics.items():
    report += f'- {k}: {v:.4f}\n'
report += '\n## Test Set Performance\n'
for k, v in test_metrics.items():
    report += f'- {k}: {v:.4f}\n'
report += '\n## Training Classification Report\n'
report += '```\n' + classification_report(y_train, y_train_pred) + '\n```\n'
report += '\n## Test Classification Report\n'
report += '```\n' + classification_report(y_test, y_test_pred) + '\n```\n'

with open(os.path.join(output_dir, 'xgboost_overfitting_report.md'), 'w') as f:
    f.write(report)

print('Overfitting check completed. See models/xgboost_overfitting_report.md') 