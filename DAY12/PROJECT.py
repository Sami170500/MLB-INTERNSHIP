import tensorflow as tf
import tensorflow_datasets as tfds
(train_ds, test_ds), info = tfds.load(
    "cats_vs_dogs",
    split=["train[:80%]", "train[80%:]"],
    as_supervised=True,
    with_info=True
)
def preprocess(image, label):
    image = tf.image.resize(image, (224, 224))
    image = image / 255.0
    return image, label
train_ds = train_ds.map(preprocess)
test_ds = test_ds.map(preprocess)
BATCH_SIZE = 32
train_ds = train_ds.shuffle(1000).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
test_ds = test_ds.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
base = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)
base.trainable = False
model = Sequential([
    base,
    GlobalAveragePooling2D(),
    Dense(128, activation="relu"),
    Dense(2, activation="softmax")
])

model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=5
)

loss, accuracy = model.evaluate(test_ds)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)
class_names = ["Cat", "Dog"]

images, labels = next(iter(test_ds))

predictions = model.predict(images)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 12))

for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i])
    predicted_label = np.argmax(predictions[i])
    actual_label = labels[i].numpy()
    plt.title(
        f"Pred: {class_names[predicted_label]}\nActual: {class_names[actual_label]}"
    )
    plt.axis("off")

plt.tight_layout()
plt.show()
plt.figure(figsize=(8,5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()
