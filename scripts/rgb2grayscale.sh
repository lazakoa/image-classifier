#!/bin/bash

DIRECTORY=$1
counter=0
for filename in $1/*.jpg; do
    convert $filename -set colorspace Gray -separate -average $filename
    echo $filename
    counter=$(expr $counter + 1)
    echo $counter 
done
