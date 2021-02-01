import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Concatenate, Activation, LSTM, Dropout
from keras.models import Model, Sequential


def get_model():
    model_lstm = Sequential()
    # input should be in one dimmension for lstm
    # units is for output space
    model_lstm.add(LSTM(units=55, return_sequences=True, input_shape=(55,3)))
    # to avoid over train our network we have to turn off 20% our neurons 
    model_lstm.add(Dropout(0.2))
    
    model_lstm.add(LSTM(units=55, return_sequences=True))
    model_lstm.add(Dropout(0.2))
    
    model_lstm.add(LSTM(units=55))
    model_lstm.add(Dropout(0.2))

    model_lstm.add(Dense(units=55))

    model_lstm.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy']) # binary_crossentropy or mean_squared_error?
    model_lstm.summary()
