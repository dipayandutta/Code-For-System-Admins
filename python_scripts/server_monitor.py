'''
Author :- Dipayan Dutta
Purpose:- Remote server monitoring using paramiko

'''
import paramiko
import sys
import time
import select

host = '192.168.56.102'
i    = 1

while True:
	print "Trying to connect to %s (%i/30)" %(host,i)

	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host,username='nagiosserver',password='node')
		print "Connected to host %s" % host
		break

	except paramiko.AuthenticationException:
		print "Authenticatio Error to %s " %host
		sys.exit(2)

	except:
		print "Could not Connect to %s , trying to reconnect...." %host
		i+=1
		time.sleep(2)
	if i==30:
		print "Unable to Connect to host %s" %host
		sys.exit(2)


def freespace():
	stdin_free , stdout_free , stderr_free = ssh.exec_command("free")
	for freespace in stdout_free:
		print freespace

def space():
	stdin_space , stdout_space , stderr_space = ssh.exec_command("df -hT | grep /dev/sda1")
	for space in stdout_space:
		print space

def processConsumption():
	stdin_prc , stdout_prc , stderr_prc = ssh.exec_command("ps aux --sort=-%mem | awk 'NR<=10{print $0}'")
	for process in stdout_prc:
		print process



print "====================================SPACE LEFT====================================="
space()
print "====================================FREE SPACE======================================"
freespace()
print "====================================10 TOP PROCESS==================================="
processConsumption()
