from prepare_data import prepare_y_train_data, prepare_x_train_data
from generating_x_data import create_finite_amount_of_data, create_finite_amount_from_mid
from model import get_my_model_n, get_my_model_with_parameters
from helpers import swap_positions

# creating training data
x_full_data = create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 2, 6)
x_full_data += create_finite_amount_of_data(8, 19, [1, 2, 3, 4, 5], 1, 4)
x_full_data = prepare_x_train_data(x_full_data)
x_training_data = x_full_data

# creating test data
x_test_data = create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 2, 5)
x_test_data += create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 1, 4)
x_test_data = prepare_x_train_data(x_test_data)

# creating y-train data
y_train = []
for index in range(len(x_training_data)):
    y_train.append([1])
y_train = prepare_y_train_data(y_train)
# creating y-test data
y_test = []
for index in range(len(x_training_data)):
    y_test.append([1])
y_test = prepare_y_train_data(y_test)

# mixing data
for index in range(len(x_training_data)):
    new_index = index % 55
    swap_positions(x_training_data[index], 0, new_index)
    swap_positions(y_train[index], 0, new_index)
print("mixing finish")
print("X training data")
print(len(x_training_data))

best_score = 0
best_model = None
table_with_results = []
for hidden in range(2,6):
    for vertical_exp in range(1,4):
        model = get_my_model_with_parameters(hidden, vertical_exp)
        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
        history = model.fit(x_training_data, y_train, epochs=6, batch_size=32)

        # test using prepared data
        y_test = []
        for i in range(len(x_test_data)):
            y_test.append([1])
        y_test = prepare_y_train_data(y_test)
        score = model.evaluate(x_test_data, y_test, verbose=2)
        print("Score my")
        print(score)
        if best_score < score[1]:
            best_model = model
            best_score = score[1]
        table_with_results.append([hidden, vertical_exp, score, history])
# write the best model
if best_model:
    print("model will be saved")
    print(best_score)
    best_model.save("model-the-best.h5")
print(table_with_results)
