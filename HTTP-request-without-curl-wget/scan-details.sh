#!/bin/bash
# Author-Dipayan Dutta
# My Own website Port Scanner

# open a file descriptor and url/port
exec 3<>/dev/tcp/www.put-the-scan-url/443

lines=(
  'GET / HTTPS/1.1' 
  'Host: www.put-the-scan-url'
  'Connection:close'   
  ''
)

printf '%s\r\n' "${lines[@]}" >&3 

while read -r data <&3; do
  echo "got server data: $data"
done
exec 3>&-

ipaddress=$(dig +short www.put-the-scan-url | awk NR==2)
echo $ipaddress

for port in {22,23,25,80,443,3306,5432,163}
  do (echo>/dev/tcp/$ipaddress/$port) >& /dev/null && echo "$port is open";
done
