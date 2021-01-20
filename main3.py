from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces(shuffle=True, random_state=1000)
X_train = faces['images']

import tensorflow.compat.v1 as tf

nb_epochs = 800
batch_size = 100
code_length = 512
width = 32
height = 32
graph = tf.Graph()

with graph.as_default():
    input_images_xl = tf.placeholder(tf.float32,
                                     shape=(batch_size, X_train.shape[1],
                                            X_train.shape[2], 1))
    input_images = tf.image.resize_images(input_images_xl, (width, height),
                                          method=tf.image.ResizeMethod.BICUBIC)
    # Encoder
    conv_0 = tf.layers.conv2d(inputs=input_images,
                              filters=16,
                              kernel_size=(3, 3),
                              strides=(2, 2),
                              activation=tf.nn.relu,
                              padding='same')
    conv_1 = tf.layers.conv2d(inputs=conv_0,
                              filters=32,
                              kernel_size=(3, 3),
                              activation=tf.nn.relu,
                              padding='same')
    conv_2 = tf.layers.conv2d(inputs=conv_1,
                              filters=64,
                              kernel_size=(3, 3),
                              activation=tf.nn.relu,
                              padding='same')
    conv_3 = tf.layers.conv2d(inputs=conv_2,
                              filters=128,
                              kernel_size=(3, 3),
                              activation=tf.nn.relu,
                              padding='same')
