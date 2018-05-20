#!/bin/bash
setting=$2
mkdir testsb
mkdir testsb/pos
mkdir testsb/neg
for file in $1/*$setting"1"*G
do 
	echo $file
	cp $file testsb/pos
done
for file in $1/*$setting"0"*G
do
	echo $file
	cp $file testsb/neg
done

