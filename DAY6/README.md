# Day-6: Student Score Prediction System

## Project Overview

In this project, I learned how to prepare data for Machine Learning and built my first Linear Regression model using Scikit-learn. The project includes data preprocessing, feature engineering, model training, prediction, evaluation, and visualization.

---

## Dataset

The dataset contains the following information about students:

- Student_ID
- Name
- Age
- Program
- Python Score
- Mathematics Score
- Statistics Score
- Machine Learning Score
- Attendance

A new column named **Average_Score** was created by calculating the average of the subject scores.

---

## Data Preprocessing

The following preprocessing steps were performed:

- Loaded the dataset using Pandas.
- Checked dataset information and statistics.
- Checked for missing values.
- Checked for duplicate records.
- Created a new column named **Average_Score**.
- Applied One-Hot Encoding to the **Program** column.
- Removed unnecessary columns such as Student_ID and Name.
- Selected Features (X) and Target (y).
- Split the dataset into Training (80%) and Testing (20%).
- Applied StandardScaler for feature scaling.

---

## Machine Learning

A Linear Regression model was built using Scikit-learn.

The workflow included:

- Training the model
- Predicting student average scores
- Comparing Actual vs Predicted values
- Evaluating model performance

---

## Evaluation Metrics Used

The following metrics were used to evaluate the model:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

---

## Visualization

A scatter plot was created using Seaborn to compare the Actual Average Scores with the Predicted Average Scores.

---

## What I Learned

- Importance of Data Preprocessing
- Features and Target Variables
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Train-Test Split
- Data Leakage and how to avoid it
- Machine Learning workflow
- Linear Regression using Scikit-learn
- Model evaluation using MAE, MSE, and R² Score

---

## Why Train-Test Split is Important

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

The training data is used to train the model, while the testing data is used to evaluate the model on unseen data. This helps determine how well the model generalizes to new data and prevents overfitting.

---

## Model Performance

The Linear Regression model successfully predicted student average scores.

### Evaluation Results

- Mean Absolute Error (MAE): Very close to 0
- Mean Squared Error (MSE): Very close to 0
- R² Score: 1.0

### Observations

The model achieved excellent performance because the target variable (**Average_Score**) was calculated directly from the subject scores used as input features. As a result, the Linear Regression model learned the relationship accurately and produced highly accurate predictions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Seaborn
- Matplotlib

---

## Project Files

- Practice.py
- model.py
- student_performance.csv
- preprocessed_student_performance.csv
- Actual_vs_Predicted.png
- README.md
