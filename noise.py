#!/bin/env python

import numpy as np
import imageio

def gaussian(image):
    """
    Adds gaussian noise to the image.
    """
    row, col = image.shape
    mean = 0 
    var = 0.1
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noisy = image + gauss

    return noisy

def poisson(image):
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy

# this one adds too much noise
def speckle(image):
    row, col = image.shape
    gauss = np.random.randn(row, col)
    gauss = gauss.reshape(row, col)
    noisy = image + image * gauss
    return noisy

def saltPepper(image):
    row, col = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    # salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0

    return out

from os import listdir

def augmentDir(path):
    for filename in listdir(path):
        im_base =  imageio.imread(path + filename)
        im_1 = np.uint8(gaussian(im_base))
        im_2 = np.uint8(poisson(im_base))
        im_3 = np.uint8(saltPepper(im_base))
        imageio.imwrite(path + 'aug1_' + filename, im_1)
        imageio.imwrite(path + 'aug2_' + filename, im_2)
        imageio.imwrite(path + 'aug3_' + filename, im_3)
    return None

# augment the data present in the training folder
augmentDir('data/train/pos/')
augmentDir('data/train/neg/')

print('Done')
