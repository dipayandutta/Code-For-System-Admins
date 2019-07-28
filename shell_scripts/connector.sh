#!/bin/bash

username='locallogin' # change the username
ipaddr="192.168.199.120" #change IP Address

# To connect to the remote server and execute the script
ssh -l ${username} ${ipaddr} 'bash -s' < ram_cpu.sh
