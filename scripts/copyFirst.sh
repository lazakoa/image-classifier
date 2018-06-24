#!/bin/bash
i="0"	
for text in $(cat sorted.txt); do
	if [[ $text = *".png"* ]];
	then
	echo $text
	i=$[$i+1] 
       	cp $text Top100	
		if [ $i -gt 100 ]; then
		       break	
		fi 
fi
done

