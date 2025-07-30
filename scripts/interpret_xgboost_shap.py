import pandas as pd
import numpy as np
import shap
import joblib
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

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

# Check if model is XGBoost
if 'XGB' not in str(type(model)):
    raise ValueError('The best model is not an XGBoost model. Please check model selection.')

# Compute SHAP values
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Create output directory
output_dir = os.path.join(base_dir, 'models')
os.makedirs(output_dir, exist_ok=True)

# 1. SHAP summary plot (global feature importance)
plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'xgboost_shap_summary.png'))
plt.close()

# 2. SHAP dependence plots for top 3 features
top_features = np.array(X_test.columns)[np.argsort(-np.abs(shap_values.values).mean(0))][:3]
for feature in top_features:
    plt.figure()
    shap.dependence_plot(feature, shap_values.values, X_test, show=False)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'xgboost_shap_dependence_{feature}.png'))
    plt.close()

# 3. Save a markdown summary
report = '# XGBoost SHAP Interpretation\n\n'
report += '## Global Feature Importance (SHAP Summary Plot)\n'
report += '![SHAP Summary](xgboost_shap_summary.png)\n\n'
report += '## Top 3 Feature Dependence Plots\n'
for feature in top_features:
    report += f'### {feature}\n'
    report += f'![SHAP Dependence {feature}](xgboost_shap_dependence_{feature}.png)\n\n'

with open(os.path.join(output_dir, 'xgboost_shap_report.md'), 'w') as f:
    f.write(report)

print('SHAP interpretation completed. Check the models directory for plots and report.') 