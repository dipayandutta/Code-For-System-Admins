#!/bin/bash

# open a file descriptor and url/port
exec 3<>/dev/tcp/www.baruipurcollege.ac.in/443

lines=(
  'GET / HTTPS/1.1' 
  'Host: www.baruipurcollege.ac.in'
  'Connection:close'   
  ''
)

printf '%s\r\n' "${lines[@]}" >&3 

while read -r data <&3; do
  echo "got server data: $data"
done
exec 3>&-
