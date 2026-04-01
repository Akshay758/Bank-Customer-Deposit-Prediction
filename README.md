# 🏦 Bank Customer Deposit Prediction

> A machine learning project to predict whether a bank customer will subscribe to a term deposit — helping banks optimize marketing campaigns and target the right customers.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Workflow](#project-workflow)
- [Models Used](#models-used)
- [Results](#results)
- [Conclusion](#conclusion)

---

## Overview

Banks spend significant resources on marketing campaigns for term deposits. This project uses supervised machine learning classification to predict which customers are likely to subscribe, enabling smarter, data-driven outreach.

The model is trained on real-world customer demographic, financial, and campaign interaction data.

---

## Dataset

The dataset contains **17 features** per customer:

| Category | Features |
|---|---|
| **Demographics** | `age`, `job`, `marital`, `education` |
| **Financial** | `balance`, `default`, `housing`, `loan` |
| **Campaign Info** | `contact`, `day`, `month`, `duration`, `campaign` |
| **Previous Campaign** | `pdays`, `previous`, `poutcome` |
| **Target** | `y` — Did the customer subscribe? (`yes` / `no`) |

<details>
<summary>📋 Feature Descriptions</summary>

| Feature | Description |
|---|---|
| `age` | Age of the customer |
| `job` | Type of job (admin, technician, management, etc.) |
| `marital` | Marital status (married, single, divorced) |
| `education` | Education level (primary, secondary, tertiary) |
| `default` | Has credit in default (yes/no) |
| `balance` | Average yearly balance (in euros) |
| `housing` | Has a housing loan (yes/no) |
| `loan` | Has a personal loan (yes/no) |
| `contact` | Communication type (cellular, telephone) |
| `day` | Last contact day of the month |
| `month` | Last contact month of the year |
| `duration` | Duration of last contact in seconds |
| `campaign` | Number of contacts during this campaign |
| `pdays` | Days since last contact from a previous campaign |
| `previous` | Number of contacts before this campaign |
| `poutcome` | Outcome of the previous marketing campaign |
| `y` | **Target** — subscribed to term deposit (yes/no) |

</details>

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EC6B10?style=flat&logo=xgboost&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `matplotlib` & `seaborn` | Data visualization and EDA |
| `scikit-learn` | ML model training and evaluation |
| `xgboost` | Best-performing gradient boosting model |

---

## Project Workflow

```
1. Data Collection
       ↓
2. Data Cleaning & Preprocessing
       ↓
3. Exploratory Data Analysis (EDA)
       ↓
4. Feature Encoding & Scaling
       ↓
5. Model Training (8 Classifiers)
       ↓
6. Model Evaluation
       ↓
7. Hyperparameter Tuning (XGBoost)
       ↓
8. Final Model Selection
```

---

## Models Used

Eight classification algorithms were trained and benchmarked:

| Model | Notes |
|---|---|
| Logistic Regression | Baseline linear model |
| K-Nearest Neighbors | Distance-based classifier |
| Decision Tree | Interpretable tree-based model |
| Random Forest | Ensemble of decision trees |
| Support Vector Machine | Margin-based classifier |
| Naive Bayes | Probabilistic classifier |
| Gradient Boosting | Sequential ensemble method |
| **XGBoost** ⭐ | **Best performing model** |

### Evaluation Metrics

All models were evaluated using:

- ✅ Accuracy
- ✅ Precision
- ✅ Recall
- ✅ F1 Score
- ✅ Confusion Matrix

---

## Results

### 🏆 Best Model: XGBoost Classifier

| Stage | Accuracy |
|---|---|
| Initial XGBoost | 80% |
| After Hyperparameter Tuning | **83%** |

> Hyperparameter tuning was applied to the XGBoost model to optimize parameters such as learning rate, max depth, and number of estimators — resulting in a **3% accuracy improvement**.

---

## Conclusion

This project demonstrates how machine learning can meaningfully support banking operations. By accurately identifying customers likely to subscribe to term deposits, banks can:

- 🎯 **Target** the right customers more effectively
- 💰 **Reduce** wasted marketing spend
- 📈 **Improve** overall campaign conversion rates

The XGBoost model with hyperparameter tuning achieved the best performance at **83% accuracy**, making it a strong candidate for real-world deployment in customer outreach strategies.
