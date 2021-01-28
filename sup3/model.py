import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation
from keras.models import Model


def get_advance_model():
    input_plan = Input(shape=(55,3))
    input_room = Input(shape=(55,3))
    input_teacher = Input(shape=(55,3))
    
    combined = concatenate([input_plan, input_room, input_teacher])

    model.add(Dense(55 * 3 * 3, activation='relu'))
    model.add(Dense(55, activation='softmax'))
    model.summary()
    return model


