import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from lifelines import CoxPHFitter, KaplanMeierFitter
from sklearn.model_selection import train_test_split
import joblib

# Load data
base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data.csv')
df = pd.read_csv(data_path)

# Prepare features and target
features = [
    'rev_Mean', 'mou_Mean', 'totcalls', 'custcare_Mean',
    'age1', 'age2', 'change_mou', 'drop_vce_Mean', 'ovrrev_Mean'
]
# Only keep features that exist in the dataframe
features = [f for f in features if f in df.columns]

# Create a survival dataset
survival_df = df[['Customer_ID', 'churn', 'eqpdays'] + features].copy()
survival_df = survival_df.rename(columns={'churn': 'event', 'eqpdays': 'duration'})

# Ensure all relevant columns are numeric and drop rows with missing/non-numeric values
cols_to_check = ['duration', 'event'] + features
cols_to_check = [col for col in cols_to_check if col in survival_df.columns]
print('Columns to check:', cols_to_check)
for col in cols_to_check:
    print(f"Column: {col}, Type: {type(survival_df[col])}")
    if not isinstance(survival_df[col], pd.Series):
        print(f"Skipping column {col} as it is not a Series.")
        continue
    survival_df[col] = pd.to_numeric(survival_df[col], errors='coerce')
survival_df = survival_df.dropna(subset=cols_to_check)

# Stratify by revenue segment (high vs. low)
median_revenue = survival_df['rev_Mean'].median()
survival_df['revenue_segment'] = np.where(survival_df['rev_Mean'] >= median_revenue, 'High Revenue', 'Low Revenue')

# Further stratify by age segment
median_age = survival_df['age1'].median()
survival_df['age_segment'] = np.where(survival_df['age1'] < median_age, 'Young', 'Old')

# Further stratify by service type
median_calls = survival_df['totcalls'].median()
survival_df['service_segment'] = np.where(survival_df['totcalls'] < median_calls, 'Basic', 'Premium')

# Kaplan-Meier curves by revenue segment
kmf = KaplanMeierFitter()
plt.figure(figsize=(8, 6))
for segment in survival_df['revenue_segment'].unique():
    mask = survival_df['revenue_segment'] == segment
    kmf.fit(survival_df.loc[mask, 'duration'], survival_df.loc[mask, 'event'], label=segment)
    kmf.plot_survival_function(ci_show=True)
plt.title('Kaplan-Meier Survival Curves by Revenue Segment')
plt.xlabel('Time (days)')
plt.ylabel('Survival Probability')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'models', 'km_by_revenue_segment.png'))
plt.close()

# Kaplan-Meier curves by age segment
plt.figure(figsize=(8, 6))
for segment in survival_df['age_segment'].unique():
    mask = survival_df['age_segment'] == segment
    kmf.fit(survival_df.loc[mask, 'duration'], survival_df.loc[mask, 'event'], label=segment)
    kmf.plot_survival_function(ci_show=True)
plt.title('Kaplan-Meier Survival Curves by Age Segment')
plt.xlabel('Time (days)')
plt.ylabel('Survival Probability')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'models', 'km_by_age_segment.png'))
plt.close()

# Kaplan-Meier curves by service segment
plt.figure(figsize=(8, 6))
for segment in survival_df['service_segment'].unique():
    mask = survival_df['service_segment'] == segment
    kmf.fit(survival_df.loc[mask, 'duration'], survival_df.loc[mask, 'event'], label=segment)
    kmf.plot_survival_function(ci_show=True)
plt.title('Kaplan-Meier Survival Curves by Service Segment')
plt.xlabel('Time (days)')
plt.ylabel('Survival Probability')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'models', 'km_by_service_segment.png'))
plt.close()

# Fit Cox Proportional Hazards model with multiple features
cph = CoxPHFitter()
cph.fit(survival_df[['duration', 'event'] + features], 'duration', 'event')

# Save Cox model
model_path = os.path.join(base_dir, 'models', 'cox_model.joblib')
joblib.dump(cph, model_path)

# Predict and plot the average survival function for the test set
surv_funcs = cph.predict_survival_function(survival_df[features])
mean_surv = surv_funcs.mean(axis=1)
plt.figure()
plt.plot(mean_surv.index, mean_surv.values, label='Average Predicted Survival')
plt.title('Average Predicted Survival Function (Cox Model, Multi-Feature)')
plt.xlabel('Time (days)')
plt.ylabel('Survival Probability')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'models', 'cox_predicted_survival_multifeature.png'))
plt.close()

# Save report
report = '# Refined Survival Analysis Report\n\n'
report += '## Kaplan-Meier Survival Curves by Revenue Segment\n'
report += '![KM by Revenue Segment](km_by_revenue_segment.png)\n\n'
report += '## Kaplan-Meier Survival Curves by Age Segment\n'
report += '![KM by Age Segment](km_by_age_segment.png)\n\n'
report += '## Kaplan-Meier Survival Curves by Service Segment\n'
report += '![KM by Service Segment](km_by_service_segment.png)\n\n'
report += '## Cox Proportional Hazards Model Summary (Multi-Feature)\n'
report += '```\n' + str(cph.summary) + '\n```\n'
report += '## Average Predicted Survival Function (Multi-Feature Cox Model)\n'
report += '![Predicted Survival Function](cox_predicted_survival_multifeature.png)\n'

with open(os.path.join(base_dir, 'models', 'survival_analysis_report.md'), 'w') as f:
    f.write(report)

print('Refined survival analysis complete. See models/survival_analysis_report.md') 