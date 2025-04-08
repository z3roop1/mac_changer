import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #srp is used to send and recive packets we can do the same with sr 
    #but with srp we can also set the custom Headers(here MAC address)
    answered  = scapy.srp(arp_request_broadcast, timeout=1)[0]

    for element in answered:
        print(element)
        # print(element[1].hwdst)
        # print(element[1].pdst)
        print("--------------------------------------------")


scan("192.168.1.9/24")

#for this code this is output it contains sent raw packet and response raw packet
#QueryAnswer(query=<Ether  dst=ff:ff:ff:ff:ff:ff type=ARP |<ARP  pdst=192.168.1.23 |>>, answer=<Ether  dst=30:c9:ab:8b:96:0f src=7e:58:26:25:0a:de type=ARP |<ARP  hwtype=Ethernet (10Mb) ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=7e:58:26:25:0a:de psrc=192.168.1.23 hwdst=30:c9:ab:8b:96:0f pdst=192.168.1.24 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>)