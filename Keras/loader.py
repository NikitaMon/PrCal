import tensorflow as tf
import keras

import matplotlib.pyplot as plt

def datasetload():
    # загрузка датасета
    tf.keras.datasets.mnist.load_data(path="mnist.npz")
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    y_train = tf.keras.utils.to_categorical(y_train)
    plt.imshow( x_train[0] )
    

