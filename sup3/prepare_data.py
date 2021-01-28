
def prepare_x_train_data(x_train):
    new_data = []
    for av_hours in x_train:
        for index in range(len(av_hours), 55):
            av_hours.append([0,0,0])
        new_data.append(av_hours)
    return new_data

def prepare_y_train_data(y_train):
    new_data = []
    for propabilities in y_train:
        for index in range(len(propabilities), 55):
            propabilities.append(0)
        new_data.append(propabilities)
    return new_data