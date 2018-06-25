#!/bin/env python

from os import listdir
from PIL import Image
from subprocess import run
import sys

"""
    Script takes two arguments, the targetdir must exist for the 
    script to run.
    
    image2square.py srcdir targetdir
"""

def convertImages(srcdir, targetdir, size):

    for image in listdir(srcdir):
        print("Processing: " + image)

        # get max dim
        
        side = 0
        
        with Image.open(srcdir + '/' + image) as im:

            side = max(im.size[0], im.size[1])

<<<<<<< HEAD
        if side >= 175:
=======
        if side >= size:
>>>>>>> df8c0db69b6e54bb72389103458f1cbed3b51d3b
            run(['convert', srcdir + '/' + image, '-gravity', 'center',
                '-extent', str(side) + 'x' + str(side),
                targetdir + '/' + image])
        else:
            pass

if __name__ == "__main__":
    print('test')
    src = sys.argv[1]
    target = sys.argv[2]
    print('Beginning to conver images')
    convertImages(src, target, sys.argv[3])
    print('Done')
