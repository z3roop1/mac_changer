#!/usr/bin/python

import subprocess

#ifconfig wlan0 down
#ifconfig wlan0 hw ether 01:11:12:23:32:44
#ifconfig wlan0 up

interface = input("enter the interface > ")
new_mac = input("enter the new MAC address > ")

print("[+] Changing mac address")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell= True)
subprocess.call("ifconfig " + interface + " up", shell=True)
