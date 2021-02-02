import random
from generating_x_data import create_finite_amount_of_data, create_finite_amount_from_mid

def prepare_x_train_data(x_train):
    new_data = []
    for av_hours in x_train:
        for index in range(len(av_hours), 55):
            av_hours.append([0,0,0])
        new_data.append(av_hours)
    return new_data

def prepare_y_train_data(y_train):
    new_data = []
    for propabilities in y_train:
        for index in range(len(propabilities), 55):
            propabilities.append(0)
        new_data.append(propabilities)
    return new_data

# prepare generating true data
# stworzenie danych ktore sa prawdziwe
# strategia, bierzemy dni najblizej poniedzialku
# czyli y data to są jedynki i 54 zera
x_full_data = create_finite_amount_of_data(8,19,[1,2,3,4,5],2, 6)
x_full_data += create_finite_amount_of_data(8,19,[1,2,3,4,5],1, 4)
print(len(x_full_data))
# uzupelnienie x daty do pelnych 55 trojek
for x_data in x_full_data:
    for i in range(len(x_data), 55):
        x_data.append([0,0,0])

# dividing x_full_data on training data and test data
# 80% to training and 20% to test
x_training_data = x_full_data
x_test_data = create_finite_amount_from_mid(8,19,[1,2,3,4,5],2, 5)
x_test_data += create_finite_amount_from_mid(8,19,[1,2,3,4,5],1, 4)

for x_data in x_test_data:
    for i in range(len(x_data), 55):
        x_data.append([0,0,0])


# for data in x_full_data:
#     if random.random() > 0.2:
#         x_training_data.append(data)
#     else:
#         x_test_data.append(data)

# print(len(x_training_data) / len(x_full_data))
print("x_test_data")
print(len(x_test_data) / len(x_full_data))

y_train = []
for index in range(len(x_training_data)):
    y_train.append([1])
for propabilities in y_train:
    for index in range(len(propabilities), 55):
        propabilities.append(0)

y_test = []
for index in range(len(x_training_data)):
    y_test.append([1])
for propabilities in y_test:
    for index in range(len(propabilities), 55):
        propabilities.append(0)


import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model

from model import get_my_model_n
 

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
model.fit(x_training_data, y_train, epochs=6)

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
print(score)
if (max(out[0]) == out[0][1]):
    print("model will be saved")
    model.save("model3.h5")