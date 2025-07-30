import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

def build_baseline_model():
    # Load modeling data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'modeling_data.csv')
    df = pd.read_csv(data_path)
    
    # Prepare features and target
    X = df.drop(['Customer_ID', 'churn'], axis=1)
    y = df['churn']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Initialize and train Random Forest model
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1
    )
    
    # Train model
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1 Score': f1_score(y_test, y_pred),
        'ROC AUC': roc_auc_score(y_test, y_pred_proba)
    }
    
    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Get feature importance
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save model
    model_path = os.path.join(output_dir, 'baseline_rf_model.joblib')
    joblib.dump(rf_model, model_path)
    
    # Generate and save plots
    # 1. Confusion Matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig(os.path.join(output_dir, 'confusion_matrix.png'))
    plt.close()
    
    # 2. Feature Importance Plot
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance.head(20))
    plt.title('Top 20 Most Important Features')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'feature_importance.png'))
    plt.close()
    
    # Generate markdown report
    report = '# Baseline Model Performance Report\n\n'
    
    # Model Overview
    report += '## Model Overview\n'
    report += '- Model Type: Random Forest Classifier\n'
    report += '- Number of Trees: 100\n'
    report += '- Training Set Size: {:,}\n'.format(len(X_train))
    report += '- Test Set Size: {:,}\n\n'.format(len(X_test))
    
    # Performance Metrics
    report += '## Performance Metrics\n'
    report += '| Metric | Score |\n'
    report += '|--------|-------|\n'
    for metric, score in metrics.items():
        report += f'| {metric} | {score:.4f} |\n'
    
    # Classification Report
    report += '\n## Detailed Classification Report\n'
    report += '```\n'
    report += classification_report(y_test, y_pred)
    report += '```\n\n'
    
    # Top Features
    report += '## Top 20 Most Important Features\n'
    report += '| Feature | Importance Score |\n'
    report += '|---------|-----------------|\n'
    for _, row in feature_importance.head(20).iterrows():
        report += f'| {row["Feature"]} | {row["Importance"]:.4f} |\n'
    
    # Save report
    with open(os.path.join(output_dir, 'baseline_model_report.md'), 'w') as f:
        f.write(report)
    
    print('Baseline model training completed. Check the models directory for results.')

if __name__ == '__main__':
    build_baseline_model() 