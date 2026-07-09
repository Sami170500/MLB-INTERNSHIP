# Breast Cancer Prediction System

## Project Overview

This project builds a **Breast Cancer Prediction System** using the **Breast Cancer Wisconsin Diagnostic Dataset** available in the Scikit-learn library. A Logistic Regression model is trained to classify tumors as **Malignant** or **Benign**. Hyperparameter tuning is performed using **GridSearchCV** to find the best model parameters.

---

## Objectives

* Load the Breast Cancer dataset.
* Perform basic data exploration.
* Check for missing and duplicate values.
* Split the dataset into training and testing sets.
* Preprocess the data using `StandardScaler`.
* Train a Logistic Regression model.
* Evaluate the baseline model.
* Perform Hyperparameter Tuning using `GridSearchCV`.
* Compare the baseline model with the tuned model.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn

---

## Libraries Used

```python
pandas
scikit-learn
```

---

## Workflow

1. Load Breast Cancer dataset.
2. Create a DataFrame.
3. Perform Exploratory Data Analysis (EDA).
4. Check target class distribution.
5. Split data into training and testing sets.
6. Scale features using `StandardScaler`.
7. Train the Logistic Regression model.
8. Evaluate the baseline model.
9. Apply `GridSearchCV` for hyperparameter tuning.
10. Evaluate the tuned model.
11. Compare baseline and tuned model performance.

---

## Evaluation Metrics

The following metrics are used:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Hyperparameter Tuning

GridSearchCV is used to search for the best values of:

* `C`
* `max_iter`

Example parameter grid:

```python
params = {
    "C": [0.01, 0.1, 1, 10, 100],
    "max_iter": [100, 500, 700, 1000]
}
```

---

## Results

The project displays:

* Baseline Model Accuracy
* Tuned Model Accuracy
* Best Hyperparameters
* Best Cross Validation Score
* Best Estimator
* Precision
* Recall
* F1 Score

---

## Learning Outcomes

After completing this project, you will understand:

* Classification using Logistic Regression.
* Data preprocessing using StandardScaler.
* Model evaluation techniques.
* Hyperparameter tuning using GridSearchCV.
* Selecting the best model based on evaluation metrics.

---

## Conclusion

This project demonstrates a complete machine learning classification pipeline, including data preprocessing, model training, evaluation, and hyperparameter tuning. GridSearchCV helps identify the optimal model parameters, improving model reliability and performance.
