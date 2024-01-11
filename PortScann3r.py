import sys
import socket
import argparse
from datetime import datetime

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open on {target}")
                # Enhance service detection by attempting to determine the service version
                try:
                    service = socket.getservbyport(port)
                    print(f" Service: {service}")
                except (socket.error, OSError):
                    print(" Service: Unable to determine service version")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

def port_scanner(target, start_port, end_port):
    print("-" * 50)
    print("Scanning target " + target)
    print("Time started: " + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            scan_port(target, port)
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", nargs=2, type=int, default=[50, 85],
                        help="Start and end ports to scan (default: 50-85)")

    args = parser.parse_args()

    print(''' 
   
██████╗       ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗      ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ╚════╝╚════██║██║     ██╔══██║██║╚██╗██║
██║           ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝           ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                
                                      -@pr4T!K
                                   
''')

    port_scanner(args.target, args.ports[0], args.ports[1])

if __name__ == "__main__":
    main()