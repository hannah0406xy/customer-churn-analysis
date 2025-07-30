import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
from datetime import datetime
from tqdm import tqdm

def load_and_prepare_data():
    """Load and prepare the data for modeling"""
    print("Loading and preparing data...")
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'modeling_data.csv')
    df = pd.read_csv(data_path)
    
    # Prepare features and target
    X = df.drop(['Customer_ID', 'churn'], axis=1)
    y = df['churn']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns

def train_and_evaluate_models(X_train, X_test, y_train, y_test, feature_names):
    """Train and evaluate multiple models"""
    # Define models with optimized parameters
    models = {
        'Random Forest': RandomForestClassifier(
            n_estimators=100,  # Reduced from 257
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features='sqrt',
            random_state=42,
            n_jobs=-1
        ),
        'XGBoost': xgb.XGBClassifier(
            n_estimators=100,  # Reduced from 200
            max_depth=6,
            learning_rate=0.1,
            random_state=42,
            n_jobs=-1,
            early_stopping_rounds=10,
            eval_metric='auc'
        ),
        'LightGBM': lgb.LGBMClassifier(
            n_estimators=100,  # Reduced from 200
            max_depth=6,
            learning_rate=0.1,
            random_state=42,
            n_jobs=-1
        ),
        'CatBoost': CatBoostClassifier(
            iterations=100,  # Reduced from 200
            depth=6,
            learning_rate=0.1,
            random_state=42,
            verbose=False,
            early_stopping_rounds=10
        ),
        'Neural Network': MLPClassifier(
            hidden_layer_sizes=(50,),  # Simplified architecture
            max_iter=100,  # Reduced from 200
            random_state=42
        )
    }
    
    # Dictionary to store results
    results = {}
    
    # Train and evaluate each model with progress bar
    for name, model in tqdm(models.items(), desc="Training Models"):
        print(f"\nTraining {name}...")
        
        # Train model with early stopping for gradient boosting models
        if name == 'XGBoost':
            eval_set = [(X_test, y_test)]
            model.fit(
                X_train, y_train,
                eval_set=eval_set,
                verbose=False
            )
        elif name == 'LightGBM':
            eval_set = [(X_test, y_test)]
            model.fit(
                X_train, y_train,
                eval_set=eval_set,
                callbacks=[lgb.early_stopping(10)]
            )
        elif name == 'CatBoost':
            eval_set = [(X_test, y_test)]
            model.fit(
                X_train, y_train,
                eval_set=eval_set,
                verbose=False
            )
        else:
            model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        metrics = {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred),
            'Recall': recall_score(y_test, y_pred),
            'F1 Score': f1_score(y_test, y_pred),
            'ROC AUC': roc_auc_score(y_test, y_pred_proba)
        }
        
        # Store results
        results[name] = {
            'model': model,
            'metrics': metrics,
            'predictions': y_pred,
            'probabilities': y_pred_proba
        }
        
        print(f"{name} training completed.")
        print("Metrics:", metrics)
    
    return results

def generate_comparison_report(results, feature_names):
    """Generate a comprehensive comparison report"""
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate report
    report = '# Algorithm Comparison Report\n\n'
    report += f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n'
    
    # Performance Comparison
    report += '## Performance Metrics Comparison\n'
    report += '| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |\n'
    report += '|-------|----------|-----------|---------|-----------|----------|\n'
    
    for name, result in results.items():
        metrics = result['metrics']
        report += f"| {name} | {metrics['Accuracy']:.4f} | {metrics['Precision']:.4f} | "
        report += f"{metrics['Recall']:.4f} | {metrics['F1 Score']:.4f} | {metrics['ROC AUC']:.4f} |\n"
    
    # Feature Importance for tree-based models
    report += '\n## Feature Importance (Top 10) for Tree-based Models\n'
    tree_models = ['Random Forest', 'XGBoost', 'LightGBM', 'CatBoost']
    
    for name in tree_models:
        if name in results:
            model = results[name]['model']
            if hasattr(model, 'feature_importances_'):
                importance = pd.DataFrame({
                    'Feature': feature_names,
                    'Importance': model.feature_importances_
                }).sort_values('Importance', ascending=False)
                
                report += f'\n### {name}\n'
                report += '| Feature | Importance |\n'
                report += '|---------|------------|\n'
                for _, row in importance.head(10).iterrows():
                    report += f"| {row['Feature']} | {row['Importance']:.4f} |\n"
    
    # Save best model
    best_model_name = max(results.items(), key=lambda x: x[1]['metrics']['ROC AUC'])[0]
    best_model = results[best_model_name]['model']
    joblib.dump(best_model, os.path.join(output_dir, 'best_model.joblib'))

    # Save individual models for ensembling
    if 'XGBoost' in results:
        joblib.dump(results['XGBoost']['model'], os.path.join(output_dir, 'xgboost_model.joblib'))
    if 'LightGBM' in results:
        joblib.dump(results['LightGBM']['model'], os.path.join(output_dir, 'lightgbm_model.joblib'))
    if 'CatBoost' in results:
        joblib.dump(results['CatBoost']['model'], os.path.join(output_dir, 'catboost_model.joblib'))

    # Generate comparison plots
    # 1. Performance Metrics Comparison
    metrics_df = pd.DataFrame({
        name: result['metrics'] for name, result in results.items()
    }).T
    
    plt.figure(figsize=(12, 6))
    metrics_df.plot(kind='bar', rot=45)
    plt.title('Model Performance Comparison')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'model_comparison.png'))
    plt.close()
    
    # Save report
    with open(os.path.join(output_dir, 'algorithm_comparison_report.md'), 'w') as f:
        f.write(report)
    
    print(f"\nBest performing model: {best_model_name}")
    print("Comparison report and plots have been saved to the models directory.")

def main():
    # Load and prepare data
    X_train, X_test, y_train, y_test, feature_names = load_and_prepare_data()
    
    # Train and evaluate models
    results = train_and_evaluate_models(X_train, X_test, y_train, y_test, feature_names)
    
    # Generate comparison report
    generate_comparison_report(results, feature_names)

if __name__ == '__main__':
    main() 