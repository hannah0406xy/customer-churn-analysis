# Executive Insights Prompt

## Context
You are an AI assistant tasked with interpreting the results of a survival analysis and prior machine learning models on customer churn data. Your goal is to create a narrative and actionable insights for an Amazon-level executive.

## Data and Results
- **Survival Analysis Results:**
  - Kaplan-Meier curves stratified by revenue, age, and service segments.
  - Cox Proportional Hazards model summary with key predictors (e.g., `rev_Mean`, `mou_Mean`, `totcalls`, `custcare_Mean`, `age1`, `age2`, `change_mou`, `drop_vce_Mean`).
  - Average predicted survival function.
- **Prior Model Results:**
  - Classification models (e.g., XGBoost, LightGBM, CatBoost) performance metrics (accuracy, precision, recall, F1, ROC AUC).
  - Residual analysis and misclassified cases.

## Task
1. **Summarize Key Findings:**
   - Highlight the most significant insights from the survival analysis and prior models.
   - Focus on metrics, trends, and patterns that matter to a business executive.

2. **Create a Narrative:**
   - Tell a story that connects the data insights to business outcomes.
   - Explain how these insights can impact customer retention, revenue, and strategic decision-making.

3. **Provide Actionable Insights:**
   - Recommend specific, data-driven actions the executive can take.
   - Prioritize recommendations based on impact and feasibility.

4. **Format:**
   - Use bullet points for clarity.
   - Keep the language concise and business-focused.
   - Avoid technical jargon unless necessary.

## Example Output
- **Key Findings:**
  - High-revenue customers show a different churn pattern than low-revenue customers.
  - Younger customers churn faster than older customers.
  - Premium service customers have a higher churn risk than basic service customers.
  - The Cox model achieved a concordance index of 0.67, indicating moderate predictive power.

- **Narrative:**
  - Our analysis reveals that customer churn is not uniform across segments. High-revenue and premium service customers are at higher risk, while older customers are more loyal. This suggests that our retention strategies should be tailored to these segments to maximize impact.

- **Actionable Insights:**
  - **Targeted Retention:** Focus retention efforts on high-revenue and premium service customers, offering personalized incentives to reduce churn.
  - **Customer Care:** Improve customer care for segments with high dropped call rates to enhance satisfaction and reduce churn.
  - **Strategic Timing:** Use survival curves to time interventions for maximum impact, especially for high-risk segments.

## Deliverable
A concise, data-driven narrative with actionable insights that an Amazon-level executive can use to make informed decisions. 