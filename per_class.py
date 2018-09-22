#!/bin/env python

import argparse
from keras.models import load_model
from os import listdir
from os.path import abspath, join

from scipy import misc
import imageio
from PIL import Image
import numpy as np
from skimage import color

"""
    Setting up the argument parser for the script.
"""

parser = argparse.ArgumentParser()
parser.add_argument("model", help="path to the model weights")
parser.add_argument("data", help="path to the data directory")
parser.add_argument("--dims", 
        help="controls image resizing, default is 175", 
        type=int)

args = parser.parse_args()

"""
    Loads the data to be classified. This is process is dependent on
    the directory structure for the image data. Currently this script
    will process the data in:

    data/train -> data/train/pos , data/train/neg
    data/test -> data/test/pos , data/test/neg
    
    Per class accucracy will be returned for neg and pos from how the
    data is partitioned.
"""

data_dir = args.data

data_neg_path = join(args.data, 'neg')
data_pos_path = join(args.data, 'pos')

def returnImages(path):
    images = listdir(path)
    return list(map(lambda x: join(path, x), images))

data_neg = returnImages(data_neg_path)
data_pos = returnImages(data_pos_path)

"""
    Loading the weights and defining a function that will run the 
    classifier on the images.
"""

model = load_model(args.model)

if args.dims == None:
    args.dims = 175

def classify(image):
    im = imageio.imread(image)
    if len(im.shape) == 3:
        im = color.rgb2gray(im)
    im = misc.imresize(im, (args.dims, args.dims))
    im = np.expand_dims(im, axis=0)
    im = np.expand_dims(im, axis=3)
    return model.predict(im)[0][0]


def classifyAll(data):
    return list(map(lambda x: 0 if x < .5 else 1, 
        map(lambda x: classify(x), data)))


data_neg_classified = classifyAll(data_neg)
data_pos_classified = classifyAll(data_pos)

neg_total = len(data_neg_classified)
pos_total = len(data_pos_classified)

neg_correct = neg_total - sum(data_neg_classified)
pos_correct = sum(data_pos_classified)

def report(title, total, correct):
    print(title)
    print("total: ", total)
    print('correctly classified: ', correct)
    print('accuracy: ', correct/total)

report('--Positive Examples--',
        pos_total,
        pos_correct)

report('--Negative Examples--',
        neg_total,
        neg_correct)
