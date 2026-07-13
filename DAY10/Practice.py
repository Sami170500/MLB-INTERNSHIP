import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense

M = Sequential()
M.add(input(shape=(4,)))
M.add(Dense(5, activation="relu"))
M.add(Dense(1, activation="sigmoid"))
M.summary()

M = Sequential()
M.add(Input(shape=(4,)))
M.add(Dense(5, activation="sigmoid"))
M.add(Dense(1, activation="sigmoid"))
M.summary()


M = Sequential()
M.add(input(shape=(4,)))
M.add(Dense(5, activation="relu"))
M.add(Dense(1, activation="sigmoid"))
M.summary()

M = Sequential()
M.add(input(shape=(4,)))
M.add(Dense(5, activation="tanh"))
M.add(Dense(1, activation="sigmoid"))
M.summary()
