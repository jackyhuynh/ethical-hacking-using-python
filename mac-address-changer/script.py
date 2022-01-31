#!/usr/bin/env python

import subprocess
import optparse

def mac_changer_str(interface, new_mac):
    subprocess.call(f"ifconfig {interface} down", shell=True)       # disable the MAC address
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)         # enable the mac Address


"""
This is a more secure version of the above command
"""
def mac_changer_list(interface, new_mac):
    subprocess.call(["ifconfig",interface,"down"])       # disable the MAC address
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])         # enable the mac Address


parser = optparse.OptionParser()
# -i, --interface: to specify the interface/ dest: where store the user input, help="Interface to change its MAC address"
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

parser.parse_args()

interface = input("interface > ")
new_mac = input("new MAC > ")
mac_changer_list(interface, new_mac)