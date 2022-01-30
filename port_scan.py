import socket


# Scanning
def port_scan(address, port):
    try:
        target = socket.gethostbyname(address) 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Setting up socket
        socket.setdefaulttimeout(1) # set timeout

        result = s.connect_ex((target, port)) # connect
        if result == 0:
            return port
        s.close()
    except socket.gaierror:
        return "ERROR: Hostname Could Not Be Resolved"
    except socket.error:
        return "ERROR: Server not responding"


addresses = ["142.250.186.174", "142.250.185.110"] # IP addresses to scan "on"
ports = [80, 22] # Ports to scan for
for addr in addresses:
    for port in ports:
        res = port_scan(addr, port)
        print(str(res) + "  |  " + addr)
