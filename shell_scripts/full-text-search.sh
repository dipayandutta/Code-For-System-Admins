#!/bin/bash

#searchString="Acid/Calcium, Maintenance-free Liquid Electrolyte"
searchString="src:"
find /data/ -iname "*" -type f -print0 | xargs -0 grep -H $searchString 2>error.log
prevState=`echo $?`
echo $prevState

if [ "$prevState" -ne 0 ]
then
	echo "Search String is in pdf file"
fi
find /data/ -iname "*.pdf" -exec pdfgrep $searchString {} + 2>error.log 
