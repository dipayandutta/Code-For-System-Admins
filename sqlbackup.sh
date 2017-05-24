#Author :-Dipayan Dutta
#Date   :-24/05/2017
#Purpose:- Shell Script to take mysql backup
#version:- 1.0

#creating a function name - backup
function backup(){
	
	#creating a directory with current date
	mkdir sqlbackup_$(date '+%d-%b-%Y')
	#changing my directory location	
	cd sqlbackup_$(date '+%d-%b-%Y')
	#reading Database name
	echo "Enter Database Name"
	read dbname
	#Reading Database Username
	echo "Enter user Name"
	read username
	#using mysqldump to create database backup
	mysqldump -u $username -p $dbname > $dbname.sql
	#Reading password
	#checking if last command is successful or not
	if [ !$? ];then
		echo "Database backup Done"
	else 
		echo "Unable to take backup"
	fi
	#Creating compressed file 	
	tar -czf $dbname.tar.gz $dbname.sql 
	#Checking if compression command run successfully or not 
	if [ !$? ] ; then
		echo "Compression Done"
	else
		echo "Unable to Compress"
	fi
	chmod 0600 $dbname.tar.gz 
	#Reading Server and User Details 
	echo "Enter Remote Server Username"
	read remoteuser
	echo "Enter Remote server IPaddress"
	read ipadd
	echo "Enter Path to copy"
	read location

	rsync -avz $dbname.tar.gz $remoteuser@$ipadd:$location
}

backup #calling the backup function 
