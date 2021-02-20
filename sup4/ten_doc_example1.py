from model import get_diff_model
import numpy as np
from prepare_data import prepare_x_train_data, prepare_y_train_data

my_model = get_diff_model()
my_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
x_learn = [
    np.array([
        2.0, 10.0, 12.0, 
        2.0, 12.0, 14.0
    ]),
]
x_learn2 = [
    np.array([
        1.0, 10.0, 12.0,
        2.0, 12.0, 14.0,
    ])
]
x_learn3 = [
    np.array([
        2.0, 10.0, 12.0,
        3.0, 12.0, 14.0,
    ])
]

x_learn = prepare_x_train_data(x_learn)
x_learn2 = prepare_x_train_data(x_learn2)
x_learn3 = prepare_x_train_data(x_learn3)
y_learn = [
    np.array([1])
]


my_model.fit([x_learn, x_learn2, x_learn3], prepare_y_train_data(y_learn), epochs=6)
