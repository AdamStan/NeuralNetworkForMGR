from tensorflow.keras.preprocessing.sequence import pad_sequences

def prepare_x_train_data(x_train):
    new_data = []
    for av_hours in x_train:
        for index in range(len(av_hours), 55):
            av_hours.append([0,0,0])
        new_data.append(av_hours)
    return new_data

def prepare_y_train_data(y_train):
    return pad_sequences(sequences=y_train, maxlen=55)