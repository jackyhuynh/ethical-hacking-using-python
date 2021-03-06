#!/usr/bin/env python

import subprocess
import optparse
import re

"""
This is a security testing of the ifconfig
"""
# def mac_changer_str(interface, new_mac):
#    subprocess.call(f"ifconfig {interface} down", shell=True)       # disable the MAC address
#    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
#    subprocess.call(f"ifconfig {interface} up", shell=True)         # enable the mac Address


"""
This is a more secure version of the above function
That can help user prevent code injection
More detail on list 
"""


def mac_changer(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])  # disable the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])  # enable the mac Address


"""
get user input
"""


def get_arguments():
    parser = optparse.OptionParser()
    # -i, --interface: to specify the interface/ dest: where store the user input, help="Interface to change its MAC address"
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # methods return 2 set of information
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Clould not read MAC address")


# get the user input
options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# interface of the options user input
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC was sucessfully change to " + current_mac)
else:
    print("[-] MAC address did not get changed.")



