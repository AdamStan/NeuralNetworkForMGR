from tensorflow.keras.preprocessing.sequence import pad_sequences


def prepare_x_train_data(x_train):
    return pad_sequences(sequences=x_train, maxlen=55*3)


def prepare_y_train_data(y_train):
    return pad_sequences(sequences=y_train, maxlen=55)
