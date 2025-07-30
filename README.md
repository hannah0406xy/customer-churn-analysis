# Customer Churn Analysis & CLV Modeling Project

## 📊 Project Overview

This comprehensive analysis project examines customer churn patterns in the telecommunications industry using advanced machine learning techniques, survival analysis, and customer lifetime value (CLV) modeling. The project delivers actionable insights for customer retention strategies and revenue optimization.

## 🎯 Key Objectives

- **Predictive Modeling**: Develop ensemble models to predict customer churn with high accuracy
- **Survival Analysis**: Analyze customer retention patterns using Kaplan-Meier curves and Cox proportional hazards
- **CLV Analysis**: Calculate and segment customers by lifetime value
- **Pricing Optimization**: Develop data-driven pricing strategies for different customer segments
- **Targeting Matrix**: Create actionable customer targeting strategies based on churn risk and CLV

## 🏗️ Project Architecture

```
mrkt671_group_project-master/
├── data/processed/          # Processed datasets and analysis outputs
├── docs/                   # Project documentation and data dictionary
├── models/                 # Model outputs, visualizations, and reports
├── paper/                  # Academic paper and executive reports
├── scripts/               # Python analysis scripts
└── environment.yml        # Conda environment configuration
```

## 🔬 Methodology

### 1. **Data Preprocessing & Feature Engineering**
- Comprehensive data cleaning and validation
- Feature correlation analysis and multicollinearity detection
- Advanced feature engineering for predictive modeling

### 2. **Ensemble Machine Learning**
- **XGBoost**: Primary gradient boosting model with SHAP interpretation
- **Random Forest**: Robust ensemble method for feature importance
- **Logistic Regression**: Interpretable baseline model
- **CatBoost**: Advanced gradient boosting with categorical handling

### 3. **Survival Analysis**
- **Kaplan-Meier Curves**: Non-parametric survival analysis
- **Cox Proportional Hazards**: Multivariate survival modeling
- **Segment Analysis**: Survival patterns by customer segments

### 4. **Customer Lifetime Value (CLV) Modeling**
- **CLV Calculation**: Revenue-based lifetime value estimation
- **Quintile Analysis**: Customer segmentation by CLV
- **Segment Profiling**: Demographic and behavioral analysis

### 5. **Pricing & Retention Strategy**
- **Discount Impact Analysis**: Revenue optimization modeling
- **Segment Pricing**: Data-driven pricing recommendations
- **Retention Strategies**: Targeted intervention strategies

## 📈 Key Findings

### Model Performance
- **Ensemble Model**: Achieved superior performance across multiple metrics
- **XGBoost**: Best individual model with detailed SHAP interpretations
- **Feature Importance**: Service quality and usage patterns are key predictors

### Customer Insights
- **High-Value Customers**: Identified distinct CLV segments with different churn patterns
- **Retention Opportunities**: Found optimal discount levels for revenue maximization
- **Targeting Matrix**: Created actionable customer targeting strategies

### Business Impact
- **Revenue Optimization**: Identified pricing strategies that maximize profit
- **Customer Segmentation**: Developed data-driven customer classification
- **Predictive Capabilities**: Built models for proactive churn prevention

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Conda package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hannah0406xy/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. **Create conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate telechurn
   ```

3. **Run analysis scripts**
   ```bash
   # Data preprocessing
   python scripts/preprocess_data.py
   
   # Build baseline model
   python scripts/build_baseline_model.py
   
   # Run ensemble analysis
   python scripts/build_ensemble_model.py
   
   # Generate CLV analysis
   python scripts/compute_clv.py
   ```

## 📋 Analysis Scripts

### Core Analysis
- `preprocess_data.py` - Data cleaning and feature engineering
- `build_baseline_model.py` - Initial model development
- `build_ensemble_model.py` - Advanced ensemble modeling
- `compare_algorithms.py` - Model comparison and evaluation

### Advanced Analytics
- `survival_analysis.py` - Kaplan-Meier and Cox analysis
- `compute_clv.py` - Customer lifetime value calculation
- `segment_clv_quintiles.py` - CLV-based segmentation
- `pricing_analysis.py` - Revenue optimization modeling

### Model Interpretation
- `interpret_xgboost_shap.py` - SHAP analysis for model interpretability
- `residual_analysis_xgboost.py` - Model diagnostics
- `check_overfitting_xgboost.py` - Overfitting detection

### Business Applications
- `create_targeting_matrix.py` - Customer targeting strategies
- `churn_deep_dive.py` - Detailed churn analysis
- `correlation_analysis.py` - Feature correlation insights

## 📊 Outputs & Deliverables

### Model Reports
- `models/baseline_model_report.md` - Initial model performance
- `models/ensemble_model_report.md` - Advanced ensemble results
- `models/improved_model_report.md` - Optimized model performance
- `models/xgboost_shap_report.md` - Model interpretability analysis

### Business Analysis
- `models/clv_analysis_report.md` - Customer lifetime value insights
- `models/pricing_analysis_report.md` - Revenue optimization strategies
- `models/targeting_matrix_report.md` - Customer targeting recommendations
- `models/survival_analysis_report.md` - Retention pattern analysis

### Visualizations
- Model performance comparisons and ROC curves
- Feature importance plots and SHAP summaries
- Survival curves and CLV distributions
- Pricing optimization charts and targeting matrices

## 📚 Documentation

- `docs/data_dictionary.md` - Complete data documentation
- `docs/churn_deep_dive.md` - Detailed churn analysis
- `paper/executive_report.md` - Executive summary
- `paper/draft.md` - Academic paper draft

## 🤝 Contributing

This project was developed as part of MRKT671 coursework. For collaboration:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is part of academic coursework. All analysis and findings are for educational and research purposes.

---

*This project demonstrates advanced customer analytics techniques including machine learning, survival analysis, and customer lifetime value modeling for strategic business decision-making.* 
