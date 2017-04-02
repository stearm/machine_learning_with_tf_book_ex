import tensorflow as tf

sess = tf.InteractiveSession()

spikes = tf.Variable([False] * 8, name="spikes")
saver = tf.train.Saver()
saver.restore(sess, "./spikes.ckpt")
print(spikes.eval())

sess.close()
