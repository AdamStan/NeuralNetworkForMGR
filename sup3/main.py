import numpy as np
from model import get_advance_model

import random
from generating_data import create_finite_amount_of_data, create_finite_amount_from_mid, \
    create_3input_available_hours, get_available_hours
from prepare_data import prepare_x_train_data, prepare_y_train_data
from helpers import swap_positions

my_model = get_advance_model() 
my_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# creating training data
x_full_data1 = create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 2, 4)
x_full_data1 += create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 1, 4)
x_full_data1 = prepare_x_train_data(x_full_data1)
x_training_data = x_full_data1

# creating x_learn data
x_learn, x_learn2, x_learn3 = [], [], []
y_train = []
for index in range(len(x_training_data)):
    x1_sample, x2_sample, x3_sample = create_3input_available_hours(x_training_data[index])
    # creating y_train data
    y_train_sample = []
    for i in range(0, get_available_hours(x1_sample), 3):
        if x1_sample[i] == x2_sample[i] and x1_sample[i] == x3_sample[i] and \
            x1_sample[i + 1] == x2_sample[i + 1] and x1_sample[i + 1] == x3_sample[i + 1] and \
                x1_sample[i + 2] == x2_sample[i + 2] and x1_sample[i + 2] == x3_sample[i + 2]:
                    y_train_sample.append(1)
                    break
        else:
            y_train_sample.append(0)
    y_train.append(y_train_sample)
    x_learn.append(x1_sample)
    x2_sample_r = []
    for i in range(len(x2_sample)):
        if x2_sample[i] != 0:
            x2_sample_r.append(x2_sample[i])
    x_learn2.append(x2_sample_r)
    x3_sample_r = []
    for i in range(len(x3_sample)):
        if x3_sample[i] != 0:
            x3_sample_r.append(x3_sample[i])
    x_learn3.append(x3_sample_r)

print("data are ready!")
print(np.array(x_learn).shape)
y_train = prepare_y_train_data(y_train)
x_learn2 = prepare_x_train_data(x_learn2)
x_learn3 = prepare_x_train_data(x_learn3)
print(np.array(y_train).shape)

x_learn = np.array(x_learn).reshape(len(x_learn), 165)
x_learn2 = np.array(x_learn2).reshape(len(x_learn2), 165)
x_learn3 = np.array(x_learn3).reshape(len(x_learn3), 165)

my_model.fit([x_learn, x_learn2, x_learn3], y_train, epochs=6, batch_size=6)
my_model.save("model-first.h5")


# creating test data
# x_test_data = create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 2, 5)
# x_test_data += create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 1, 4)
# x_test_data = prepare_x_train_data(x_test_data)