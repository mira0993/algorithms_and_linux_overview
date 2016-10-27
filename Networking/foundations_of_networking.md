# Foundations of Networking: Networking Basics

*Information taken from [Foundations of Networking: Networking Basics](https://www.linkedin.com/learning/foundations-of-networking-networking-basics) course.*

## Contents
* [Chapter 1. Network Topologies](#1-network-topologies)
* [Chapter 2. Network implementations](#2-network-implementations)
* [Chapter 3. OSI Model](#3-osi-model)
* [Chapter 4. TCP/IP Suite](#3-tcp-ip-suite)

## 1. Network Topologies
### Logical vs Physical Topologies

- **Physical**: Refers to the actual shape or layout of the wires/
- **Logical**: REfers to how the data moves through the network.

### Topologies
- **Mesh Topology**
	- **Full Mesh:** All the devices are directly connected to all devices.
	- **Partial Mesh:** All the devices directly connected to at least two other devices.
		- Mostly found in a WAN environment (Internet is an example).

- **Bus Topology**: All nodes connect directly to main cable called the bus.
	- It is simple to put together.
	- Only one signal can be send at a time.
		- **Contention** is used to determine which node sends signal.
		- **Collision** is when more than one device sends a signal at the same time.

- **Ring Topology**:
	- Similar to a bus connected to a circle.
	- Each node has an opportunity to send a signal. 
		- No collision problems but it may become slow.
		- One damaged node, may bring down all the network.

- **Hierarchical Start Topology**
	-  All the nodes are connected to a central hub or switch.
	-  It requires more cables.
	-  If a node goes down, the network will still be up.

### Point-to-point and point-to-multipoint networks

- **Point-to-point connections**: Two different nodes that are connected directly to each other with no intervening device.
- - **Point-to-multipoint connections**: One node(switch) connected to multiple nodes(servers).

### Peer-to-peer Network Management Model
- **Peer-to-Peer Model**
	- Each computer is responible for own security and management.
	- Used for small networks
- **Client Server Network Model** 
	- All devices access resources through central server.

### Internet
- **Internet** is the worldwide publically accessible infrastructure of cables, routers, switches, etc.
	- WorldWideWeb is the service that runs on top of it.

- **Intranet** is a privately accessible infrastructure of cables, routers, switches and servers.
- **Extranets** is a privately accessible infrastructure of cables, routers, switches and servers. It belongs to a company and may allow others access for a fee for specific purposes (AWS).

## 2. Network implementations

### WANs
- Wide Area Network.
- One large network that covers a large geographic area.

### MANs
- Metropolitan Area Network.
- Uses same technology as WANs but covers a smaller area (max. 50 km).

### LANs
- Local Area Network.
- Limited size (single room, a building, etc.).

### WLANs
- Wireless Local Area Network.
- It is a standard LAN that uses wireless technologies.

### PANs
- Personal Area Networks.
- It uses wireless network but not the same as WLANs.
- It also uses Bluetooth technologies.
- *Example:* Mouse connected to laptop.

## 3. OSI Model
- Open Systems Interconnection Reference Model
- It was originally intended to help students understand the network flow.

![OSI_Model](images/basics_osimodel.jpg)

### Physical Layer
- Physical trasnmission of raw data.
- Transmits data in the form of 1s and 0s.
- Defines encoding methods to transmit data.

### Data Link Layer
- Traffic control: Verify that frames are transmitted and received in the correct sequence.
- Detect and recovers from errors on physical layer.

### Network Layer
- Route packages
	- Uses network conditions to choose the best path the packet should be sent.
		- The decission  is based on number of hops, bandwidth, throughput, etc
- Translates logical addresses into physical addresses.

### Transport Layer
- Ensures messages are delivered error-free and in the correct sequence.
- Message Segmentation
	- Accepts messages from session layer and splits them into smaller units.
	- Prepares header for each smaller unit created.
	- Once the data comes back, it should reassemble the data.
	- Message acknowledgment.
	- Message traffic control: Controls rate of traffic sent when no buffers are available.

### Session Layer
- Resonsible for establishing sessions between processes running on different computers.
	- Establish connection
	- Send data
	- Terminate connection

### Presentation Layer
- Formats data to be presented to the application layer.
- Translator for the network.
	- Character code translation (*Example:* ASCII to EBCDIC).
	- Data conversion: bit order, integer-floating point.
- Data compression:
	- Reduces number of bits needed to transmit data. 
- Data encryption:
	- Encryption of data for security purposes.

### Application Layer
- Examples:
	- Resource sharing.
	- Device redirection.
	- Network management.
	- Instant messages.

### Encapsulation/De-encapsulation
- Each layer of the OSI model adds a header to the data.
	- *Encapsulate*: Move data from the application layer all the way down to the physical data.
	- *De-encapsulate*: MOve data from the physical layer all the way up to the application layer.

		```Data -> Segments -> Packets -> Frames -> Bits```


## 4. TCP/IP Suite

Group of protocls designed to work together to send data across a network. Named after the two major protocols in the suite:
	- TCP: Transport Control Protocol
	- IP: Internet Protocol

### TCP/IP Model
It has four layers:
	1. Application layer
	2. Transport layer
	3. Internet layer
	3. Network Interface Layer

#### TCP/IP Application Layer
- Defines protocols, servicse and processes that allow programs to interface with the network.
- **Examples**:
	- HTTP, Telnet,  FTP, TFTP, SNMP, DNS

#### TCP/IP Transport Layer
- Provides communication sessions management between host computers.
- Common transport layer protocol:
	- TCP (Transport Control Protocol)
	- UDP (Unreliable Datagram Protocol)
	- RTP (Real Time Protocol)

#### Internet Layer
- Taking data into IP datagrams called packets. 
- The header of the packet contains source and destination information.
- It performs routing of IP packets.
- Common protocols:
	- IP: It should find the best route to send the packets.
	- ICMP: Used by ping and traceroute.
	- ARP: Used by IP protocol to find the MAC address.

#### Network Interface Layer
- Specifies how data is physically sent though a network.
- Specifies how bits are electrically signaled by hardware.
- Standards:
	- Ethernet
	- Token Ring
	- FDDI 

### TCP/IP Model vs OSI Model
![TCP_vs_OSI_Model](images/TCP-IP-model-vs-OSI-model.png)

## Commonly Used Network Devices

### NICs
- Network Interface Card or Controller.
- Allows the computer to access the hardware of the network.
- It can be built into the motherboard or as an expansion card.
- The NIC works on the layer 1 and 2 of the OSI model.

### Hubs
- Older technology. Now we use switches.
- Works on layer 1 of the OSI model.
- Logically functions as a bus. You may have collisions.

### Bridges
- Device used to break up a network into smaller segments.

### Switch
- Uses ports to set up point-to-point connections between devices connected to the affected ports.
- No collisiones on network.

### Routers
- They are used to move data around large networks like WANs
- Use layers 3 and 4 of the OSI Model
- Make independant decissions to send data:

#### Criteria Used to Determine Route
- Hops
- Network Traffic
- Network throughput: How fast data can move through a link.
- Network reliablity
- Create/Update tables to always know best route

### Access Points
- Devices that allow computers to access the network.
- Commonly used to connect home computers to Internet.
 