# I. Program that change the MAC address

### [Everything you need to know about Python Subprocess](https://docs.python.org/3/library/subprocess.html)
### [Regular Expression for Python](https://pythex.org/)


## Source:
- Material was retrieved from [Learn Python & Ethical Hacking From Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/)

## Introduction:
- A set of instruction to carry out a task
- Make a application more abstract
- Have a block of code that change a MAC address

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

# II. Program that Check if MAC address is change
## Using Regular Expression
