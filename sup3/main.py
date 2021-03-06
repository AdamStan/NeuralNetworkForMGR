import numpy as np
from model import get_advance_model

import random
from generating_data import create_finite_amount_of_data, create_finite_amount_from_mid, \
    create_3input_available_hours
from prepare_data import prepare_x_train_data, prepare_y_train_data
from helpers import swap_positions

my_model = get_advance_model() 
my_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# creating training data
x_full_data1 = create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 2, 3)
x_full_data1 += create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 1, 3)
x_full_data1 = prepare_x_train_data(x_full_data1)
x_training_data = x_full_data1

# creating y-train data
y_train = []
for index in range(len(x_training_data)):
    y_train.append([1])
y_train = prepare_y_train_data(y_train)

# mixing data
for index in range(len(x_training_data)):
    new_index = index % 54
    swap_positions(x_training_data[index], 0, new_index * 3)
    swap_positions(x_training_data[index], 1, new_index * 3 + 1)
    swap_positions(x_training_data[index], 2, new_index * 3 + 2)
    swap_positions(y_train[index], 0, new_index)

# creating x_learn datas
x_learn, x_learn2, x_learn3 = [], [], []
for index in range(len(x_training_data)):
    which_time_will_taken = y_train[index]
    x1_sample, x2_sample, x3_sample = create_3input_available_hours(x_training_data[index], which_time_will_taken)
    x_learn.append(x1_sample)
    x_learn2.append(x2_sample)
    x_learn3.append(x3_sample)

print(np.array(x_learn).shape)
print(np.array(y_train).shape)

x_learn = np.array(x_learn).reshape(len(x_learn), 165)
x_learn2 = np.array(x_learn2).reshape(len(x_learn2), 165)
x_learn3 = np.array(x_learn3).reshape(len(x_learn3), 165)
# y_train = np.array(y_train).reshape(1, len(y_train), 55)


my_model.fit([x_learn, x_learn2, x_learn3], y_train, epochs=6, batch_size=6)
my_model.save("model-first.h5")


# creating test data
# x_test_data = create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 2, 5)
# x_test_data += create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 1, 4)
# x_test_data = prepare_x_train_data(x_test_data)