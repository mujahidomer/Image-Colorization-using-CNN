import os
import tensorflow as tf
import cv2
import sys
import numpy as np
import fnmatch
sys.path.append('/home/Imagecolor/')
sys.path.insert(0, '../architecture/')
sys.path.insert(0, '../model/')
from architecture import architecture

def eval(checkpoint_dir, image):
   with tf.Graph().as_default() as graph:
      input_image = tf.placeholder(tf.float32, shape=(1,144,160,3))
      logit = architecture.inference(input_image, 'test')
      variables = tf.all_variables()
      init      = tf.initialize_all_variables()
      sess      = tf.Session()
      saver     = tf.train.Saver(variables)
      #print 'jj'
      print((input_image))
      #print 'kk'
      tf.train.start_queue_runners(sess=sess)

      ckpt = tf.train.get_checkpoint_state(checkpoint_dir)

      if ckpt and ckpt.model_checkpoint_path:
         print 'Trying to Restoring model...'
         try:
            saver.restore(sess, ckpt.model_checkpoint_path)
         except:
            print 'Could not restore model'
            raise
            exit()

      graph_def = sess.graph.as_graph_def(add_shapes=True)
      
      img = cv2.imread(image)
      print img.shape
      print len(img.shape)
      if  len(img.shape) != 3:  #just for fun :p
         img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
         img = np.expand_dims(img, axis=2)

      if img.shape[0] != 160:
         img = cv2.resize(img, (160,144))

      img = img.astype('float')
      print img
      #print 'cc'   
      fake = np.zeros((1,144,160,3))
      #print fake
      fake[0,:,:,:] = img
      print fake
      gen_img = sess.run([logit], feed_dict={input_image:fake})[0]
      #gen_img = gen_img*255
      #print (sess.run(input_image))
      image_name = image.split('.png')[0]+'.png'
      image_name = image_name.split('/')[-1]
      try:
         print 'Writing image ', image_name
         cv2.imwrite('./static/processed_images/' + image_name, gen_img[0,:,:,:])
      except:
         raise

def main(argv=None):
   eval(sys.argv[1], sys.argv[2])

def land():
   print architecture.inference

if __name__ == "__main__":
   if len(sys.argv) < 2:
      print "Usage: python eval.py /path/to/model/ images.png"  
      exit()
   tf.app.run()   
