
import sys
import fnmatch
import os
from tqdm import tqdm

if __name__ == '__main__':

   data_dir = sys.argv[1]
   pattern = "*.png"
   image_list = list()
   for d, s, fList in os.walk(data_dir):
      for filename in fList:
         if fnmatch.fnmatch(filename, pattern):
            image_list.append(os.path.join(d,filename))

   print 'Working on images...'
   for image in tqdm(image_list):
      image_dir = os.path.dirname(image)
      resized_image = image_dir+'/'+image.split('/')[-1].split('.')[0]+'_resized.png'
      resized_gray_image = image_dir+'/'+image.split('/')[-1].split('.')[0]+'_resized_gray.png'
     
      # the 'true' image to be used in tensorflow (label)
      os.system('convert "' + image + '" -resize 160x144\! "' + resized_image +'"')

      # the gray image that we are training on
      os.system('convert "' + image + '" -resize 160x144\! -colorspace Gray "' + resized_gray_image +'"')

