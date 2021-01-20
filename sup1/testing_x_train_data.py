import numpy as np

x_train = np.array([
    [
        [1.0/7, 12.0/24, 14.0/24, ],
        [1.0/7, 14.0/24, 16.0/24, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
    ],
    [
        [2.0/7, 12.0/24, 14.0/24, ],
        [1.0/7, 14.0/24, 16.0/24, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
    ],
    [
        [2.0/7, 12.0/24, 14.0/24, ],
        [3.0/7, 14.0/24, 16.0/24, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
    ],
    [
        [2.0/7, 12.0/24, 14.0/24, ],
        [4.0/7, 8.0/24, 11.0/24, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ],
    ],
])
y_train = np.array([
    [2.0/7, 8.0/24, ],
    [2.0/7, 14.0/24 ],
    [2.0/7, 14.0/24 ],
    [4.0/7, 11.0/24 ],
])
# print(x_train.shape)
# print(y_train.shape)