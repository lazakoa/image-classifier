#!/bin/env python

"""
    Generates the training and test sets from the raw data.

    WARNING: running this script *WILL* destroy your previous test/dev folders

    Run this once.
"""

from os import listdir, makedirs
from os.path import isfile, join
from random import shuffle
from math import ceil
import shutil

from sys import argv

files = listdir('data/images')

def segmentDataSet(data, target='c1n1h1'):
    """ Takes a list of files, and spits out two lists. One list for positive
    labels and one list for negative labels.
    """

    pos = []
    neg = []

    for d in data:
	# c1n1h1
        if target in d[-10:-4]:
            pos.append(d)
        else:
            neg.append(d)
    return pos, neg

#pos, neg = segmentDataSet(files) 
def splitData(data, ratio=.93):
    temp = ceil(len(data) * ratio)
    return data[:temp], data[temp:]


"""
    usage:
        
    ./datasetup [n1|n0|c1|c0|h1|h0] ratio
"""

if __name__ == "__main__":
    pos, neg = segmentDataSet(files, argv[1])
    ans = str(input('Regenerate train and test directories? [y/n] '))
    if ans in ['Y', 'y', 'yes', 'YES']:
        if 'train' in listdir('data') and 'test' in listdir('data'):
            print('Deleting train/')
            shutil.rmtree('data/train/')
            print('Deleting test/')
            shutil.rmtree('data/test/')
            print('Done with deletion')

        shuffle(pos), shuffle(neg)
        
        trainPos, testPos = splitData(pos, float(argv[2]))
        trainNeg, testNeg = splitData(neg, float(argv[2]))
        
        train = trainPos + trainNeg
        test = testPos + testNeg
        
        print('Making the train directory')
        makedirs('data/train')
        makedirs('data/train/pos')
        for f in trainPos:
            shutil.copy('data/images/' + f, 'data/train/pos')

        makedirs('data/train/neg')
        for f in trainNeg:
            shutil.copy('data/images/' + f, 'data/train/neg')

        print('Finished populating train directory')

        print('Making the test directory')
        makedirs('data/test')
        makedirs('data/test/pos')
        for f in testPos:
            shutil.copy('data/images/' + f, 'data/test/pos')
       
        makedirs('data/test/neg')
        for f in testNeg:
            shutil.copy('data/images/' + f, 'data/test/neg')

        print('Finished populating test directory')
        print('Finished generating train & test')
    else:
        print('Exiting')

