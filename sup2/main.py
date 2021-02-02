import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np
from prepare_data import x_train_ready, y_train_ready, prepare_x_train_data


def get_my_model_n():
    model = keras.models.Sequential()
    model.add(Flatten(input_shape=(55,3)))
    model.add(Dense(55, activation='relu'))
    model.add(Dense(55, activation='relu'))
    model.add(Dense(55, activation='softmax'))
    model.summary()
    return model
 

model = get_my_model_n()
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
model.fit(x_train_ready, y_train_ready, epochs=32)

test = [
    [
        [3.0, 10.0, 12.0, ],
        [2.0, 11.0, 13.0, ],
    ]
]
test = prepare_x_train_data(test)
out = model.predict(test)
print("outy")
print(out)
print(max(out[0]))
print(out[0][0])
print(out[0][1])

# y_data to classficator - czyli mamy 55 output dostepnych okienek
# x_data to dane na wejsciu - czyli 55 trojek
# output to prawdopodobienstwo wyboru z y_data, wybrane okienko ma zostac zakwalifikowane do wstawienia
