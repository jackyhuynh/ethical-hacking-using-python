#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

"""
+ process packet take a packet as parameter
+ 
"""


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            print("HTTP Response")
            print(scapy_packet.show())

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
# call back function use in every single packet in the queue
# process_packet will be executed in every packet that trapped in the netfilter queue
queue.bind(0, process_packet)
queue.run()

"""
using flush in the terminal to flush the program
"""

