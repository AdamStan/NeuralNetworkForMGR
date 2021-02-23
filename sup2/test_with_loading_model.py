import keras

from sup2.prepare_data import prepare_x_train_data

model = keras.models.load_model("model-the-best-score.h5")
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
