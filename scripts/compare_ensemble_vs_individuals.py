import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report, roc_curve, auc

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

# Load models
models_dir = os.path.join(base_dir, 'models')
model_files = {
    'XGBoost': 'xgboost_model.joblib',
    'LightGBM': 'lightgbm_model.joblib',
    'CatBoost': 'catboost_model.joblib'
}
models = {}
for name, fname in model_files.items():
    path = os.path.join(models_dir, fname)
    if os.path.exists(path):
        models[name] = joblib.load(path)

# Get predictions and metrics for each model
results = {}
for name, model in models.items():
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    results[name] = {
        'y_pred': y_pred,
        'y_proba': y_proba,
        'metrics': {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred),
            'Recall': recall_score(y_test, y_pred),
            'F1 Score': f1_score(y_test, y_pred),
            'ROC AUC': roc_auc_score(y_test, y_proba)
        },
        'fpr': roc_curve(y_test, y_proba)[0],
        'tpr': roc_curve(y_test, y_proba)[1],
        'roc_auc': auc(roc_curve(y_test, y_proba)[0], roc_curve(y_test, y_proba)[1])
    }

# Ensemble
probas = [results[name]['y_proba'] for name in results]
ensemble_proba = np.mean(probas, axis=0)
ensemble_pred = (ensemble_proba >= 0.5).astype(int)
results['Ensemble'] = {
    'y_pred': ensemble_pred,
    'y_proba': ensemble_proba,
    'metrics': {
        'Accuracy': accuracy_score(y_test, ensemble_pred),
        'Precision': precision_score(y_test, ensemble_pred),
        'Recall': recall_score(y_test, ensemble_pred),
        'F1 Score': f1_score(y_test, ensemble_pred),
        'ROC AUC': roc_auc_score(y_test, ensemble_proba)
    },
    'fpr': roc_curve(y_test, ensemble_proba)[0],
    'tpr': roc_curve(y_test, ensemble_proba)[1],
    'roc_auc': auc(roc_curve(y_test, ensemble_proba)[0], roc_curve(y_test, ensemble_proba)[1])
}

# Bar plot for metrics
metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC']
model_names = list(results.keys())
metrics_matrix = np.array([[results[m]['metrics'][metric] for metric in metrics_names] for m in model_names])

plt.figure(figsize=(10, 6))
for i, metric in enumerate(metrics_names):
    plt.bar(np.arange(len(model_names)) + i*0.15, metrics_matrix[:, i], width=0.15, label=metric)
plt.xticks(np.arange(len(model_names)) + 0.3, model_names)
plt.ylabel('Score')
plt.title('Model Performance Comparison')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(models_dir, 'ensemble_vs_individuals_metrics.png'))
plt.close()

# ROC curves
plt.figure(figsize=(8, 6))
for name in results:
    plt.plot(results[name]['fpr'], results[name]['tpr'], label=f"{name} (AUC={results[name]['roc_auc']:.2f})")
plt.plot([0, 1], [0, 1], 'k--', lw=1)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves: Ensemble vs Individual Models')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(models_dir, 'ensemble_vs_individuals_roc.png'))
plt.close()

# Markdown summary
report = '# Ensemble vs Individual Models Comparison\n\n'
report += '## Metrics Bar Plot\n'
report += '![Metrics Bar Plot](ensemble_vs_individuals_metrics.png)\n\n'
report += '## ROC Curves\n'
report += '![ROC Curves](ensemble_vs_individuals_roc.png)\n\n'
report += '## Metrics Table\n'
report += '| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |\n'
report += '|-------|----------|-----------|--------|----------|---------|\n'
for m in model_names:
    ms = results[m]['metrics']
    report += f"| {m} | {ms['Accuracy']:.4f} | {ms['Precision']:.4f} | {ms['Recall']:.4f} | {ms['F1 Score']:.4f} | {ms['ROC AUC']:.4f} |\n"

with open(os.path.join(models_dir, 'ensemble_vs_individuals_report.md'), 'w') as f:
    f.write(report)

print('Comparison and visualization complete. See models/ensemble_vs_individuals_report.md') 