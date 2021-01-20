import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np


def get_model(item_count=5):
    input_weights = Input((item_count,))
    input_prices = Input((item_count,))
    inputs_concat = Concatenate()([input_weights, input_prices])
    picks = Dense(35, activation="sigmoid")(inputs_concat)
    picks = Dense(item_count, activation="sigmoid")(picks)
    model = Model(inputs=[input_weights, input_prices], outputs=[picks])
    model.summary()
    return model


def get_my_model(item_count=3):
    """
    N inputs with: (day, start, end)
    N = 7 days x 5 scheduled_sujects = 35 - more then throw exception 
    """
    # list with 0/1 - 0 when not availble
    input_available_days = Input((7))
    # list with 0/1 - 0 when not availble
    input_available_hours = Input((24))
    inputs = []
    for i in range(0, 2):
        inputs.append(Input((item_count)))
    inputs_concat = Concatenate()(inputs)
    picks = Dense(35, activation="sigmoid")(inputs_concat)
    model = Model(inputs=inputs, outputs=[picks])
    model.summary()
    return model

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