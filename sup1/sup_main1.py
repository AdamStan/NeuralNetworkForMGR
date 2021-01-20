import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np


def get_my_model_n():

    model = keras.models.Sequential()

    model.add(Flatten(input_shape=(6,3)))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    model.summary()
    return model
 

# get_model()
model = get_my_model_n()
# keras.utils.plot_model(model, to_file="model.png", show_shapes=True)
# model.compile - is needed before fitting
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
# model.fit - to train model
# x_train = [(1, 10, 12)]
from testing_x_train_data import x_train, y_train
print(x_train.shape)

model.fit(x_train, y_train, epochs=32)

test = np.array([
    [
        [2.0/7, 12.0/24, 14.0/24, ],
        [3.0/7, 11.0/24, 14.0/24, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
    ],
])
print(test.shape)

out = model.predict(test)
print(out)
print(out[0][0] * 7)
print(out[0][1] * 24)