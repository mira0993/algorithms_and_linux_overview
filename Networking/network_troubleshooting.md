# Troubleshooting Network Connectivity

*Information taken from [Troubleshooting Network Connectivity](https://www.linkedin.com/learning/troubleshooting-network-connectivity) course.*

## Contents
* [Chapter 1. Data Link and Network Layer](#1-Data-link-and-network-layers)
* [Chapter 2. Transport Layer Troubleshooting](#2-transport-layer-troubleshooting)

## 1. Data Link and Network Layer Troubleshooting

### Switching Loop
- It happens when a connection come backs to the original device.

- The easy way to discover the loop is rebooting the switches and leaving one disconnected. if the loop is fixed, then the switch with the loop is the one that we deactivated.
- Once we idenitfy the looping switch, we should trunk the port that is causing the issue.

### Duplicate Addressing

#### Symptoms
- Users can't get some resources.
- Ping always come back.

#### How to fix it?
- Disconnect a suspicious node and ping the IP, to see if it is still coming back or not.

#### How to avoid it?
- Use DHCP Snooping

#### Duplicate Gateway IP
- Heavy packet loss for entire subnet.
- Router detection.

### DNS/IP Addressing Issues
- Check with `ipconfig / ifconfig` the address configuration:
	- Check address is valid
	- ping DNS IP (Example: 8.8.8.8)
	- ping with the hostname (Example: google.com)

- If the last one doesn't work, then there is a problem in DNS.
- **Test to Alternate DNS**
	- Use `nslookup` to check you can do queries.
- If the issues persist:
	- We can try to disable the firewall.
	- There may be a wrong subnet configuration.

### Failed Routes/Routing Loop
- The troubleshooting duo: `ping, traceroute`
- Checkings:
	- Verify route to host (ping/traceroute)

## 2. Transport Layer Troubleshooting

### Port already in use, netstat

- **Socket** is bi-directional connection that contains an address and a port.
- Only a single application on a given protocol can listen at the same time in the same port.
- `netstat` helps to determine if a port is in use or not:
	`netstat -nap|grep :80`

### Test with wireshark/tcpdump

- These are packet captures programs fro Windows and Linux.
- We need to filter the traffic by IP and port. If not, we will get a really long lists of packets.