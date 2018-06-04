#!/bin/env python

import csv
from scipy import misc
from os import listdir, makedirs
from random import shuffle
import shutil
import imageio
from keras.models import load_model
import sys
from PIL import Image
import numpy as np

class Images:

    def __init__(self, path, model):
        # works
        self.path = path
        self.model = load_model(model)
        return None

    def select(self, number=100):
        # works
        self.images = [] 
        items = listdir(path)
        shuffle(items)

        if len(items) < number:
            for item in items:
                self.images.append(item)
        else:
            for i in range(number):
                self.images.append(items[i])
        return self.images

    def move(self, targetdir):
        # works
        makedirs(targetdir)
        for image in self.images:
            shutil.copy(self.path + image, targetdir + image)
        return None

    def classify(self):
        # works
        self.classified = []
        for image in self.images:
            im = imageio.imread(path + image)
            im = misc.imresize(im, (200, 200))
            im = np.expand_dims(im, axis=0)
            im = np.expand_dims(im, axis=3)
            self.classified.append([image, 
                self.model.predict(im)[0][0]])
        return self.classified
        
    def save(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in self.classified:
                writer.writerow(item)

def pathPad(path):
    if path[-1] == '/':
        return path
    else:
        return path + '/'

if __name__ == "__main__":
    """
        takes four arguments:
        path -- path of the image files
        model -- name of the keras model
        targetdir -- where images will be copied to
        filename -- name of the saved csv file

        NOTE: instead of copying it's possible to move as well, 1
        line change.
        
        Sample usage below: 
        manual_check.py  data/train/pos num.h5 data-2/ example.csv
    """
    path = pathPad(sys.argv[1])
    model = sys.argv[2]
    targetdir = pathPad(sys.argv[3])
    filename = sys.argv[4]
    
    temp = Images(path, model)
    temp.select()
    temp.classify()
    temp.move(targetdir)
    temp.save(filename)