import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
import numpy as np

from prepare_data import prepare_y_train_data, prepare_x_train_data
from generating_x_data import create_finite_amount_of_data, create_finite_amount_from_mid
from model import get_my_model_n

# y_data to classficator - czyli mamy 55 output dostepnych okienek
# x_data to dane na wejsciu - czyli 55 trojek
# output to prawdopodobienstwo wyboru z y_data, wybrane okienko ma zostac zakwalifikowane do wstawienia
# stworzenie danych ktore sa prawdziwe
# strategia, bierzemy dni najblizej poniedzialku
# czyli y data to są jedynki i 54 zera
x_full_data = create_finite_amount_of_data(8, 19, [1,2,3,4,5], 2, 5)
x_full_data += create_finite_amount_of_data(8, 19, [1,2,3,4,5], 1, 5)
print(len(x_full_data))
# uzupelnienie x daty do pelnych 55 trojek
x_full_data = prepare_x_train_data(x_full_data)


x_training_data = x_full_data
x_test_data = create_finite_amount_from_mid(8,19,[1,2,3,4,5],2, 5)
x_test_data += create_finite_amount_from_mid(8,19,[1,2,3,4,5],1, 5)

x_test_data = prepare_x_train_data(x_test_data)

y_train = []
for index in range(len(x_training_data)):
    y_train.append([1])
y_train = prepare_y_train_data(y_train)

y_test = []
for index in range(len(x_training_data)):
    y_test.append([1])
y_test = prepare_y_train_data(y_test)

model = get_my_model_n()
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
# okazuje ze trzeba pomieszac...
# jak?
print("mixing data")
from helpers import swap_positions 
for index in range(len(x_training_data)):
    new_index = index % 55
    swap_positions(x_training_data[index], 0, new_index)
    swap_positions(y_train[index], 0, new_index)
print("mixing finish")
print("X training data")
print(len(x_training_data))
print("x_test_data")
print(len(x_test_data) / len(x_full_data))
model.fit(x_training_data, y_train, epochs=12, batch_size=12)

# easy test - my
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
print(max(out[0]) == out[0][1])
# bigger test
y_test = []
for i in range(len(x_test_data)):
    y_test.append([1])
y_test = prepare_y_train_data(y_test)
score = model.evaluate(x_test_data, y_test, verbose=2)
print("Score mój")
print(score)
if (max(out[0]) == out[0][1]):
    print("model will be saved")
    model.save("model4.h5")
