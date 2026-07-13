from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
print(X_train.shape)
print(X_test.shape)
print(y_train[2])
print(np.unique(y_train))
plt.imshow(X_train[2],cmap='gray')
plt.title(y_train[2])
plt.show()
print(X_test[0])
X_train=X_train/255
X_test=X_test/255
print(X_test[0])
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense
m=Sequential()
m.add(Flatten(input_shape=(28,28)))
m.add(Dense(128,activation="relu"))
m.add(Dense(10,activation="softmax"))
m.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
data =m.fit(X_train,y_train,epochs=1)
test_loss, test_accuracy = m.evaluate(X_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)
pre=m.predict(X_test)
print(pre[0])
print(pre[3])

for i in range(5):
    predicted_label = np.argmax(pre[i])
    print("Image Index:", i)
    print("Predicted Label:", predicted_label)
    print("Actual Label:", y_test[i])
    plt.imshow(X_test[i], cmap="gray")
    plt.title("Predicted: " + str(predicted_label) + " | Actual: " + str(y_test[i]))
    plt.axis("off")
    plt.show()
