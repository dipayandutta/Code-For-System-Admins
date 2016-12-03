#Purpose :- Program to generate Password
#	    based on the choosen algo by the user	
#Author :- Dipayan Dutta
#
#!/bin/bash

echo "Enter choice for ENCRYPTION STANDARD";
echo "1 FOR SHA512"
echo "2 FOR SHA256"
echo "3 FOR MD5"

read choice

if [ $choice == 1 ];then
	echo "Enter number of characters of password "
	read minChars
	echo "Generating password"
	echo "..................."
	echo date +%s | sha512sum | base64 | head -c  $minChars ; echo
elif [ $choice == 2 ];then
	echo "Enter number of characters of password "
	read minChars
	echo "Generating password"
	echo "..................."
	echo date %s | sha256sum | base64 | head -c $minChars ;echo
elif [ $choice == 3 ];then
	echo "Enter number of characters of password "
	read minChars
	echo "Generating password"
	echo ".................."
	echo date +%s | md5sum | base64 | head -c $minChars ; echo
else
	echo "Invalid Choice" 
fi
