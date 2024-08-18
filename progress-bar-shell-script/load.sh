#!/bin/bash

init(){
	percent=$1
	bar_count=0
	# Change the location of the cursor
	printf "\033[s"
}

update(){
	bar_count=$(($bar_count + 100))

	# add a symbol in every delimeter
	if [ $(($bar_count % $percent)) -lt 100 ];then
		bar="$bar#"
	fi

	# print progress bar and percent
	#printf "$bar $(($bar_count / $percent))%%\n"
	printf "\033[u $bar\033[u \033[100C $(($bar_count / $percent))%%"
}
init 500
count=0
while [ $count -lt 500 ]; do
	sleep .5
	count=$((count + 1 ))
	update
done
