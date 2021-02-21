import keras
from keras import layers
from keras.layers import Input, Concatenate, Activation, LSTM, Dropout, Dense
from keras.models import Model, Sequential


def get_model():
    sequence_length = 55*3
    dictionary_size = 24 # from 0 to 23
    input_plan = layers.Input(shape=(sequence_length,), name="plan_av_hours")
    input_room = layers.Input(shape=(sequence_length,), name="room_av_hours")
    input_teacher = layers.Input(shape=(sequence_length,), name="teacher_av_hours")

    plan_embedded = layers.Embedding(input_dim=dictionary_size, output_dim=64,)(
        input_plan
    )
    output, state_h, state_c = LSTM(64, return_state=True, name="plan_hours")(
        plan_embedded
    )
    plan_state = [state_h, state_c]
    # print(plan_state)

    # Pass the 2 states to a new LSTM layer, as initial state
    # print(input_teacher)
    teacher_embedded = layers.Embedding(input_dim=dictionary_size, output_dim=64)(
        input_teacher
    )
    teacher_output = LSTM(64, name="teacher_hours")(
        teacher_embedded, initial_state=plan_state
    )

    room_embedded = layers.Embedding(input_dim=dictionary_size, output_dim=64)(
        input_room
    )
    room_output = LSTM(64, name="room_hours")(
        room_embedded, initial_state=plan_state
    )

    combined_room_and_teachers = layers.concatenate([teacher_output, room_output])
    output = Dense(55, activation='softmax')(combined_room_and_teachers)

    real_output = Dense(55)(output)

    model_lstm = Model([input_plan, input_teacher, input_room], real_output)

    model_lstm.compile(optimizer='adam', loss='mean_squared_error',
                       metrics=['accuracy'])  # binary_crossentropy or mean_squared_error?
    model_lstm.summary()
    keras.utils.plot_model(model_lstm, to_file="model4.png", show_shapes=True)
    return model_lstm
