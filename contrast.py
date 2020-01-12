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

# each array element multiply by contrast ratio  and "np.clip" used to set min & max value of the image array
image = np.clip([pixel_value * args.contrast for pixel_value in image + beta],0, 255)

#Write image in given path
cv2.imwrite(args.output, image)