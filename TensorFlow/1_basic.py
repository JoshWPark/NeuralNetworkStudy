import tensorflow as tf

a = tf.constant([1, 2, 3])

print(a)
print(a.numpy())

import numpy as np

b = np.ones(3)

print(b)
print(tf.multiply(b, 3))