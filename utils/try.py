import tensorflow as tf
import numpy as np
import sys
def _variable_on_cpu(name, shape, initializer):
   with tf.device('/cpu:0'):

      var = tf.get_variable(name, shape, initializer=initializer)
   return var
var = _variable_on_cpu("nm", [3,6,4,2],
                         tf.truncated_normal_initializer(stddev=0.1))
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
inp= var.get_shape()[3]
print(inp)
print(sess.run(var))
