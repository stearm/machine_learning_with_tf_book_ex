import tensorflow as tf

m1 = tf.constant([[1., 2.]])
m2 = tf.constant([[1], [2]])
m3 = tf.constant([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])

print(m1)
print(m2)
print(m3)