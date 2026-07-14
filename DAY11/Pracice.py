import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
(X_train,Y_train),(X_test,Y_test)=fashion_mnist.load_data()
print(X_train.shape)
print(X_test.shape)
print(set(Y_train))
print(len(set(Y_train)))
import matplotlib.pyplot as plt
for i in range(11):
    plt.imshow(X_train[i],cmap="gray")
    plt.title(Y_train[1])
plt.show()    
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
X_train=X_train/255
X_test=X_test/255
print(X_train[1])
print(X_test[0])
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
m=Sequential()
m.add(Conv2D(
    filters=30,kernel_size=(2,2),activation=('relu'),input_shape=(28,28,1)
))
m.add(MaxPooling2D(
    pool_size=(2,2)
))
m.add(Flatten())
m.add(Dense(
  units=128,activation="relu"  
))
m.add(Dense(
    units=10,activation="softmax"
))
m.summary()
m.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
train=m.fit(
    X_train,Y_train,epochs=2
)
m.evaluate(X_test, Y_test)
import numpy as np
predictions = m.predict(X_test)
Y_pred = np.argmax(predictions, axis=1)
print("actual:",Y_train[0])
print("predictied:",Y_pred[0])
