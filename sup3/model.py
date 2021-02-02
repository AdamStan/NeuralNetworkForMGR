import keras
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape
from keras.layers import Input, Activation, concatenate
from keras.models import Model, Sequential


def get_advance_model():
    input_plan = Input(shape=(165))
    input_room = Input(shape=(165))
    input_teacher = Input(shape=(165))

    branch_plan = Sequential() 
    branch_plan.add(input_plan)
    branch_plan.add(Dense(55 * 3 * 2, activation='relu'))
    branch_plan.add(Dense(55, activation="softmax"))
    
    branch_room = Sequential()
    branch_room.add(input_room)
    branch_room.add(Dense(55 * 3 * 2, activation='relu'))
    branch_room.add(Dense(55, activation="softmax"))

    branch_teacher = Sequential()
    branch_teacher.add(input_teacher)
    branch_teacher.add(Dense(55 * 3 * 2, activation='relu'))
    branch_teacher.add(Dense(55, activation="softmax"))
    
    combinded_first = concatenate([branch_plan.output, branch_teacher.output,])
    combinded_second = concatenate([combinded_first, branch_room.output])
    output = Dense(55, activation='softmax')(combinded_second)

    model = Model(inputs=[input_plan, input_teacher, input_room], outputs = output)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    model.summary()
    return model


def get_model():
    first = Sequential()
    first.add(Dense(1, input_shape=(2,), activation='sigmoid'))
    second = Sequential()
    second.add(Dense(1, input_shape=(1,), activation='sigmoid'))
    third = Sequential()
    # of course you must provide the input to result which will be your x3
    third.add(Dense(1, input_shape=(1,), activation='sigmoid'))
    # lets say you add a few more layers to first and second.
    # concatenate them
    merged = Concatenate([first, second])
    # then concatenate the two outputs
    result = Concatenate([merged,  third])
    ada_grad = Adagrad(lr=0.1, epsilon=1e-08, decay=0.0)
    result.compile(optimizer=ada_grad, loss='binary_crossentropy',
                metrics=['accuracy'])
