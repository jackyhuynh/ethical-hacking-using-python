# Program that change the MAC address
- Using wireless adapter
- Scanner 

## Tools:
- [Adapter](https://zsecurity.org/shop/)
- [Video of choosing adapter](https://www.youtube.com/watch?v=0lqRZ3MWPXY)
- [Window Virtual Machine](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)

## Resources:
- [Python list](https://www.tutorialspoint.com/python/python_lists.htm)
- [Send and receive packets (sr)](https://scapy.readthedocs.io/en/latest/usage.html#send-and-receive-packets-sr)
- [ARP Ping](https://scapy.readthedocs.io/en/latest/usage.html#arp-ping)
- [Scapy Document Python](https://scapy.readthedocs.io/en/latest/)

## Discover client from the network
- Use ARP protocal to send request, response to discover all clients in the network. 
- Plan:
	- Create ARP request directed to broadcast MAC asking for IP
	- Send packet and receive response
	- Parse the response
	- Print result
## Scan the all the IP address associate with the MAC address using scapy package
- route -n return all the current gateway router
```bash
root@kali:~/PycharmProjects/network-scanner# route -n
```
- Output
```bash
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.17.2    0.0.0.0         UG    100    0        0 eth0
192.168.17.0    0.0.0.0         255.255.255.0   U     100    0        0 eth0
```

- List all the client from the same network
```python
# network_scanner.py
#!/usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.17.1/24")
```

- Out put
```bash
root@kali:~/PycharmProjects/network-scanner# python3 network_scanner.py
Begin emission:
Finished sending 256 packets.
***
Received 3 packets, got 3 answers, remaining 253 packets
  00:50:56:c0:00:08 VMware 192.168.17.1
  00:50:56:f6:70:b8 VMware 192.168.17.2
  00:50:56:f4:22:0e VMware 192.168.17.254

``` 
- Network scan
```python
#!/usr/bin/env python3
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # use custom Ether to capture MAC of the broadcast
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request

    # srp return 2 list answered and unanswered list
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\t\t\tMAC ADDRESS\n-------------------------------")
    for answer in answered_list:
        print(answer[1].psrc+"\t\t"+answer[1].hwsrc)


scan("192.168.17.1/24")

```
