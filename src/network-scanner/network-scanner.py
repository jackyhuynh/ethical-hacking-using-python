#!/usr/bin/env python3
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # use custom Ether to capture MAC of the broadcast
    broadcast = scapy.Ether\
        (dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = \
        broadcast / arp_request

    # srp return 2 list answered and unanswered list
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    client_list = []
    for answer in answered_list:
        client_list.append({"ip": answer[1].psrc,
                            "mac": answer[1].hwsrc})

    return client_list


def print_result(answered_list):
    print("IP\t\t\t\tMAC ADDRESS\n--------------------------------------------")
    for answer in answered_list:
        print(answer['ip'] + "\t\t" + answer['mac'])


options_ = get_arguments()
# options = "192.168.17.1/24"

print_result(scan("192.168.17.1/24"))
