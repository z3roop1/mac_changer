#!/usr/bin/python

import subprocess
import argparse
import re

def change_mac(interface , mac):
    print("[+] Changing MAC address")
    #subprocess.call([]) is way more secure than subprocess.call(,shell=true)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="add the Interface(ex: wlan0)",type=str, required=True)
    parser.add_argument("-m", "--mac", help="add a new MAC address(ex: 00:11:22:33:44:55)",type=str, required=True)
    args = parser.parse_args()
    return args

def get_mac(interface):
    output = subprocess.check_output("ifconfig " + interface, shell=True, text=True)
    currentmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    return currentmac.group(0) if currentmac else ""

def main():
    args = arg_parser()
    current_mac = get_mac(args.interface)
    print("[+] Current MAC address: " + str(current_mac))
    if current_mac: change_mac(args.interface , args.mac)
    else: 
        print("[-] update failed") 
        return
    print("[+] Your MAC has updated succesfully to: " + get_mac(args.interface))


main()