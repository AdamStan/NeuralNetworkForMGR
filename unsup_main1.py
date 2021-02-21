import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np


def get_model():
    model = Sequential()# Apply linear activation function to input layer
    model.add(Dense(units=55, activation='linear',input_dim=55))
    model.add(Dense(units=55, activation='linear'))# Apply linear activation function to hidden layer
    model.add(Dense(units=55, activation='linear'))# Compile the model
    model.compile(optimizer='adam',
                loss='mean_squared_error',
                metrics=['accuracy'])
    model.summary()
    return model
    

# get_model()
model = get_my_model_n()
# keras.utils.plot_model(model, to_file="model3.png", show_shapes=True)
# model.compile - is needed before fitting
# model.fit - to train model
# x_train = [(1, 10, 12)]
from testing_x_train_data import x_train, y_train
print(x_train.shape)

# y_train = [(1, 12, 14)]
# by https://towardsdatascience.com/unsupervised-machine-learning-example-in-keras-8c8bf9e63ee0
# x = y
# model.fit(x_train, y_train, epochs=32)
model.fit(x=x_train, y=x_train,
                    epochs=32,
                    shuffle=True,
                    validation_data=(x_train, x_train),
                    verbose=1)

test = np.array([
    [
        [2.0/7, 12.0/24, 14.0/24, ],
        [3.0/7, 8.0/24, 11.0/24, ],
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