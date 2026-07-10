# Iris Flower Clustering & PCA Visualization

## Project Overview

This project uses the Iris dataset from Scikit-learn to perform **K-Means Clustering** and **Principal Component Analysis (PCA)**. The goal is to group similar flowers into clusters, reduce the dataset to two dimensions, and visualize the results.

---

## Dataset

* **Dataset:** Iris Dataset (Scikit-learn)
* **Features:**

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## What is Clustering?

Clustering is an **unsupervised learning** technique that groups similar data points into clusters based on their characteristics. K-Means clustering divides the dataset into a specified number of clusters by finding the centroid of each cluster.

---

## What is PCA?

Principal Component Analysis (PCA) is a **dimensionality reduction** technique that reduces the number of features while preserving most of the important information. In this project, PCA reduced the four original features to two principal components for easy visualization.

---

## How did you determine the best value of K?

The **Elbow Method** was used to determine the optimal value of K. WCSS (Within-Cluster Sum of Squares) was calculated for values of K from 1 to 10. The elbow point appeared at **K = 3**, where the decrease in WCSS became much slower, indicating the optimal number of clusters.

---

## What insights did you gain from the visualizations?

* K-Means successfully grouped the Iris dataset into **three clusters**.
* The scatter plot showed that similar flowers were grouped together.
* PCA reduced the dataset from four features to two principal components.
* The PCA visualization made the clusters easier to observe and compare while preserving most of the important information.

---

## Conclusion

This project demonstrated how **K-Means Clustering** can group similar data points and how **PCA** can reduce dimensionality for better visualization. Together, these techniques provide an effective way to analyze and understand unlabeled datasets.
