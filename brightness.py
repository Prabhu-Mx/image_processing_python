#!/usr/bin/env python3
import cv2
import numpy as np
import argparse

# Assigning command line args
parser = argparse.ArgumentParser(description='Code for Changing the brightness of an image')
parser.add_argument('--input', help='Path to input image.', default='eli.jpg')
parser.add_argument('--output',help ='Path to output image', default='new_image.jpg')
parser.add_argument('--brightness', help = 'Brightness level', default= '1.1', type =float)
args = parser.parse_args()


# Read the image file
image = cv2.imread(args.input)

height = image.shape[0]
width = image.shape[1]
print(image.shape)

for i in np.arange(height):
    for j in np.arange(width):
        # each array element multiply by brightness level and "np.clip" used to set min & max value of array 
        image[i][j] = np.clip([pixel_value * args.brightness for pixel_value in image [i][j]], 0, 255)
cv2.imwrite(args.output, image)

# to run this script
# goto terminal 
# python3 scriptname.py 'path to input image' 'path to save image' 1.1
# for example $python3 brightness.py --input eli.jpg --output /home/new_image.jpg' --brightness 1.1

