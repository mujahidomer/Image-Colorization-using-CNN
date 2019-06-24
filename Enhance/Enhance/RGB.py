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
rgb_im = im.convert('RGB')
width, height = im.size
for w in range(width):
    for h in range(height):
        print rgb_im.getpixel((w,h))
print('RGB values shown above')
