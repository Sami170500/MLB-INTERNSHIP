# Day-12: Transfer Learning - Cats vs Dogs Image Classifier

## Overview

This project demonstrates the use of **Transfer Learning** to build an image classifier that distinguishes between **Cats** and **Dogs** using the TensorFlow Datasets (TFDS) Cats vs Dogs dataset.

Instead of training a Convolutional Neural Network (CNN) from scratch, a pre-trained **MobileNetV2** model is used as the feature extractor. Custom classification layers are added on top of the pre-trained model to classify images into two categories: **Cat** and **Dog**.

---

## What is Transfer Learning?

Transfer Learning is a deep learning technique where a model that has already been trained on a large dataset is reused for a new but related task.

The pre-trained model has already learned useful image features such as edges, textures, shapes, and patterns. Instead of learning these features again, we use the existing knowledge and train only the final layers for our specific problem.

---

## Why did I choose MobileNetV2?

I selected **MobileNetV2** because:

- It is pre-trained on the ImageNet dataset.
- It provides high accuracy while being lightweight.
- It trains much faster than building a CNN from scratch.
- It requires fewer computational resources.
- It is suitable for mobile and edge devices.

---

## Dataset

- Dataset: Cats vs Dogs
- Source: TensorFlow Datasets (TFDS)
- Classes:
  - Cat
  - Dog

---

## Project Workflow

1. Load the Cats vs Dogs dataset using TFDS.
2. Resize all images to **224 × 224** pixels.
3. Normalize image pixel values.
4. Load the pre-trained MobileNetV2 model.
5. Freeze the base model layers.
6. Add custom Dense layers.
7. Compile the model.
8. Train the model.
9. Evaluate model performance.
10. Display sample predictions.
11. Plot training and validation accuracy and loss graphs.

---

## Experiments Performed

To improve model performance, I experimented with:

- Different numbers of epochs
- Different batch sizes
- Image preprocessing
- Freezing the MobileNetV2 base model
- Adding custom Dense layers
- Using the Adam optimizer


## Challenges Faced

- Training required significant time because of the large dataset.
- Choosing an appropriate batch size.
- Understanding how Transfer Learning works.
- Learning how to freeze the pre-trained model before training.
- Managing system resources during training.

---

## Lessons Learned

Through this project I learned:

- The concept of Transfer Learning.
- How pre-trained models reduce training time.
- How MobileNetV2 extracts image features.
- How to preprocess image datasets using TensorFlow.
- How to build image classification models using Keras.
- How to evaluate a deep learning model.
- How to visualize training and validation performance.

---

## Technologies Used

- Python
- TensorFlow
- TensorFlow Datasets (TFDS)
- Keras
- NumPy
- Matplotlib

---

## Files Included

- Transfer Learning Practice Script
- Cats vs Dogs Classifier Script / Notebook
- Training Accuracy Graph
- Training Loss Graph
- Sample Prediction Images
- README.md
- Screen Recording

---

## Conclusion

This project successfully demonstrates how Transfer Learning can be used to build an accurate image classifier with minimal training time. By using the pre-trained MobileNetV2 model, the classifier learns efficiently and achieves high validation accuracy while requiring significantly fewer computational resources than training a CNN from scratch.

