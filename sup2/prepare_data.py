
def prepare_x_train_data(x_train):
    new_data = []
    for av_hours in x_train:
        for _ in range(len(av_hours), 55):
            av_hours.append([0,0,0])
        new_data.append(av_hours)
    return new_data

def prepare_y_train_data(y_train):
    new_data = []
    for probabilities in y_train:
        for _ in range(len(probabilities), 55):
            probabilities.append(0)
        new_data.append(probabilities)
    return new_data
