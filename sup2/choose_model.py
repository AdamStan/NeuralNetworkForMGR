from prepare_data import prepare_y_train_data, prepare_x_train_data
from generating_x_data import create_finite_amount_of_data, create_finite_amount_from_mid, get_available_hours
from model import get_my_model_with_parameters
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

# creating test data
print("Test data from...")
x_test_data = create_finite_amount_from_mid(8, 19, [1, 2, 3, 4, 5], 2, 6)
x_test_data = prepare_x_train_data(x_test_data)
y_test = []
for i in range(len(x_test_data)):
    y_test.append([1])
y_test = prepare_y_train_data(y_test)

# mixing data
for index in range(len(x_training_data)):
    new_index = index % get_available_hours(x_training_data[index])
    swap_positions(x_training_data[index], 0, new_index)
    swap_positions(y_train[index], 0, new_index)
print("mixing finish")
print("X training data")
print(len(x_training_data))

best_score = 0
best_model = None
best_score_and_accuracy = 0
best_model_score = None
best_accuracy = 0
best_model_accuracy = None
table_with_results = []
for hidden in range(2,6):
    for vertical_exp in range(1,4):
        model = get_my_model_with_parameters(hidden, vertical_exp)
        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
        history = model.fit(x_training_data, y_train, epochs=6, batch_size=6)

        score = model.evaluate(x_test_data, y_test, verbose=2)
        print("Score my")
        print(score)
        accuracy = history.history['accuracy'][-1]
        print(accuracy)
        if best_score < score[1]:
            best_model_score = model
            best_score = score[1]
        if best_accuracy < accuracy:
            best_model_accuracy = model
            best_accuracy = accuracy
        if best_score_and_accuracy < score[1] * accuracy:
            best_model = model
            best_score_and_accuracy = score[1] * accuracy
        table_with_results.append([hidden, vertical_exp, score, history.history])
# write the best model
if best_model:
    print("model will be saved")
    print(best_score)
    best_model.save("model-the-best.h5")
if best_score:
    print("best score model will be saved")
    best_model_score.save("model-the-best-score.h5")
if best_model_accuracy:
    print("best accuracy model will be saved")
    best_model_accuracy.save("model-the-best-accuracy.h5")
print(table_with_results)
