import keras
from keras import layers
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape, Input
from keras.layers import Input, Concatenate, Activation, LSTM, Dropout
from keras.models import Model, Sequential


def get_model():
    sequence_length = 55 * 3
    input_plan = Input(shape=(sequence_length))
    input_room = Input(shape=(sequence_length))
    input_teacher = Input(shape=(sequence_length))
    # input should be in one dimmension for lstm
    # units is for output space
    # model_lstm.add(LSTM(units=55, return_sequences=True, input_shape=(55,3)))
    # to avoid over train our network we have to turn off 20% our neurons 
    # model_lstm.add(Dropout(0.2))
    
    # model_lstm.add(LSTM(units=55, return_sequences=True))
    # model_lstm.add(LSTM(units=55, return_sequences=True))

    # model_lstm.add(Dense(units=55, activation='softmax'))

    # Return states in addition to output
    output, state_h, state_c = LSTM(8, return_state=True, name="plan_hours")(
        input_plan
    )
    plan_state = [state_h, state_c]
    print(plan_state)

    # Pass the 2 states to a new LSTM layer, as initial state
    print(input_teacher)
    teacher_output, state_h, state_c = LSTM(8, name="teacher_hours")(
        input_teacher, initial_state=plan_state
    )
    teacher_state = [state_h, state_c]

    room_output = LSTM(8, name="room_hours")(
        input_room.inputs, initial_state=teacher_state
    )

    output = Dense(55)(room_output)


    model_lstm  = Model([input_plan, input_room], output)

    model_lstm.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy']) # binary_crossentropy or mean_squared_error?
    model_lstm.summary()
    return model_lstm

def get_diff_model():
    encoder_vocab = 1000
    decoder_vocab = 2000

    encoder_input = layers.Input(shape=(None,))
    encoder_embedded = layers.Embedding(input_dim=encoder_vocab, output_dim=64)(
        encoder_input
    )

    # Return states in addition to output
    output, state_h, state_c = layers.LSTM(64, return_state=True, name="encoder")(
        encoder_embedded
    )
    encoder_state = [state_h, state_c]
    print(encoder_state)

    decoder_input = layers.Input(shape=(None,))
    decoder_embedded = layers.Embedding(input_dim=decoder_vocab, output_dim=64)(
        decoder_input
    )
    print(decoder_embedded)
    # Pass the 2 states to a new LSTM layer, as initial state
    decoder_output = layers.LSTM(64, name="decoder")(
        decoder_embedded, initial_state=encoder_state
    )
    output = layers.Dense(10)(decoder_output)

    model = keras.Model([encoder_input, decoder_input], output)
    model.summary()
    return model
