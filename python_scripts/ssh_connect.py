import paramiko
import sys
from scp import SCPClient

username = 'yourusername'
password = 'yourpassword'
host = '192.168.56.101'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
	ssh.connect(host,port,username,password)
	stdin_pwd ,stdout_pwd , stderr_pwd = ssh.exec_command("pwd")
	stdin_ls , stdout_ls  , stderr_ls  = ssh.exec_command("ls -l")
	
	print stdout_pwd.read()
	for files in stdout_ls.read().split('\n'):
		print files

	
except Exception as e:
	raise "Unable to connect to {} ".format(host)
	raise e 

finally:
	ssh.close()