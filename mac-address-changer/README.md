# ADD YOUR CODE HERE IN THIS FOLDER
cd /opt/pycharm-community-2021.3.1/bin
./pycharm.sh
## Source:
- Material was retrieved from [Learn Python & Ethical Hacking From Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/)

## Mac Address Changer
- MAC Address (Media Access Control)
```
- Permanent
- Physical
- Unique
```
- Assigned by manufacture
- Data flow from MAC1 to MAC2
- Change MAC:
```
- Increase anonymity
- Impersonate other devices
- Bu pass filter
```

## Change MAC Address
- Command 1: Turn it down
```
ifconfig eth0 down
# ifconfig: ip configuration
# etho0: name of the interface
# down: turn it off (disable the interface)
```
- Command 2: Change it
```
ifconfig  eth0(name/option) hw ether(MAC Address of eth0) 00:11:22:33:44:55(new)

```
- Command 3: Turn it on again
```
ifconfig eth0 up
```

## Module:
### Using the subprocess Module
```
subprocess.call("string", shell=True)
# run command in the foreground 
# Not execute anything else until it finish the execution
```
### subprocess using list
```
subprocess.call(["ifconfig",interface,"down"], shell=True)
```