#!/bin/env python

import argparse
import csv
from os import listdir

from keras.models import load_model
import imageio
from skimage import color
from scipy import misc
import numpy as np

"""
    Howto:

    ./classification_check.py -h
"""

# Setting up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("model", 
        help="path to .h5 file")
parser.add_argument("dir", 
        help="input directory")
parser.add_argument("flag", 
        help="[h1|n1|c1|etc] specifies the directory type")
parser.add_argument("csv", 
        help="path of output csv file")

# utility function
def pathPad(path):
    if path[-1] == '/':
        return path
    else:
        return path + '/'

# image loading and preparation
def imageFormat(path, size=(200,200)):
    im = imageio.imread(path)

    if len(im.shape) == 3:
        im = color.rgb2gray(im)

    im = misc.imresize(im, size)
    im = np.expand_dims(im, axis=0)
    im = np.expand_dims(im, axis=3)
    return im

# threshold factory
def threshold(x):

    def temp(i):
        if i >= x:
            return 1
        else:
            return 0
    return temp
     
if __name__ == "__main__":
    args = parser.parse_args()
    model = load_model(args.model)
    path = pathPad(args.dir)
    flag = args.flag
    csvout = args.csv

    thres50 = threshold(.50)

    with open(csvout, 'w', newline='') as f:
        writer = csv.writer(f)
        images = listdir(path)

        for image in images:
            line = [] # contents of the csv file
            line.append(image)

            im = imageFormat(path + image)
            pred = thres50(model.predict(im)[0][0])
            line.append(pred)

            if flag in image and pred == 0:
                writer.writerow(line)
            if flag not in image and pred == 1:
                writer.writerow(line)
