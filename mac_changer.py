#!/usr/bin/python

import subprocess

#ifconfig wlan0 down
#ifconfig wlan0 hw ether 01:11:12:23:32:44
#ifconfig wlan0 up
print("[+] Changing mac address")
subprocess.call("ifconfig wlp4s0 down" , shell = True)
subprocess.call("ifconfig wlp4s0 hw ether 12:23:34:45:23:65", shell= True)
subprocess.call("ifconfig wlp4s0 up", shell=True)
