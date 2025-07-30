# Improved Model Performance Report

## Model Overview
- Model Type: Random Forest Classifier
- Best Parameters: {'max_depth': 20, 'max_features': 'sqrt', 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 257}
- Training Set Size: 80,000
- Test Set Size: 20,000

## Performance Metrics
| Metric | Score |
|--------|-------|
| Accuracy | 0.6354 |
| Precision | 0.6311 |
| Recall | 0.6363 |
| F1 Score | 0.6337 |
| ROC AUC | 0.6871 |

## Detailed Classification Report
```
              precision    recall  f1-score   support

           0       0.64      0.63      0.64     10088
           1       0.63      0.64      0.63      9912

    accuracy                           0.64     20000
   macro avg       0.64      0.64      0.64     20000
weighted avg       0.64      0.64      0.64     20000
```

## Top 20 Most Important Features
| Feature | Importance Score |
|---------|-----------------|
| eqpdays | 0.0267 |
| months | 0.0173 |
| mou_trend | 0.0169 |
| usage_trend_stability | 0.0137 |
| customer_value | 0.0137 |
| revenue_usage_trend | 0.0127 |
| device_price_impact | 0.0122 |
| revenue_trend_stability | 0.0117 |
| care_trend_impact | 0.0116 |
| care_per_month | 0.0116 |
| care_quality_intensity | 0.0115 |
| quality_trend_impact | 0.0115 |
| avgqty | 0.0114 |
| totcalls | 0.0112 |
| change_mou | 0.0112 |
| rev_trend | 0.0111 |
| revenue_consistency | 0.0110 |
| loyalty_score | 0.0108 |
| totrev | 0.0107 |
| usage_consistency | 0.0107 |

## New Engineered Features
| Feature | Description |
|---------|-------------|
| customer_value | Total revenue * months of service |
| revenue_per_month | Average monthly revenue |
| usage_consistency | Measure of usage pattern consistency |
| revenue_consistency | Measure of revenue pattern consistency |
| service_quality | Composite service quality score |
| usage_trend_stability | Measure of usage trend stability |
| revenue_trend_stability | Measure of revenue trend stability |
| value_quality_ratio | Interaction of customer value and service quality |
| usage_quality_ratio | Interaction of usage consistency and service quality |
| churn_risk | Composite churn risk score |
