import numpy as np
import matplotlib as posibilities
import pandas as pd

dataset_train = pd.read_csv("stocks.csv")
training_set = dataset_train.iloc[:, 1:2].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range= (0,1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
Y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i,0])
    Y_train.append(training_set_scaled[i, 0])

X_train, Y_train = np.array(X_train), np.array(Y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

regression = Sequential()
print((X_train.shape[1], 1))
regression.add(LSTM(units=50, return_sequences=True, input_shape= (X_train.shape[1], 1)))
regression.add(Dropout(0.2))

regression.add(LSTM(units=50, return_sequences=True))
regression.add(Dropout(0.2))

regression.add(LSTM(units=50, return_sequences=True))
regression.add(Dropout(0.2))

regression.add(Dense(1))

regression.compile(optimizer='adam', loss='mean_squared_error')
regression.summary()

print(X_train.shape)
print(X_train.shape[1])
print(Y_train.shape)

regression.fit(X_train, Y_train, epochs=10, batch_size=1)
