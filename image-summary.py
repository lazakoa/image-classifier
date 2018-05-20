#!/bin/env python

import sys
from os import listdir

"""
    Takes a directory as an argument.
"""

def summary(targetDir):
    imageNames = listdir(targetDir)
    c1 = 0
    n1 = 0
    h1 = 0
    total = len(imageNames)

    for name in imageNames:
        if 'c1' in name:
            c1 += 1
        if 'n1' in name:
            n1 += 1
        if 'h1' in name:
            h1 += 1

    print('Summary: ')
    print('Contours: [1] ', c1, ' [0] ', total - c1)
    print('Numbers : [1] ', n1, ' [0] ', total - n1)
    print('Hands   : [1] ', h1, ' [0] ', total - h1)

if __name__ == "__main__":
    if sys.argv[1] == None:
        print("Forgot to give the target directory.")
    else:
        targetDir = sys.argv[1]
        summary(targetDir)
