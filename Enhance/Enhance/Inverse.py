import cv2
import numpy as np
import sys
import scipy.misc
from scipy import misc
from PIL import Image, ImageEnhance
from scipy.misc.pilutil import Image
from PIL import Image
import sys
im = Image.open(sys.argv[1])
#im = Image.open('/home/satyendra/Enhance/index.jpg')
im_array = scipy.misc.fromimage(im)
im_inverse = 255 - im_array
im_result = scipy.misc.toimage(im_inverse)
misc.imsave('result.jpg',im_result)
print('Your image has been processed by Inverse Method')
