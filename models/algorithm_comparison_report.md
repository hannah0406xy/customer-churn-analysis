# Algorithm Comparison Report

Generated on: 2025-05-20 20:03:13

## Performance Metrics Comparison
| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|----------|-----------|---------|-----------|----------|
| Random Forest | 0.6309 | 0.6271 | 0.6297 | 0.6284 | 0.6812 |
| XGBoost | 0.6431 | 0.6372 | 0.6502 | 0.6436 | 0.6992 |
| LightGBM | 0.6368 | 0.6311 | 0.6430 | 0.6369 | 0.6980 |
| CatBoost | 0.6322 | 0.6259 | 0.6410 | 0.6334 | 0.6890 |
| Neural Network | 0.6022 | 0.5984 | 0.6003 | 0.5993 | 0.6405 |

## Feature Importance (Top 10) for Tree-based Models

### Random Forest
| Feature | Importance |
|---------|------------|
| eqpdays | 0.0271 |
| months | 0.0210 |
| mou_trend | 0.0204 |
| revenue_usage_trend | 0.0146 |
| device_price_impact | 0.0137 |
| quality_trend_impact | 0.0136 |
| care_quality_intensity | 0.0134 |
| care_trend_impact | 0.0132 |
| rev_trend | 0.0129 |
| totrev | 0.0128 |

### XGBoost
| Feature | Importance |
|---------|------------|
| eqpdays | 0.0480 |
| months | 0.0308 |
| refurb_new | 0.0233 |
| mou_trend | 0.0195 |
| hnd_price | 0.0182 |
| usage_pattern_score | 0.0149 |
| age1 | 0.0125 |
| totmrc_Range | 0.0125 |
| rev_Range | 0.0121 |
| kid6_10 | 0.0119 |

### LightGBM
| Feature | Importance |
|---------|------------|
| mou_trend | 119.0000 |
| totmrc_Range | 113.0000 |
| months | 108.0000 |
| totmrc_Mean | 108.0000 |
| eqpdays | 77.0000 |
| revenue_usage_trend | 67.0000 |
| avgqty | 66.0000 |
| hnd_price | 61.0000 |
| crclscod | 59.0000 |
| usage_pattern_score | 55.0000 |

### CatBoost
| Feature | Importance |
|---------|------------|
| months | 12.4694 |
| eqpdays | 11.2091 |
| mou_trend | 10.6662 |
| totmrc_Range | 4.6528 |
| totmrc_Mean | 4.4261 |
| hnd_price | 3.7303 |
| peak_usage_ratio | 2.7080 |
| avgqty | 2.4886 |
| mou_Mean | 2.2327 |
| crclscod | 2.2099 |
