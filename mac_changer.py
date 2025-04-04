#!/usr/bin/python

import subprocess

#list of commands to be used to change a mac address of a machine
#ifconfig wlan0 down
#ifconfig wlan0 hw ether 01:11:12:23:32:44
#ifconfig wlan0 up

interface = input("enter the interface > ")
new_mac = input("enter the new MAC address > ")

print("[+] Changing mac address")
#subprocess.call([]) is way more secure than subprocess.call(,shell=true)
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
