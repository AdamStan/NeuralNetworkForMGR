import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np


def get_my_model_n():
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55,3)))
    model.add(Dense(55*3, activation='relu'))
    model.add(Dense(55, activation='softmax'))
    model.summary()
    return model