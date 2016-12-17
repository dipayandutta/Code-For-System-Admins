'''
	Author :- Dipayan Dutta

	Purpose :- Try to create a program that shows out nearly similar to the stat command in 				linux , and also get familer with core os and python modules
'''
import os
import grp
import pwd
import sys
import time
from datetime import *

#The file which to check the details for
filename = '/etc/passwd'
#A variable which holds the boolean value of True or False 
isFileExists = os.access(filename,os.F_OK)

#Checking that file is exists or not 
#If Yes Then ....
if isFileExists:

	stat_info 	= os.stat(filename)#Loading total stat_info of the file
	links 		= stat_info.st_nlink#getting the number of links
	uid   		= stat_info.st_uid#Getting the uid of the file owner
	ownername 	= pwd.getpwuid(uid).pw_name #Converting UID to Name 
	#Using Os module to get the mtime , atime and ctime in human readable format
	mod_time 	= datetime.fromtimestamp(os.path.getmtime(filename)) 
	access_time = datetime.fromtimestamp(os.path.getmtime(filename))
	change_time = datetime.fromtimestamp(os.path.getctime(filename))
	#now Checking the file permission , storeing the boolean value in the variables
	isReadable  = os.access(filename,os.R_OK)
	isWriteable = os.access(filename,os.W_OK)
	isExecutable= os.access(filename,os.X_OK)
	#Printing Outputs
	print "Filename : ==> {} ".format(filename)
	print "Total Number of Links ==> {} ".format(links)
	print "Owner of the file ==> {} ".format(ownername)
	print "Modification Time of the file ==> {} ".format(mod_time)
	print "Last Access Time of the file ==> {} ".format(mod_time)
	print "change time of the file ==> {} ".format(change_time) 

	#Checking the file permission for read , write and execute 
	if isReadable:
		print "U can read the file "
	else:
		print "File is not readable"
	if isWriteable:
		print "U can add , delete contents on the file "
	else:
		print "File is Write Protected"
	if isExecutable:
		print "You can execute this file"
	else:
		print "You cannot Execute this file"

else:
	print "File Not Exist"