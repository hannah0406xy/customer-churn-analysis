# Customer Lifetime Value Optimization and Retention Strategy: A Survival Analysis Approach to Telecom Churn Management

## Group 671 - MRKT/INSY 671
Julian Bartlett, Ananya Sharma, Michael Chen, Samantha Rodriguez

---

## Introduction

### Problem Description
In the hypercompetitive telecommunications industry, customer churn presents a significant challenge with direct impact on revenue stability and growth. With customer acquisition costs 5-25 times higher than retention costs, telecom providers face increasing pressure to identify at-risk customers and implement effective retention strategies. Traditional approaches to churn management often rely on reactive measures after warning signs appear, and treat churn as a binary outcome rather than a time-dependent process. This study addresses these limitations by developing a comprehensive framework that integrates survival analysis with customer lifetime value (CLV) estimation to enable proactive, value-based retention strategies.

### Plan of Action
Our approach follows a systematic methodology that combines statistical rigor with practical business application:

1. **Survival Analysis**: We employ Kaplan-Meier estimation and Cox Proportional Hazards modeling to understand the time-dependent nature of customer churn across different segments.
2. **CLV Computation**: We integrate survival probabilities with revenue data to calculate expected customer lifetime value for each customer.
3. **Segmentation Framework**: We develop a two-dimensional targeting matrix that combines CLV quintiles with churn risk to prioritize retention efforts.
4. **Pricing Optimization**: We implement a two-part tariff model to maximize profit under current and segment-specific pricing strategies.
5. **Counterfactual Analysis**: We simulate the impact of various retention discount scenarios on overall profitability and identify optimal segment-specific strategies.

This methodological approach transforms churn management from a reactive classification problem into a proactive value optimization framework with time-based targeting mechanisms.

## Empirical Section

### Data Description
Our analysis utilizes a comprehensive telecom dataset comprising 100,000 customers with 73 variables spanning demographics, service usage, billing information, and churn status. Key variables include monthly usage (MOU), revenue (REV), customer service calls, dropped calls, and demographic factors including age. The data exhibits significant heterogeneity across customer segments, with monthly revenue ranging from $0 to $223.07 (mean: $53.64) and monthly usage from 0 to 3,360 minutes (mean: 615.7). Customer age distribution is bimodal, allowing for meaningful age segmentation (25-35 and 45-60 years). The churn rate in the dataset is 50%, providing balanced classes for modeling.

A notable data characteristic is the positive correlation between usage intensity and churn risk (r = 0.31, p < 0.001), challenging the conventional wisdom that higher engagement correlates with retention. This finding directed our modeling approach toward understanding the dynamic relationship between usage patterns and churn timing rather than simply predicting binary outcomes.

### Estimation Results
Our survival analysis revealed distinct patterns across customer segments, with significant differences in survival curves between revenue, age, and service segments (log-rank test: p < 0.05 for all segmentations). The Cox Proportional Hazards model identified key churn predictors including monthly usage (coef = 0.314, p < 0.001), customer care interactions (coef = 0.023, p < 1e-20), and age (coef = -0.127, p < 1e-96), confirming that higher usage correlates with increased churn risk while customer age acts as a protective factor.

The ensemble machine learning model, combining XGBoost, LightGBM, and CatBoost, achieved superior predictive performance (AUC = 0.847) compared to individual models. Feature importance analysis highlighted monthly usage, equipment age, and revenue fluctuations as the strongest predictors, aligning with the Cox model findings and providing a consistent view of churn dynamics across methodologies.

Building on these survival insights, we calculated individual Customer Lifetime Value (CLV) estimates, finding an average CLV of $28.45 with substantial variation across segments. Older customers demonstrated 3.24× higher median CLV ($34.57) compared to younger customers ($6.43), while basic service customers showed 2.55× higher median CLV than premium service customers, highlighting the importance of segment-specific retention strategies.

## Analytical Section

### Value-Based Optimization Framework
We formulated the customer retention problem as a value optimization challenge where the objective is to maximize total expected profit. The profit function incorporates both the revenue component (two-part tariff) and the cost component (acquisition and retention costs):

```
Profit = Σ[CLV_i × P(retention_i) - retention_cost_i × retention_effort_i]
```

Where:
- CLV_i is the estimated lifetime value of customer i
- P(retention_i) is the probability of retaining customer i (from survival models)
- retention_cost_i is the cost of retention efforts for customer i
- retention_effort_i is a binary decision variable indicating whether to target customer i

We implemented a two-part tariff structure with:
- A fixed fee component (F) applied to all customers
- A variable rate component (α) applied to the customer's monthly revenue

This pricing structure allows for price discrimination based on usage patterns and willingness to pay, extracting maximum consumer surplus while maintaining competitive positioning.

### Optimization Results
Our pricing optimization model identified an optimal fixed fee of $200 and variable rate of 50% of monthly revenue, potentially generating an estimated annual profit of $19 million. Segment-specific optimization revealed that the high-value, high-risk segment (Q5|High Risk) could yield $1.93 million in profit, making it the highest priority for retention efforts.

The targeting matrix approach enabled precise resource allocation by dividing customers into ten segments based on CLV quintiles and churn risk. For each segment, we developed tailored strategies ranging from premium retention offers for high-value, high-risk customers to efficient, automated management for low-value segments.

Importantly, our implementation of second-degree price discrimination through the two-part tariff structure proved more effective than both uniform pricing and retention discount strategies, demonstrating the value of segment-based approaches over blanket policies.

## Strategy Evaluation

### Candidate Strategies
Based on our empirical and analytical findings, we identified three candidate strategies:
1. **Uniform Pricing**: Single fixed fee and variable rate for all customers
2. **Segment-Based Pricing**: Differentiated pricing by CLV and risk segment
3. **Retention Discount**: Blanket discount rates (5%, 10%, 15%) on the variable rate component

### Counterfactual Analysis
Our counterfactual simulations demonstrated clear differences in profit outcomes across strategies:

| Strategy | Parameters | Annual Profit | Profit Δ |
|----------|------------|--------------|----------|
| Uniform Pricing | F=$200, α=50% | $19,008,297 | Baseline |
| Segment-Based | Varies by segment | $19,196,114 | +$187,817 |
| 5% Discount | F=$200, α=47.5% | $19,007,882 | -$415 |
| 10% Discount | F=$200, α=45% | $19,007,467 | -$830 |
| 15% Discount | F=$200, α=42.5% | $19,007,052 | -$1,244 |

The segment-based pricing strategy outperformed both uniform pricing and discount strategies, generating an additional $187,817 in annual profit. Notably, blanket retention discounts reduced profit across all discount rates, reinforcing the need for targeted rather than universal retention offers.

Additionally, our counterfactual analysis of segment-specific initiatives revealed that allocating 80% of the retention budget to the top two CLV quintiles could yield a 24% higher return on investment compared to uniform budget allocation.

### Conclusion
Based on our comprehensive analysis, we recommend implementing the segment-based pricing strategy with differentiated retention approaches guided by the CLV-risk targeting matrix. Specifically, high-value, high-risk customers should receive premium retention offers with dedicated account management, while low-value segments should be managed through efficient, automated systems. This approach not only maximizes immediate profitability but also optimizes long-term customer value and resource allocation, creating sustainable competitive advantage in customer retention. 