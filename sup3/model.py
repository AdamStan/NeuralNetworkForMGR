from keras.layers import Dense
from keras.layers import Input, concatenate
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
