# Wine Quality Prediction using Machine Learning

## Project Overview
This project focuses on predicting the **quality of wine** using various **machine learning classification algorithms** based on its chemical properties. The objective is to analyze physicochemical features of wine and build a robust predictive model that can classify wine quality accurately.

Wine quality assessment is an important task in the food and beverage industry, and machine learning provides an efficient way to automate this decision-making process.

---

## Problem Statement
Given several chemical attributes of wine, predict whether the wine is of **good quality or bad quality**.

This is a **Supervised Machine Learning Classification Problem**.

---

## Dataset Information
- Dataset used: **Wine Quality Dataset**
- Source: UCI Machine Learning Repository
- Type: Structured tabular data
- Target Variable: `quality`

### Input Features:
- Fixed Acidity  
- Volatile Acidity  
- Citric Acid  
- Residual Sugar  
- Chlorides  
- Free Sulfur Dioxide  
- Total Sulfur Dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  

---

## Technologies & Tools Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow
1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Selection & Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Comparison
9. Final Model Selection

---

## Exploratory Data Analysis (EDA)
- Checked for missing values and data types
- Analyzed feature distributions
- Visualized correlations using heatmaps
- Identified important features affecting wine quality such as:
  - Alcohol
  - Volatile Acidity
  - Sulphates

---

## Machine Learning Models Used
The following models were trained and evaluated:

| Model Name | Description |
|-----------|-------------|
| Logistic Regression | Baseline linear classifier |
| Decision Tree Classifier | Rule-based tree model |
| Random Forest Classifier | Ensemble learning model |
| Support Vector Machine (SVM) | Margin-based classifier |
| K-Nearest Neighbors (KNN) | Distance-based classifier |

---

## Model Performance Comparison

| Model | Accuracy |
|------|----------|
| Logistic Regression | ~74% |
| Decision Tree | ~76% |
| KNN | ~78% |
| SVM | ~80% |
| **Random Forest** | **~83% (Best)** |

> Accuracy may slightly vary depending on random state and hyperparameters.

---

##  Best Model Selection
###  Random Forest Classifier (Selected Model)

**Reasons for Selection:**
- Achieved the **highest accuracy**
- Handles non-linear data effectively
- Reduces overfitting through ensemble learning
- Performs well with minimal feature engineering

---

##  Final Outcome
- The **Random Forest Classifier** was selected as the final prediction model.
- It demonstrated strong generalization capability on unseen data.
- The model can predict wine quality reliably using chemical features.

---

##  Evaluation Metrics Used
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

---

##  Future Improvements
- Hyperparameter tuning using GridSearchCV
- Try Gradient Boosting / XGBoost
- Convert classification into multi-class quality prediction
- Deploy the model using Flask or FastAPI

---

##  How to Run the Project
python wine_quality_prediction.ipynb
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
