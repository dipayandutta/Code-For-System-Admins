#!/bin/bash
total_memory=$(free -mh | grep "Mem:" | awk '{print $2}')
used_memory=$(free -mh | grep "Mem:" | awk '{print $3}')
free_memory=$(free -mh | grep "Mem:" | awk '{print $4}')

echo "Total Memory "$total_memory
echo "Used Memory "$used_memory
echo "Free Memory "$free_memory


total_swap_memory=$(free -mh | grep "Swap:" | awk '{print $2}')
used_swap_memory=$(free -mh | grep "Swap:" | awk '{print $3}')
free_swap_memory=$(free -mh | grep "Swap:" | awk '{print $4}')

echo "Total Swap Memory "$total_swap_memory
echo "Used Swap Memory "$used_swap_memory
echo "Free Swap Memory"$free_swap_memory
