import keras
from keras.layers import Dense
from keras.layers import Input, concatenate
from keras.models import Model, Sequential


def get_advance_model():
    input_plan = Input(shape=165)
    input_room = Input(shape=165)
    input_teacher = Input(shape=165)

    branch_plan = Sequential() 
    branch_plan.add(input_plan)
    branch_plan.add(Dense(55 * 3 * 2, activation='relu'))
    branch_plan.add(Dense(55 * 3 * 2, activation='relu'))
    branch_plan.add(Dense(55, activation="softmax"))
    
    branch_room = Sequential()
    branch_room.add(input_room)
    branch_room.add(Dense(55 * 3 * 2, activation='relu'))
    branch_room.add(Dense(55 * 3 * 2, activation='relu'))
    branch_room.add(Dense(55, activation="softmax"))

    branch_teacher = Sequential()
    branch_teacher.add(input_teacher)
    branch_teacher.add(Dense(55 * 3 * 2, activation='relu'))
    branch_teacher.add(Dense(55 * 3 * 2, activation='relu'))
    branch_teacher.add(Dense(55, activation="softmax"))
    
    combined_first = concatenate([branch_plan.output, branch_teacher.output,])
    combined_second = concatenate([combined_first, branch_room.output])
    layer_after_concat = Dense(165, activation="relu")(combined_second)
    output = Dense(55, activation='softmax')(layer_after_concat)

    model = Model(inputs=[input_plan, input_teacher, input_room], outputs=output)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    model.summary()
    keras.utils.plot_model(model, to_file="model3.png", show_shapes=True)
    return model
