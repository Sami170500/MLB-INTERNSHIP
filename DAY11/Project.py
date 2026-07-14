import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
(X_train,Y_train),(X_test,Y_test)=fashion_mnist.load_data()
print(X_train.shape)
print(len(set(Y_train)))
X_train=X_train.reshape(-1,28,28,1)
X_test=X_test.reshape(-1,28,28,1)
X_test=X_test/255
X_train=X_train/255
print(X_train[0])
print(Y_train[0])
import matplotlib.pyplot as plt
for i in range(10):
    plt.imshow(X_train[i],cmap='gray')
    plt.title(Y_train[i])
    plt.show()
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense
m=Sequential()
m.add(Conv2D(
    filters=32,kernel_size=(3,3),activation='relu',input_shape=(28,28,1)
))
m.add(MaxPool2D(
    pool_size=(2,2)
))
m.add(Flatten())
m.add(Dense(
    units=150,activation="relu"
))
m.add(Dense(
    units=10,activation="softmax"
))
m.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
history=m.fit(
    X_train,Y_train,epochs=10,validation_split=0.2
)
m.evaluate(X_test,Y_test)
prediction=m.predict(X_test)
import numpy as np
y_pred=np.argmax(prediction,axis=1)
print("Actual :",Y_test[0])
print("Model Prediction:",y_pred[0])
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(Y_test, y_pred)
print(cm)
display = ConfusionMatrixDisplay(confusion_matrix=cm)
display.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()
