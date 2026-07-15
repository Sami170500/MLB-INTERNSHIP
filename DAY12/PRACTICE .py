import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
base=MobileNetV2(
    weights="imagenet",include_top=False,input_shape=(224,224,3)
)
base.summary()
base.trainable=False
m=Sequential([base,GlobalAveragePooling2D(),
              Dense(units=128,activation='relu'),Dense(units=2,activation='softmax')])
import tensorflow_datasets as tfds
(train_ds,test_ds)=tfds.load('cats_vs_dogs',split=['train[:80%]','train[80%:]'],as_supervised=True)
def preprocess(image,label):
    image=tf.image.resize(image,(224,224))
    image=image/255
    return image,label
train_ds=train_ds.map(preprocess)
test_ds=test_ds.map(preprocess)
