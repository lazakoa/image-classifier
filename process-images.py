#!/bin/env python

from os import listdir
from PIL import Image
from subprocess import run

def maxSize(dirpath):
    """
    dirpath is a string that is the directory with the raw images relative to
    this script.
    """

    imageList = listdir(dirpath)
    x = 0
    y = 0

    for image in imageList:
        with Image.open(dirpath + '/' + image) as im:
            if im.size[0] > x:
                x = im.size[0]
            if im.size[1] > y:
                y = im.size[1]
    return x,y

def convertImages(srcdir, targetdir):
    """
    srcdir is the raw data
    targetdir is where the converted images will go

    All paths are relative to where this script resides.
    """

    x, y = maxSize(srcdir)
    
    # a extra 3 is added to image size, so both dims are 
    # evenly divisible

    for image in listdir(srcdir):
        print('Converting: ' + image)
        run(['convert', srcdir + '/' + image, '-gravity', 'center',
                '-extent', str(x) + 'x' + str(y + 34),
                targetdir + '/' + image])
    print(x, y)

#convert $i -gravity center -extent 512x512 new/$name.jpg	

if __name__ == '__main__':
    print('Scanning for max image size ...')
    print('Max image size is: ', maxSize('data/raw-data'))
    print('Beginning to convert images ...')
    convertImages('data/raw-data', 'data/images')
    print('Done')
