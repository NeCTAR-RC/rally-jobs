#!/bin/sh

# Simple uptime metric
UPTIME=$(cat /proc/uptime | awk '{print $1}')
echo "{\"uptime\":$UPTIME}"
