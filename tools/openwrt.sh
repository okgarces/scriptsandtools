#!/bin/bash

while true;
do
output=`./openwrt.exp | grep wlan0 | awk 'NR==1 {print \$4}' | sed 's/\.//' |  xargs echo -n`
TOP="-91"
echo "Check is: $output"
if [ "$output" -le $TOP ]; then
 echo "ALERT!!! WIFI IS NOT WORKING"
 osascript -e 'display notification "ALERT!!! WiFi IS NOT WORKING: '$output'" with title "WiFi Problem"'
fi
sleep 60;
done
