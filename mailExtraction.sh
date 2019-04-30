#!/bin/bash
numberOfDir=$(find . -mindepth 1 -maxdepth 1 -type d | wc -l)
echo $numberOfDir

extract(){
	while [ $numberOfDir -gt 0 ];
		do
				lastName=$(ls -td -- */ | head -n 1 | cut -d'/' -f1)
				echo $lastName
				cd $lastName
				cp *.* /home/admin/mails
				cd ..
				rm -rf $lastName
				numberOfDir=$(($numberOfDir-1))
		done
}

extract


