# DNS Spoofer

## Introduction 
- Check when the user go to a specific website and redirect it.
- 
## Testing Environment:
- Testing from our own environment (local machine)
- Using Scapy to modify the captured packet
- Analyze what happen when a request is sent and received in DNS layer, UDP layer
## Resorces:
- [Using Scapy in your tools](https://scapy.readthedocs.io/en/latest/extending.html)
- [Scapy Source Code](https://github.com/invernizzi/scapy-http)
- [Filter that apply to ARP](https://biot.com/capstats/bpf.html)
- [Steal my login](https://www.stealmylogin.com/demo.html)
- [Test capturing URL](http://testphp.vulnweb.com/login.php)

## Tools:
- Store the capture packet in a queue

```bash
root@kali:~/PycharmProjects/packet-sniffer-2# iptables -I FORWARD -j NFQUEUE --queue-num 0
```
- Need to install netfilterqueue