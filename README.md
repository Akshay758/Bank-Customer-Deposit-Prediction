# Bank Customer Deposit Prediction

## Project Overview
This project predicts whether a bank customer will subscribe to a term deposit based on demographic, financial, and marketing campaign data. Machine learning classification models were used to analyze customer behavior and identify potential customers who are more likely to subscribe to a bank deposit.

## Dataset Description
The dataset contains 17 customer-related features:

- **age** – Age of the customer  
- **job** – Type of job (admin, technician, management, etc.)  
- **marital** – Marital status (married, single, divorced)  
- **education** – Education level (primary, secondary, tertiary)  
- **default** – Has credit in default (yes/no)  
- **balance** – Average yearly balance (in euros)  
- **housing** – Has housing loan (yes/no)  
- **loan** – Has personal loan (yes/no)  
- **contact** – Communication type (cellular, telephone)  
- **day** – Last contact day of the month  
- **month** – Last contact month of the year  
- **duration** – Duration of the last contact in seconds  
- **campaign** – Number of contacts during this campaign  
- **pdays** – Days since the client was last contacted from previous campaign  
- **previous** – Number of contacts performed before this campaign  
- **poutcome** – Outcome of the previous marketing campaign  
- **y** – Target variable (whether the client subscribed to a term deposit)

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

## Machine Learning Models Used
Multiple classification algorithms were applied to compare model performance:

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree Classifier  
- Random Forest Classifier  
- Support Vector Machine (SVM)  
- Naive Bayes  
- Gradient Boosting  
- **XGBoost Classifier**

## Model Performance
Among all models, **XGBoost performed the best**.

- Initial XGBoost Accuracy: **80%**
- After applying **Hyperparameter Tuning**: **83% Accuracy**

Hyperparameter tuning was performed to optimize model parameters and improve prediction performance.

## Model Evaluation Metrics
The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Project Workflow
1. Data Collection  
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature Encoding & Scaling  
5. Model Training with Multiple Classification Algorithms  
6. Model Evaluation  
7. Hyperparameter Tuning for XGBoost  
8. Final Model Selection

## Conclusion
The project demonstrates how machine learning can be used to predict customer behavior in banking. By identifying customers who are more likely to subscribe to term deposits, banks can optimize marketing strategies and improve campaign efficiency.
