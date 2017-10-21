#!/bin/bash

host_name=`hostname`
home_dir=`cat /etc/passwd | grep -e $host_name | cut -d ':' -f 6`
transferMB=`echo "$(ifconfig enp1s0 | grep -v grep | grep bytes | awk '{print $2}' | cut -d ':' -f 2)
/ 1024 / 1024" | bc`

echo "HostName is ===> "$host_name
echo "Home Directory is ===>"$home_dir
echo "Transfer Bytes ===> "$transferMB
