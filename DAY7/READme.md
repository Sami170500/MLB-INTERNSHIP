# Iris Flower Classification System

## Project Overview

This project demonstrates a Machine Learning classification model that predicts the species of an Iris flower based on four flower measurements using the Logistic Regression algorithm.

The project uses the built-in Iris dataset from Scikit-learn and evaluates the model using different classification metrics.

---

## Dataset

**Dataset:** Iris Dataset (Scikit-learn)

The dataset contains **150 samples** with **4 input features** and **3 target classes**.

### Features

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Target Classes

- Setosa
- Versicolor
- Virginica

---

## What is Classification?

Classification is a supervised Machine Learning technique used to predict categories or classes. The model learns from labeled data and predicts the class of new data.

Examples:
- Spam or Not Spam
- Disease Detection
- Face Recognition
- Flower Species Prediction

---

## Classification vs Regression

| Classification | Regression |
|----------------|------------|
| Predicts categories or labels | Predicts numerical values |
| Output is discrete | Output is continuous |
| Example: Spam Detection | Example: House Price Prediction |
| Example: Iris Flower Species | Example: Salary Prediction |

---

## Algorithm Used

**Logistic Regression**

Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability that a sample belongs to a particular class.

---

## Workflow

1. Load the Iris dataset.
2. Explore the dataset.
3. Split the dataset into training and testing sets.
4. Train the Logistic Regression model.
5. Predict the flower species.
6. Evaluate the model.
7. Display the Confusion Matrix.
8. Compare Actual vs Predicted values.

---

## Evaluation Metrics Used

The following metrics were used to evaluate the model:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## Model Performance

- Accuracy: **1.00 (100%)**
- Precision: **1.00**
- Recall: **1.00**
- F1-Score: **1.00**

---

## Observations

- The Logistic Regression model achieved excellent performance on the Iris dataset.
- All test samples were classified correctly.
- The Confusion Matrix showed no incorrect predictions.
- The Iris dataset is clean and well-separated, making it suitable for Logistic Regression.

---

## Libraries Used

- Python
- Pandas
- Scikit-learn

---

## Project Files

- classification_practice.py
- iris_classification.py
- README.md
- Confusion Matrix Screenshot
- Screen Recording

---

## Conclusion

This project demonstrates the complete workflow of a classification problem using Logistic Regression. The model successfully classified Iris flowers with high accuracy and performed well on all evaluation metrics.
