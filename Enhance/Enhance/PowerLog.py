import cv2
import numpy as np
import sys
import scipy.misc
from scipy import misc
from PIL import Image, ImageEnhance
from scipy.misc.pilutil import Image
from PIL import Image
import sys
#im = Image.open(sys.argv[1])
print('4.Your image has been processed by Power Log Transform')
im = cv2.imread('/home/satyendra/Enhance/image_1244_resized_gray.png')
im = im/255.0
im_power_law_transformation = cv2.pow(im,0.6)
cv2.imshow('Original Image',im)
cv2.imshow('Power Law Transformation',im_power_law_transformation)
k = cv2.waitKey(0) 
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
