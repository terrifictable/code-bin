using System;
using System.Net.Sockets;
using System.Threading;

namespace scanner 
{
    class PortScanner
    {
        private string host;
        private PortList portList;
        
        public PortScanner(string host, int portStart, int portStop) {
            this.host = host;
            this.portList = new PortList(portStart, portStop);
        }

        public void start(int threadCounter) {
            for (int i = 0; i < threadCounter; i++) {
                Thread thread1 = new Thread(new ThreadStart(RunScanTcp));
                thread1.Start();
            }
        }

        public void RunScanTcp() {
            int port;
            TcpClient tcp = new TcpClient();

            while ((port = portList.NextPorts()) != -1) {
                Console.Title = "Current Port Count: " + port.ToString();

                try {
                    tcp = new TcpClient(host, port);
                } catch {
                    continue;
                } finally {
                    try {
                        tcp.Close();
                    } catch (Exception e) {
                        Console.WriteLine(e.Message);
                    }
                    Console.WriteLine("TCP Port {0} is open", port);
                }
            }
        }
    }
}