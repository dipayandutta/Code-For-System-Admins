# Author : - Dipayan Dutta

#Use :- Pass the user name as an argument and 	
	#this programm will tell you about the 
	#user 

#usage : - ./user_type.sh username


#!/bin/bash

if test $# -ne 1 ;then
	echo "USAGE : $0 username";
	exit 3;
else
	uid=`grep $1 /etc/passwd | cut -d':' -f3`
	
	echo "$1 user uid is " $uid
	
	if [ $uid -ge 1000 ];then
		echo "Normal user";
	elif [ $uid == 0 ];then
		echo "root user";
	elif [[ $uid -ge 1 && $uid -le 200 ]];then
		echo "System User assigned statically to the system processed";
	elif [[ $uid -ge 200 && $uid -le 1000 ]];then
		echo "System User that used by system process that do not owned system files .";
	else
		echo "User not preasent";
	fi
fi	
