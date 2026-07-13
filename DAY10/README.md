# Fashion MNIST - Artificial Neural Network (ANN)

## 📌 Project Overview

This project demonstrates how to build a simple **Artificial Neural Network (ANN)** using TensorFlow/Keras to classify images from the **Fashion MNIST** dataset.

The model is trained to recognize different types of clothing items such as T-shirts, trousers, dresses, shoes, bags, and more.

---

## 📂 Dataset

The project uses the **Fashion MNIST** dataset, which is built into TensorFlow/Keras.

- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels (Grayscale)
- Number of Classes: 10

---

## 🎯 Project Objectives

- Load the Fashion MNIST dataset
- Explore the dataset (shape, labels, sample images)
- Normalize pixel values
- Build a simple Artificial Neural Network (ANN)
- Train the model
- Evaluate the model on the test dataset
- Display training and validation accuracy
- Make predictions on test images
- Compare predicted and actual labels

---

# What is Deep Learning?

Deep Learning is a branch of Machine Learning that uses Artificial Neural Networks (ANNs) with multiple layers to automatically learn patterns from data. It is widely used for image classification, object detection, speech recognition, and natural language processing.

---

# Machine Learning vs Deep Learning

| Machine Learning | Deep Learning |
|------------------|---------------|
| Requires manual feature extraction | Learns features automatically |
| Works well with smaller datasets | Usually requires large datasets |
| Simpler algorithms (Decision Trees, KNN, etc.) | Uses Artificial Neural Networks |
| Faster training | Longer training time |
| Best for structured data | Best for images, audio, and text |

---

# What is a Perceptron?

A Perceptron is the basic building block of an Artificial Neural Network.

It receives input values, multiplies them by weights, adds a bias, applies an activation function, and produces an output.

**Equation:**

```
Output = Activation(Σ(Input × Weight) + Bias)
```

---

# Activation Functions Used

## ReLU (Rectified Linear Unit)

- Used in the hidden layer
- Formula:

```
f(x) = max(0, x)
```

- Helps the network learn complex patterns
- Reduces the vanishing gradient problem

Example:

```python
Dense(128, activation="relu")
```

---

## Softmax

- Used in the output layer
- Converts outputs into probabilities
- Probabilities always sum to 1
- Used for multi-class classification

Example:

```python
Dense(10, activation="softmax")
```

---

# Model Architecture

```
Input Layer
      ↓
Flatten (28 × 28 → 784)
      ↓
Dense (128 Neurons, ReLU)
      ↓
Dense (10 Neurons, Softmax)
      ↓
Predicted Class
```

---

# Model Performance

- Training Accuracy: 88.50%
- Testing Accuracy: 87.90%

---

# Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib

---

# Learning Outcomes

Through this project, I learned:

- Loading datasets using TensorFlow/Keras
- Understanding training and testing datasets
- Data normalization
- Building an Artificial Neural Network
- Training and evaluating a deep learning model
- Making predictions on unseen images
- Comparing predicted and actual labels

---

