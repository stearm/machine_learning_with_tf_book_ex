from math import pi
import tensorflow as tf

x = 1.0
mean = 1.0
sigma = 1.0

# gaussian distribution

(1.0 / tf.sqrt(2.0 * pi * tf.square(sigma))) \
    * (tf.exp(tf.negative(tf.square(x - mean))) / (2.0 * tf.square(sigma)))
