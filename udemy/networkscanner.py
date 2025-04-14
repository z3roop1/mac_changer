#!/usr/bin/env python

import scapy.all as scapy

import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered  = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(results_list):
    print("IP\t\t\t MAC Address")
    for element in results_list:
        print(element["ip"]+"\t\t"+element["mac"])

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",help="select the target(eg: 10.0.2.23/24)",type=str, required=True)
    args = parser.parse_args()
    return args

def main():
    args = arguments()
    scan_result = scan(args.target)
    print_result(scan_result)

main()