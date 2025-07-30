import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
from scipy.stats import randint, uniform

def engineer_features(df):
    """Create additional features based on domain knowledge and baseline model insights"""
    # Create a copy to avoid modifying the original dataframe
    df_new = df.copy()
    
    # 1. Customer Value Features
    df_new['customer_value'] = df_new['totrev'] * df_new['months']
    df_new['revenue_per_month'] = df_new['totrev'] / df_new['months']
    
    # 2. Usage Pattern Features
    df_new['usage_consistency'] = 1 - (df_new['mou_Range'] / (df_new['mou_Mean'] + 1))
    df_new['revenue_consistency'] = 1 - (df_new['rev_Range'] / (df_new['rev_Mean'] + 1))
    
    # 3. Service Quality Features
    df_new['service_quality'] = 1 - (df_new['drop_rate'] + df_new['block_rate'])
    
    # 4. Trend Features
    df_new['usage_trend_stability'] = 1 - abs(df_new['mou_trend'])
    df_new['revenue_trend_stability'] = 1 - abs(df_new['rev_trend'])
    
    # 5. Interaction Features
    df_new['value_quality_ratio'] = df_new['customer_value'] * df_new['service_quality']
    df_new['usage_quality_ratio'] = df_new['usage_consistency'] * df_new['service_quality']
    
    # 6. Composite Features
    df_new['churn_risk'] = (
        df_new['drop_rate'] * 
        df_new['block_rate'] * 
        (1 - df_new['usage_consistency']) * 
        (1 - df_new['revenue_consistency'])
    )
    
    return df_new

def improve_model():
    # Load modeling data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'modeling_data.csv')
    df = pd.read_csv(data_path)
    
    # Engineer new features
    df = engineer_features(df)
    
    # Prepare features and target
    X = df.drop(['Customer_ID', 'churn'], axis=1)
    y = df['churn']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Define parameter distributions for RandomizedSearchCV
    param_dist = {
        'n_estimators': randint(100, 300),
        'max_depth': [None, 20],  # Reduced options
        'min_samples_split': [2, 5],  # Reduced options
        'min_samples_leaf': [1, 2],  # Reduced options
        'max_features': ['sqrt', 'log2']
    }
    
    # Initialize base model with early stopping
    base_model = RandomForestClassifier(
        random_state=42,
        n_jobs=-1,
        warm_start=True  # Enable warm start for faster training
    )
    
    # Initialize RandomizedSearchCV
    random_search = RandomizedSearchCV(
        estimator=base_model,
        param_distributions=param_dist,
        n_iter=20,  # Number of parameter settings to try
        cv=3,  # Reduced from 5 to 3 folds
        scoring='roc_auc',
        n_jobs=-1,
        verbose=1,
        random_state=42
    )
    
    # Perform random search
    print("Starting RandomizedSearchCV...")
    random_search.fit(X_train, y_train)
    
    # Get best model
    best_model = random_search.best_estimator_
    
    # Make predictions
    y_pred = best_model.predict(X_test)
    y_pred_proba = best_model.predict_proba(X_test)[:, 1]
    
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
        'Importance': best_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save model
    model_path = os.path.join(output_dir, 'improved_rf_model.joblib')
    joblib.dump(best_model, model_path)
    
    # Generate and save plots
    # 1. Confusion Matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig(os.path.join(output_dir, 'improved_confusion_matrix.png'))
    plt.close()
    
    # 2. Feature Importance Plot
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance.head(20))
    plt.title('Top 20 Most Important Features')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'improved_feature_importance.png'))
    plt.close()
    
    # Generate markdown report
    report = '# Improved Model Performance Report\n\n'
    
    # Model Overview
    report += '## Model Overview\n'
    report += '- Model Type: Random Forest Classifier\n'
    report += f'- Best Parameters: {random_search.best_params_}\n'
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
    
    # New Features Section
    report += '\n## New Engineered Features\n'
    report += '| Feature | Description |\n'
    report += '|---------|-------------|\n'
    report += '| customer_value | Total revenue * months of service |\n'
    report += '| revenue_per_month | Average monthly revenue |\n'
    report += '| usage_consistency | Measure of usage pattern consistency |\n'
    report += '| revenue_consistency | Measure of revenue pattern consistency |\n'
    report += '| service_quality | Composite service quality score |\n'
    report += '| usage_trend_stability | Measure of usage trend stability |\n'
    report += '| revenue_trend_stability | Measure of revenue trend stability |\n'
    report += '| value_quality_ratio | Interaction of customer value and service quality |\n'
    report += '| usage_quality_ratio | Interaction of usage consistency and service quality |\n'
    report += '| churn_risk | Composite churn risk score |\n'
    
    # Save report
    with open(os.path.join(output_dir, 'improved_model_report.md'), 'w') as f:
        f.write(report)
    
    print('Model improvement completed. Check the models directory for results.')

if __name__ == '__main__':
    improve_model() 