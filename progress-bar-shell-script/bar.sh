#!/bin/bash

count=0
max_count=10
percent=0
while [ $count -lt $max_count ]; do
	sleep .5
	count=$((count + 1 ))
	percent=$((count*100/max_count))
	printf $percent
	echo  "%"

	echo -e "\n"
done
