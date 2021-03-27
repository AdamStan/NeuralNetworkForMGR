import numpy as np
from model import get_advance_model

from generating_data import create_finite_amount_of_data, create_input_available_hours_for_teacher_and_room
from prepare_data import prepare_x_train_data, prepare_y_train_data

my_model = get_advance_model()
my_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

print("Creating x full data")
x_full_data = create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 2, 6)
x_full_data += create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 1, 4)
x_full_data = prepare_x_train_data(x_full_data)
x_training_data = x_full_data

# creating x_learn data
x_learn2, x_learn3 = [], []
y_train = []
print("Creating x data for other inputs and y-train list")
for index in range(len(x_training_data)):
    x2_sample, x3_sample = create_input_available_hours_for_teacher_and_room(x_training_data[index])
    # creating y_train data
    # y_train_sample = []
    # for i in range(0, len(x_training_data[index]), 3):
    #     if x_training_data[index][i] == x2_sample[i] and x_training_data[index][i] == x3_sample[i] and \
    #             x_training_data[index][i + 1] == x2_sample[i + 1] and x_training_data[index][i + 1] == x3_sample[i + 1] and \
    #             x_training_data[index][i + 2] == x2_sample[i + 2] and x_training_data[index][i + 2] == x3_sample[i + 2]:
    #         y_train_sample.append(1)
    #         break
    #     else:
    #         y_train_sample.append(0)
    y_train.append([1])
    x_learn2.append(x2_sample)
    x_learn3.append(x3_sample)

print("data are ready!")
not_valid = 0
for index in range(len(y_train)):
    ok = False
    for y_v in y_train[index]:
        if y_v == 1:
            ok = True
            break
    if not ok:
        print("Not valid sample:")
        print(y_train[index])
        print(index)
        not_valid += 1
print(not_valid)
y_train = prepare_y_train_data(y_train)
x_learn2 = prepare_x_train_data(x_learn2)
x_learn3 = prepare_x_train_data(x_learn3)
print(np.array(y_train).shape)

x_learn = np.array(x_full_data).reshape(len(x_full_data), 165)
x_learn2 = np.array(x_learn2).reshape(len(x_learn2), 165)
x_learn3 = np.array(x_learn3).reshape(len(x_learn3), 165)

my_model.fit([x_learn, x_learn2, x_learn3], y_train, epochs=6, batch_size=32)
my_model.save("model-first.h5")

# creating test data
# x_test_data = create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 2, 5)
# x_test_data += create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 1, 4)
# x_test_data = prepare_x_train_data(x_test_data)
