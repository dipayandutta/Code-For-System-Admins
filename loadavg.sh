#!/bin/bash
OneMin=$(uptime | awk '{print $8}' | cut -d ',' -f1)
FiveMin=$(uptime | awk '{print $9}' | cut -d ',' -f1)
FifteenMin=$(uptime | awk '{print $10}' | cut -d ',' -f1)

echo $OneMin
echo $FiveMin
echo $FifteenMin
