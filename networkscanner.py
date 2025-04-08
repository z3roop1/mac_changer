import scapy.all as scapy

def scan(ip):
    #this is to make an arp packet 
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())

    #this is set an MAC address
    #* as data in a network is shared through a MAC address not IP address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())

    #Combining the both arp and broadcast
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())

    #scapy.ls is used for to list information about the classes 
    # scapy.ls(scapy.ARP())
    # scapy.ls(scapy.Ether())

scan("192.168.1.9")