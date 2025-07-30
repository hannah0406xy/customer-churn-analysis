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

# Load available models
models_dir = os.path.join(base_dir, 'models')
model_files = {
    'xgboost': 'xgboost_model.joblib',
    'lightgbm': 'lightgbm_model.joblib',
    'catboost': 'catboost_model.joblib'
}
models = {}
for name, fname in model_files.items():
    path = os.path.join(models_dir, fname)
    if os.path.exists(path):
        models[name] = joblib.load(path)

if len(models) == 0:
    raise RuntimeError('No models found for ensembling.')

# Get predicted probabilities from each model
probas = []
for name, model in models.items():
    probas.append(model.predict_proba(X_test)[:, 1])

# Average probabilities
ensemble_proba = np.mean(probas, axis=0)
ensemble_pred = (ensemble_proba >= 0.5).astype(int)

# Evaluate ensemble
metrics = {
    'Accuracy': accuracy_score(y_test, ensemble_pred),
    'Precision': precision_score(y_test, ensemble_pred),
    'Recall': recall_score(y_test, ensemble_pred),
    'F1 Score': f1_score(y_test, ensemble_pred),
    'ROC AUC': roc_auc_score(y_test, ensemble_proba)
}

# Save report
used_models = ', '.join(models.keys())
report = f'# Custom Ensemble Model Performance ({used_models})\n\n'
report += '## Metrics\n'
for k, v in metrics.items():
    report += f'- {k}: {v:.4f}\n'
report += '\n## Classification Report\n'
report += '```\n' + classification_report(y_test, ensemble_pred) + '\n```\n'

with open(os.path.join(models_dir, 'ensemble_model_report.md'), 'w') as f:
    f.write(report)

print(f'Custom ensemble built and evaluated using: {used_models}. See models/ensemble_model_report.md') 