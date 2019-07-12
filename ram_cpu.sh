#!/bin/bash


# function defination
ram_cpu_util()
{
    # Get Total Memory Space in GB
    total=`free -mh |  awk 'BEGIN{FS=" "} {print $2 }' | awk 'NR==2{ print }'`
    # Get Used Memory Space in GB
    used=`free -mh |  awk 'BEGIN{FS=" "} {print $3 }' | awk 'NR==2{ print }'`
    # Get free Memory Space in GB
    free=`free -mh |  awk 'BEGIN{FS=" "} {print $4 }' | awk 'NR==2{ print }'`
    # Memory Utilization in Percentage
    mem_percent=`free -m | awk 'NR==2{printf "%.2f%%\n",$3*100/$2 }'`
    # Get the remote server CPU utilization in Percentage(%)
    cpu_utilization=`grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}'`
    # Get CPU load
    cpu_load=`top -bn1 | grep load | awk '{printf "CPU Load: %.2f\n", $(NF-2)}' `
    # optionally i added total Number of Core
    cpu_core=`nproc`
    # Print The Detials on the running Terminal
    echo "Total RAM ==> "$total
    echo "Used RAM ==> "$used
    echo "Free RAM ==> "$free
    echo "RAM Utilzation => " $mem_percent
    echo "CPU Utilization =>" $cpu_utilization
    echo "CPU Load ==> " $cpu_load
    echo "Total Number Of Cores => " $cpu_core
}
# function Calling
ram_cpu_util
