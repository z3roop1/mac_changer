#!/usr/bin/python

import subprocess
import argparse

#list of commands to be used to change a mac address of a machine
#ifconfig wlan0 down
#ifconfig wlan0 hw ether 01:11:12:23:32:44
#ifconfig wlan0 up

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", help="add the Interface(ex: wlan0)",type=str, required=True)
parser.add_argument("-m", "--mac", help="add a new MAC address(ex: 00:11:22:33:44:55)",type=str, required=True)
args = parser.parse_args()


print("[+] Changing mac address")
#subprocess.call([]) is way more secure than subprocess.call(,shell=true)
subprocess.call(["ifconfig",args.interface,"down"])
subprocess.call(["ifconfig",args.interface,"hw","ether",args.mac])
subprocess.call(["ifconfig",args.interface,"up"])
