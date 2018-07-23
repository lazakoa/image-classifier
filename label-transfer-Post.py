#!/bin/env python

from os import listdir, mkdir
from shutil import copyfile

# directory with correct labels but incorrect padding
correctLabels = 'data/relabeling/correct-labels'

# directory with bad labels but right padding
unpaddedBadLabels = 'data/relabeling/unpadded-bad-labels'

# desired output, directory with proper labels and correct padding
relabeledMaster = 'data/relabeling/relabeled-master'

# directory for desired output
mkdir(relabeledMaster)

labelPool = set(listdir(correctLabels))

def complimentFactory(str1, str2):
    def temp(string):
        return string.replace(str1, str2)
    return temp

# functions that generate a complimentary string to check
n0sub = complimentFactory('n0', 'n1')
n1sub = complimentFactory('n1', 'n0')

# this can be made more compact, another function factory would work.
for badLabel in listdir(unpaddedBadLabels):

    if 'n1' in badLabel:
        temp = n1sub(badLabel)

        if badLabel in labelPool:
            copyfile(unpaddedBadLabels + '/' + badLabel,
                     relabeledMaster + '/' + badLabel)
        
        elif temp in labelPool:
            copyfile(unpaddedBadLabels + '/' + badLabel,
                     relabeledMaster + '/' + temp)
        else:
            print('ERROR 1: ', badLabel)
    
    elif 'n0' in badLabel:
        temp = n0sub(badLabel)

        if badLabel in labelPool:
            copyfile(unpaddedBadLabels + '/' + badLabel,
                     relabeledMaster + '/' + badLabel)

        elif temp in labelPool:
            copyfile(unpaddedBadLabels + '/' + badLabel,
                     relabeledMaster + '/' + temp)
        else:
            print('ERROR 2: ', badLabel)

    else:
        print('Bad data: ', badLabel)
    
