import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model


def get_my_model_n():
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55,3)))
    model.add(Dense(165, activation='relu'))
    model.add(Dense(165, activation='relu'))
    model.add(Dense(55, activation='softmax'))
    model.summary()
    return model


def get_my_model_with_parameters(hidden_layers_amount=2, vertcal=1):
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55,3)))
    for _ in range(hidden_layers_amount):
        model.add(Dense(165*vertcal, activation='relu'))
    model.add(Dense(55, activation='softmax'))
    model.summary()
    return model