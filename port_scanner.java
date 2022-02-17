import java.io.*;
import java.net.*;
import java.util.*;

class port_scan {
    public static void sendPingRequest(String ipAddress, int port, int timeout)
            throws UnknownHostException, IOException {
        InetAddress ping = InetAddress.getByName(ipAddress);

        if (ping.isReachable(timeout) && portIsOpen(ipAddress, port, timeout))
            System.out.print("\r\033[92m" + port + "   |   " + ipAddress + "   |   Valid\n");
        else
            System.out.print("\r\033[93m" + port + "   |   " + ipAddress + "   |   Invalid\r");
    }

    private static boolean portIsOpen(String ip, int port, int timeout) {
        try {
            Socket socket = new Socket();
            socket.connect(new InetSocketAddress(ip, port), timeout);
            socket.close();
            return true;
        } catch (Exception ex) {
            return false;
        }
    }

    public static void main(String[] args) throws UnknownHostException, IOException {
        try {
            if (args.length < 2) {
                System.out.println("usage: java port_scan.java IP PORTSTART PORTEND [-d]");
                System.exit(1);
            }
            String ipAddress = args[0];
            for (int i = Integer.parseInt(args[1]); i < Integer.parseInt(args[2]); i++) {
                int port = i;
                sendPingRequest(ipAddress, port, 1000);
            }
            System.out.println("\033[97m");
        } catch (Exception e) {
            System.out.println("usage: java port_scan.java IP PORTSTART PORTEND [-d]");
            if (Arrays.asList(args).contains("-d")) {
                System.out.println("\n ---- DEBUG ---- \n" + e);
            }
            System.exit(1);
        }
    }
}
// USAGE: java port_scan.java 127.0.0.1 1 65000 [-d]
