from prepare_data import prepare_y_train_data, prepare_x_train_data
from generating_x_data import create_finite_amount_of_data, create_finite_amount_from_mid, get_available_hours
from model import get_my_model_n
from helpers import swap_positions

# creating training data
x_full_data = create_finite_amount_of_data(8, 19, [1, 2,3,4,5], 2, 6)
x_full_data += create_finite_amount_of_data(8, 19, [1,2,3,4,5], 1, 4)
x_full_data = prepare_x_train_data(x_full_data)
x_training_data = x_full_data

# creating y-train data
y_train = []
for index in range(len(x_training_data)):
    y_train.append([1])
y_train = prepare_y_train_data(y_train)

# mixing data
for index in range(len(x_training_data)):
    new_index = index % get_available_hours(x_training_data[index])
    print(get_available_hours(x_training_data[index]))
    swap_positions(x_training_data[index], 0, new_index)
    swap_positions(y_train[index], 0, new_index)
print("mixing finish")
print("X training data")
print(len(x_training_data))

model = get_my_model_n()
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
history = model.fit(x_training_data, y_train, epochs=6, batch_size=32)

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
if max(out[0]) == out[0][1]:
    print("model will be saved")
    model.save("model6.h5")
