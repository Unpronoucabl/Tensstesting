# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:14:15 2018

@author: CrystalGlacier
"""

import tensorflow as tf

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

result = tf.multiply(x1,x2)
sess = tf.Session()
print(sess.run(result))
sess.close()

"""
with tf.Session as sess:
    output = sess.run(result)
    print(output)
"""