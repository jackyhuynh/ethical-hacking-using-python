# Ethical Hacking Using Python

## [LINUX COMMAND LINE](https://www.mediacollege.com/linux/command/linux-command.html)
## Start PyCharm:
```bash
root@kali: cd /opt/pycharm-community-2021.3.1/bin
root@kali: ./pycharm.sh

```
## Navigate to the projectL
```bash
root@kali: cd /PycharmProjects/
```

## Introduction
The goal of the program in this repo is usually to hack into a certain system! 
Start by learning how this system work and its weaknesses, then how to write a 
python program to exploit these weaknesses and hack the system. Application include
 from backdoors, keyloggers, credential harvesters, network hacking tools, website hacking tools 
- Material was retrieved from [Learn Python & Ethical Hacking From Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/)

## Resources:



## Programming topics:
- Programming topics:
```
- Using modules and libraries.
- Variables, types ...etc.
- Handling user input.
- Reading and writing files.
- Functions.
- Loops.
- Data structures.
- Regex.
- Desiccation making.
- Recursion.
- Threading.
- Object oriented programming.
- Packet manipulation using scapy.
- Netfilterqueue.
- Socket programming.
- String manipulation.
- Exceptions.
- Serialisation.
- Compiling programs to binary executables.
- Sending & receiving HTTP requests.
- Parsing HTML.
```
- Hacking topics:
```
- Basics of network hacking / penetration testing.
- Changing MAC address & bypassing filtering.
- Network mapping.
- ARP Spoofing - redirect the flow of packets in a network.
- DNS Spoofing - redirect requests from one website to another.
- Spying on any client connected to the network - see usernames, passwords, visited urls ....etc.
- Inject code in pages loaded by any computer connected to the same network.
- Replace files on the fly as they get downloaded by any computer on the same network.
- Detect ARP spoofing attacks.
- Bypass HTTPS.
- Create malware for Windows, OS X and Linux.
- Create trojans for Windows, OS X and Linux.
- Hack Windows, OS X and Linux using custom backdoor.
- Bypass Anti-Virus programs.
- Use fake login prompt to steal credentials.
- Display fake updates.
- Use own keylogger to spy on everything typed on a Windows & Linux.
- Learn the basics of website hacking / penetration testing.
- Discover subdomains.
- Discover hidden files and directories in a website.
- Run wordlist attacks to guess login information.
- Discover and exploit XSS vulnerabilities.
- Discover weaknesses in websites using own vulnerability scanner.
```
- Application in this repo:
```
- mac_changer - changes MAC Address to anything we want.
- network_scanner - scans network and discovers the IP and MAC address of all connected clients.
- arp_spoofer - runs an arp spoofing attack to redirect the flow of packets in the network allowing us to intercept data.
- packet_sniffer - filters intercepted data and shows usernames, passwords, visited links ....etc
- dns_spoofer - redirects DNS requests, eg: redirects requests to from one domain to another.
- file_interceptor - replaces intercepted files with any file we want.
- code_injector - injects code in intercepted HTML pages.
- arpspoof_detector - detects ARP spoofing attacks.
- execute_command payload - executes a system command on the computer it gets executed on.
- execute_and_report payload - executes a system command and reports result via email.
- download_and_execute payload - downloads a file and executes it on target system.
- download_execute_and_report payload - downloads a file, executes it, and reports result by email.
- reverse_backdoor - gives remote control over the system it gets executed on, allows us to
- Access file system.
- Execute system commands.
- Download & upload files
- keylogger - records key-strikes and sends them to us by email.
- crawler - discovers hidden paths on a target website.
- discover_subdomains - discovers subdomains on target website.
- spider - maps the whole target website and discovers all files, directories and links.
- guess_login - runs a wordlist attack to guess login information.
- vulnerability_scanner - scans a target website for weaknesses and produces a report with all findings.
```
Acomplishment:
```
As you build the above you'll learn:
- Setting up a penetration testing lab to practice hacking safely.
- Installing Kali Linux and Windows as virtual machines inside ANY operating system.
- Linux Basics.
- Linux terminal basics.
- How networks work.
- How clients communicate in a network.
- Address Resolution Protocol - ARP.
- Network layers.
- Domain Name System - DNS.
- Hypertext Transfer Protocol - HTTP.
- HTTPS.
- How anti-virus programs work.
- Sockets.
- Connecting devices over TCP.
- Transferring data over TCP.
- How website work.
- GET & POST requests.
```


## Documents/Research Paper
- [Python 3 Standard Library](https://docs.python.org/3/index.html)

## Technology
List of technology
- Python 
- Object Oriented Design
- PyCharm IDE

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them
- Jupyter Notebook: If you want just test the code, simply go to google and search for jupiter notebook or another Python online IDE. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 
- Anacoda Navigator: Install Anaconda Navigator if you want to develop data-science projects using Python or R. Anaconda Navigator is a desktop graphical user interface included in Anaconda that allows you to launch applications and easily manage conda packages, environments and channels without the need to use command line commands. 
- PyCharm Community IDE: Be More Productive: Save time while PyCharm takes care of the routine. Focus on the bigger things and embrace the keyboard-centric approach to get the most of PyCharm's many productivity features. Get Smart Assistance: PyCharm knows everything about your code. Rely on it for intelligent code completion, on-the-fly error checking and quick-fixes, easy project navigation, and much more.
- Please download open the source folder as a project (right click on the folder that contain main, templates, static, and venv and run as open Python Project using PyCharm).
- PLease download all the necessary packages before run the application. If you use PyCharm, it will take care of your missing package or
```
# or u can use
pip install all-missing-package(replace all-missing-package with the package(packages) that you intend to install)
```

### Installing
A step by step series of examples that tell you how to get a development enviroment running:
* Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html) Community Edition.
* [Install Anacoda Navigator](https://docs.anaconda.com/anaconda/navigator/install/#:~:text=Installing%20Navigator%20Navigator%20is%20automatically%20installed%20when%20you,install%20anaconda-navigator.%20To%20start%20Navigator,%20see%20Getting%20Started.) - If you haven't downloaded and installed Anacoda Navigator yet, here's how to get started.
* [Jupyter Notebook](https://jupyter.org/try) - Click here to go to the online free Jupiter Notebook.

## Running the tests


## Deployment
All the notebook can be used for research and academic basic function for Python. 

## Built With
* [PyCharm Community IDE](https://www.jetbrains.com/pycharm/download/#section=windows) 

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](). 

## Authors

* **Truc Huynh** - *Initial work* - [TrucDev](https://github.com/jackyhuynh)

## Format
my README.md format was retrieved from
* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Any acknowledgments go here
