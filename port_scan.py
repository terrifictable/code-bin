import os
import socket
import sys


def port_scan(address, port):
    try:
        target = socket.gethostbyname(address)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            return port  # if port != None or port != "None" else "None"
        else:
            s.close()
            return "None"
    except socket.gaierror:
        return "ERROR: Hostname Could Not Be Resolved"
    except socket.error:
        return "ERROR: Server not responding"


ports = [80]
if "-h" in sys.argv:
    sys.exit(__file__.split("\\")[-1] + " ip [-p port] [-h]")
elif len(sys.argv) > 1:
    addresses = sys.argv[1].split(",")
    if "-p" in sys.argv:
        ports = sys.argv[3].split(",")
else:
    sys.exit(__file__.split("\\")[-1] + " ip [-p port] [-h]")

for addr in addresses:
    for port in ports:
        res = port_scan(addr, int(port))
        space = " "*(8-len(str(res)))
        print(str(res) + space + "|  " + addr)
