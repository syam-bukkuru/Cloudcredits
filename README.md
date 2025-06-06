# 📊 Customer Churn Prediction Project

This project aims to predict customer churn based on demographic, service usage, and contract information using classification models like **Random Forest** and **Logistic Regression**. The dataset includes key features like age, tenure, contract type, internet service, and monthly charges.

---
## 📌 Project Workflow

### 1️⃣ Data Loading & Inspection
- Load dataset using Pandas
- Identify and handle missing values (InternetService had ~30% missing — filled as 'No Internet')

---
### 2️⃣ Exploratory Data Analysis (EDA)

**Univariate Analysis**  
- Distribution of numerical variables like Age, Tenure, Monthly Charges  
- Distribution of categorical variables like Churn, Contract Type, Internet Service  

**Correlation Matrix**  
- Examined correlations among numeric features

**Bivariate Analysis**  
- Boxplots and barplots to explore relationships between variables like Churn vs Tenure, Churn vs Monthly Charges  
- Churn rate by Contract Type and Internet Service  

---
### 3️⃣ Data Preprocessing
- Label Encoding for target variable `Churn`
- Standard Scaling for numeric features
- One-Hot Encoding for categorical variables using `ColumnTransformer`
- Train-test split (80-20 split)

---
### 4️⃣ Model Building

- **Random Forest Classifier**
- **Logistic Regression**

Both models were evaluated using:
- Accuracy Score
- Classification Report
- ROC AUC Score
- ROC Curve Comparison

------

### 5️⃣ Model Evaluation

| Model               | Accuracy | AUC Score |
|:------------------:|:---------|:-----------|
| Random Forest        |  99.5 %  |  1.000    |
| Logistic Regression  |  94 %  |  0.991    |

---

### 6️⃣ Model Saving
- Saved trained models (`.pkl` files) for future inference
- Saved preprocessing pipeline for consistent data transformation during inference

---
## 📈 How to Run

1️⃣ Install dependencies:
```bash
. pip install pandas numpy matplotlib seaborn scikit-learn
. Open the Jupyter/Colab notebook churn_prediction_notebook.ipynb
. Run all cells sequentially
```
### 📊 Dataset Information
- **Source**: [Kaggle - Telecom Customer Churn Insights for Analysis](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis)
- **Size**: 1000 rows × 10 columns
- **Target Variable**: `Churn`