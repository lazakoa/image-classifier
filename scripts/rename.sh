#!/bin/bash
for file in pos/*n0*
do
       newfile=`echo $file | sed 's/n0/n1/'`
       mv $file $newfile
done

