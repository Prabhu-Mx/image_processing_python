#!/usr/bin/env python3
import cv2
import numpy as np
import argparse

# Assigning command line args
parser = argparse.ArgumentParser(description="Image contrast adjustment")
parser.add_argument('--input',help='Enter path of input image')
parser.add_argument('--output',help='Enter path of output image')
parser.add_argument('--contrast', help='Enter desired contrast ratio', type= float)
args = parser.parse_args()
beta = 0 # brightness
# Read the image file
image = cv2.imread(args.input)

height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]


for x in np.arange(height):
    for y in np.arange(width):
        for z in np.arange(depth):
              #print( x, y, z)
              image [x, y, z] = [pixel_value * (args.contrast) for pixel_value in image([x][y][z])]

#cv2.imwrite(args.output, image)