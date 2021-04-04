import keras
from keras.layers import Dense, Flatten


def get_my_model_n():
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55, 3), name="available_hours"))
    model.add(Dense(165, activation='relu'))
    model.add(Dense(165, activation='relu'))
    model.add(Dense(55, activation='softmax', name="output"))
    model.summary()
    return model


def get_my_model_with_parameters(hidden_layers_amount, ver):
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55, 3), name="available_hours"))
    for _ in range(hidden_layers_amount):
        model.add(Dense(165*ver, activation='relu'))
    model.add(Dense(55, activation='softmax', name="output"))
    model.summary()
    return model
