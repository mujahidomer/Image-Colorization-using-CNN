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

# image = Image.open('/home/satyendra/Enhance/index.jpg')
contrast = ImageEnhance.Contrast(im)
out = contrast.enhance(1.7)
im.show()
