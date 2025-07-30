# Executive Insights Prompt

## Context
You are an AI assistant tasked with interpreting the results of a comprehensive customer churn analysis for a telecommunications company. Your goal is to create a narrative and actionable insights for an Amazon-level executive.

## Data and Results Overview

### Survival Analysis Results
- **Customer Segments:**
  - Revenue-based segmentation (High vs. Low Revenue)
  - Age-based segmentation (Young vs. Old)
  - Service-based segmentation (Basic vs. Premium)

- **Key Predictors (Cox Model):**
  - Revenue metrics (`rev_Mean`, `ovrrev_Mean`)
  - Usage metrics (`mou_Mean`, `totcalls`, `change_mou`)
  - Service quality (`custcare_Mean`, `drop_vce_Mean`)
  - Customer characteristics (`age1`, `age2`)

### Machine Learning Model Results
- **Model Performance:**
  - Ensemble Model (XGBoost, LightGBM, CatBoost):
    - Accuracy: 0.5985
    - Precision: 0.5666
    - Recall: 0.8073
    - F1 Score: 0.6659
    - ROC AUC: 0.6530

- **Key Features (by importance):**
  1. Equipment days (`eqpdays`)
  2. Usage trends (`mou_trend`)
  3. Customer tenure (`months`)
  4. Revenue-usage relationship (`revenue_usage_trend`)
  5. Service quality metrics (`care_quality_intensity`)

## Task
1. **Summarize Key Findings:**
   - Highlight the most significant insights from both survival analysis and machine learning models
   - Focus on metrics and patterns that impact business outcomes
   - Emphasize segment-specific behaviors and risks

2. **Create a Narrative:**
   - Connect the data insights to business implications
   - Explain how different customer segments behave
   - Highlight the relationship between service quality and churn

3. **Provide Actionable Insights:**
   - Recommend specific, data-driven actions
   - Prioritize recommendations based on impact and feasibility
   - Include timing and targeting suggestions

4. **Format Requirements:**
   - Use clear, concise bullet points
   - Focus on business impact
   - Include specific metrics and percentages
   - Avoid technical jargon

## Example Structure

### Key Findings
- Segment-specific churn patterns
- Critical risk factors
- Service quality impact
- Revenue implications

### Business Narrative
- Customer behavior patterns
- Service quality impact
- Revenue and retention relationships

### Actionable Recommendations
- Immediate actions
- Strategic initiatives
- Resource allocation suggestions

## Deliverable
A concise, data-driven narrative with actionable insights that an Amazon-level executive can use to make informed decisions about customer retention strategies and resource allocation. 