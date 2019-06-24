import cv2
import numpy as np
import sys
import scipy.misc
from scipy import misc
from PIL import Image, ImageEnhance
from scipy.misc.pilutil import Image
from PIL import Image
import sys

#img = Image.open(sys.argv[1])
#name = Image.open(sys.argv[1])
img = cv2.imread('/home/satyendra/Enhance/index.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
print('Your image has been processed by Histogram Equilization')

