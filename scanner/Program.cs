using System;

namespace scanner
{
    class Program
    {
        static void Main(string[] args)
        {
            string host;
            int portStart;
            int portStop;
            int Threads;

            string ip;
            Console.Write("IP/Domain >>> ");
            ip = Console.ReadLine();
            Console.WriteLine();
            host = ip;

            string startPort;
            Console.Write("Start on Port >>> ");
            startPort = Console.ReadLine();

            Console.WriteLine();

            int number;
            bool resStart = Int32.TryParse(startPort, out number);

            if (resStart) {
                portStart = int.Parse(startPort);
            } else {
                Console.WriteLine("Invalid Input");
                return;
            }


            string endPort;
            Console.Write("Last Port (max: 65535) >>> ");
            endPort = Console.ReadLine();
            Console.WriteLine();

            int number1;
            bool resEnd = Int32.TryParse(endPort, out number1);

            if (resEnd) {
                portStop = int.Parse(endPort);
            } else {
                Console.WriteLine("Invalid Input");
                return;
            }


            string threadsToRun;
            Console.Write("Amount of Thready >>> ");
            threadsToRun = Console.ReadLine();
            Console.WriteLine();

            int number2;
            bool resThreads = Int32.TryParse(threadsToRun, out number2);

            if (resThreads) {
                Threads = int.Parse(threadsToRun);
            } else {
                Console.WriteLine("Invalid Input");
                return;
            }

            if (resStart == true && resEnd == true) {
                try {
                    portStart = int.Parse(startPort);
                    portStop = int.Parse(endPort);
                } catch { return; }
            }

            if (resThreads == true) {
                try {
                    Threads = int.Parse(threadsToRun);
                } catch { return; }
            }

            PortScanner ps = new PortScanner(host, portStart, portStop);
            ps.start(Threads);
        }
    }
}
