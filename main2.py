import keras
from keras.layers import Activation
from keras.layers import Input, Concatenate, Dense
from keras.models import Model, Sequential
import pandas

dataX = pandas.read_csv("medical_insurance_fraud_train.csv")

def anomalyScores(originalDF, reducedDF):
    loss = np.sum((np.array(originalDF) - \
                   np.array(reducedDF))**2, axis=1)
    loss = pd.Series(data=loss,index=originalDF.index)
    loss = (loss-np.min(loss))/(np.max(loss)-np.min(loss))
    
    print('Mean for anomaly scores: ', np.mean(loss))
    
    return loss

# Call neural network API
model = Sequential()# Apply linear activation function to input layer
# Generate hidden layer with 14 nodes, the same as the input layer
model.add(Dense(units=14, activation='linear',input_dim=14))
model.add(Dense(units=14, activation='linear'))# Apply linear activation function to hidden layer
# Generate output layer with 14 nodes
model.add(Dense(units=14, activation='linear'))

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])
# model.fit - to train model
# Train the model
num_epochs = 10
batch_size = 256
history = model.fit(x=dataX, y=dataX,
                    epochs=num_epochs,
                    batch_size=batch_size,
                    shuffle=True,
                    validation_data=(dataX, dataX),
                    verbose=1)