# Fashion MNIST Image Classifier using CNN

## Project Overview

This project implements an **Image Classification** model using a **Convolutional Neural Network (CNN)** on the **Fashion MNIST** dataset provided by TensorFlow/Keras. The model classifies grayscale images of clothing items into one of ten categories.

---

# Dataset

* **Dataset:** Fashion MNIST
* **Training Images:** 60,000
* **Testing Images:** 10,000
* **Image Size:** 28 × 28 pixels
* **Color Mode:** Grayscale
* **Number of Classes:** 10

Classes:

* T-shirt/Top
* Trouser
* Pullover
* Dress
* Coat
* Sandal
* Shirt
* Sneaker
* Bag
* Ankle Boot

---

# Why CNNs are Better than ANNs for Image Data

Artificial Neural Networks (ANNs) treat every pixel as an independent input and ignore the spatial relationship between neighboring pixels. This results in a very large number of parameters and poor performance on image data.

Convolutional Neural Networks (CNNs) are specifically designed for image processing. CNNs use convolution filters to automatically detect important features such as edges, textures, shapes, and patterns. They require fewer parameters due to weight sharing and preserve the spatial information of images, making them more accurate and computationally efficient for image classification.

---

# Purpose of Convolution and Pooling Layers

### Convolution Layer

The convolution layer applies learnable filters (kernels) over the image to extract useful features such as edges, corners, textures, and shapes. During training, the filter values (weights) are updated using backpropagation to improve feature extraction.

### Max Pooling Layer

The max pooling layer reduces the spatial dimensions of the feature maps by selecting the maximum value from each pooling window. This decreases computation, reduces overfitting, and helps the model focus on the most important features.

---

# Model Architecture

```
Input Layer
(28 × 28 × 1)

↓

Conv2D
32 Filters
Kernel Size = (3 × 3)
Activation = ReLU

↓

MaxPooling2D
Pool Size = (2 × 2)

↓

Flatten

↓

Dense Layer
150 Neurons
Activation = ReLU

↓

Output Layer
10 Neurons
Activation = Softmax
```

---

# Model Configuration

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Metric: Accuracy
* Epochs: 10
* Validation Split: 20%

---

# Results

### Training Accuracy

Approximately **97.7%**

### Validation Accuracy

Approximately **91.5%**


# Performance Evaluation

The model was evaluated using:

* Test Accuracy
* Training Accuracy Curve
* Validation Accuracy Curve
* Training Loss Curve
* Validation Loss Curve
* Confusion Matrix
* Actual vs Predicted Labels
* Correctly Classified Images
* Incorrectly Classified Images

---

# Graphs Included

* Training vs Validation Accuracy
* Training vs Validation Loss
* Confusion Matrix

---

# Challenges Faced

### Challenge 1

Understanding the difference between CNN layers such as Convolution, Pooling, Flatten, and Dense layers.

**Solution:** Studied the role of each layer and implemented them step by step.

### Challenge 2

Understanding the output of `model.predict()`.

**Solution:** Learned that the model returns class probabilities and used `numpy.argmax()` to convert probabilities into predicted class labels.

### Challenge 3

Understanding overfitting.

**Solution:** Compared training and validation accuracy/loss graphs and identified slight overfitting after approximately five epochs.

---

# Libraries Used

* TensorFlow
* Keras
* NumPy
* Matplotlib
* Scikit-learn

---

# Conclusion

A CNN model was successfully built and trained to classify Fashion MNIST images. The model achieved high training accuracy and good testing accuracy while demonstrating the effectiveness of convolution and pooling layers for image classification. The project also included visualization of training performance, confusion matrix analysis, and prediction of sample images.


* Training & Testing Video

---

