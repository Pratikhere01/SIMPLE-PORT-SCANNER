```

██████╗       ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗      ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ╚════╝╚════██║██║     ██╔══██║██║╚██╗██║
██║           ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝           ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                
                                      -@pr4T!K

```

**Scans for open ports over a Network**


A Port scanner software can probe machines for open ports. Port scanners are often used by network administrators to verify the security of machines in their network. They are of interest to Internet miscreants as well, since attackers can use them to find machines to compromise simply by probing for software versions with known vulnerabilities.




The basic idea behind a port scanner is simple: Given an IP address of a machine and a list of interesting ports to scan, the scanner will connect on each port using TCP sockets, make a determination of whether or not the port is open based on success of the connection request and close the socket before moving on to the next port to scan.





It additionally provides information about the associated service running on the open port.



Features to be add in future:
- Add functionality to save the scan results to a file for later analysis.
- Scan a range of IP addresses.
