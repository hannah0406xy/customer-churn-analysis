# Baseline Model Performance Report

## Model Overview
- Model Type: Random Forest Classifier
- Number of Trees: 100
- Training Set Size: 80,000
- Test Set Size: 20,000

## Performance Metrics
| Metric | Score |
|--------|-------|
| Accuracy | 0.6255 |
| Precision | 0.6255 |
| Recall | 0.6090 |
| F1 Score | 0.6171 |
| ROC AUC | 0.6752 |

## Detailed Classification Report
```
              precision    recall  f1-score   support

           0       0.63      0.64      0.63     10088
           1       0.63      0.61      0.62      9912

    accuracy                           0.63     20000
   macro avg       0.63      0.63      0.63     20000
weighted avg       0.63      0.63      0.63     20000
```

## Top 20 Most Important Features
| Feature | Importance Score |
|---------|-----------------|
| eqpdays | 0.0231 |
| mou_trend | 0.0165 |
| months | 0.0152 |
| revenue_usage_trend | 0.0143 |
| quality_trend_impact | 0.0131 |
| device_price_impact | 0.0130 |
| care_trend_impact | 0.0128 |
| rev_trend | 0.0124 |
| loyalty_score | 0.0123 |
| care_quality_intensity | 0.0122 |
| change_mou | 0.0122 |
| totcalls | 0.0121 |
| totrev | 0.0121 |
| mou_Range | 0.0119 |
| avgqty | 0.0119 |
| usage_pattern_score | 0.0116 |
| plan_usage_efficiency | 0.0116 |
| change_rev | 0.0115 |
| peak_usage_ratio | 0.0114 |
| csa | 0.0114 |
