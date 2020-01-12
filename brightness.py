#!/usr/bin/env python3
import cv2
import numpy as np
import sys

# Assigning command line argv
input_image = str(sys.argv[1])
output_image = str(sys.argv[2])
brightness = float(sys.argv[3])

# Read the image file
image = cv2.imread(input_image)

height = image.shape[0]
width = image.shape[1]

for i in np.arange(height):
    for j in np.arange(width):
        # each array element multiply by brightness level and "np.clip" used to set min & max value of array 
        image[i][j] = np.clip([pixel_value * brightness for pixel_value in image [i][j]], 0, 255)
cv2.imwrite(output_image, image)

# to run this script
# goto terminal 
# python3 scriptname.py 'path to input image' 'path to save image' 1.1
# above 1.1 is the brightness level we would like to increase
