import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM
from keras.models import Model
from model import get_advance_model

import random
from ..utilities.generating_data import create_finite_amount_of_data, create_finite_amount_from_mid

my_model = get_advance_model() 
my_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
# okazuje ze trzeba pomieszac...
# jak?
# print("mixing data")
# from helpers import swap_positions 
# for index in range(len(x_training_data)):
#     new_index = index % 55
#     swap_positions(x_training_data[index], 0, new_index)
#     swap_positions(y_train[index], 0, new_index)
# print("mixing finish")
# model.fit(x_training_data, y_train, epochs=6)

# # easy test - my
# test = [
#     [
#         [3.0, 10.0, 12.0, ],
#         [2.0, 11.0, 13.0, ],
#     ]
# ]
# test = prepare_x_train_data(test)
# out = model.predict(test)
# print("outy")
# print(out)
# print(max(out[0]))
# print(out[0][0])
# print(out[0][1])
# print(max(out[0]) == out[0][1])
# # bigger test
# y_test = []
# for i in range(len(x_test_data)):
#     y_test.append([1])
# y_test = prepare_y_train_data(y_test)
# score = model.evaluate(x_test_data, y_test, verbose=2)
# print(score)
# if (max(out[0]) == out[0][1]):
#     print("model will be saved")
#     model.save("model2.h5")