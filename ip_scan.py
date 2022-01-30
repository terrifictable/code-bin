import random
import threading
import socket


def scan(length):
    for i in range(length):
        p1, p2, p3, p4 = random.randrange(0, 255, 1), \
            random.randrange(0, 255, 1), \
            random.randrange(0, 255, 1), \
            random.randrange(0, 255, 1)
        ip_addr = f'{p1}.{p2}.{p3}.{p4}'
        print("\r" + ip_addr, end="\r")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        try:
            sock.connect((ip_addr, 22))
            print("\nFound working addres: " + ip_addr + "\n")
            with open("./addresses.txt", "a") as f:
                f.write(ip_addr + ":22")
        except:
            pass


threads = []
for i in range(5):
    thread = threading.Thread(target=scan, args=(100,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
