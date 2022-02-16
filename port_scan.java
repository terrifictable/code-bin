import java.io.*;
import java.net.*;
import java.util.*;

class NewClass {
    public static void sendPingRequest(String ipAddress, int port, int timeout)
            throws UnknownHostException, IOException {
        InetAddress ping = InetAddress.getByName(ipAddress);
        if (ping.isReachable(timeout) && portIsOpen(ipAddress, port, timeout))
            System.out.println(port + "   |   " + ipAddress + "   |   Valid");
        else
            System.out.println(port + "   |   " + ipAddress + "   |   Invalid");
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
            if (args.length < 1) {
                System.out.println("usage: java .java IP PORT [-d]");
                System.exit(1);
            }
            String ipAddress = args[0];
            int port = Integer.parseInt(args[1]);

            sendPingRequest(ipAddress, port, 5000);
        } catch (Exception e) {
            System.out.println("usage: java .java IP PORT [-d]");
            if (Arrays.asList(args).contains("-d")) {
                System.out.println("\n ---- DEBUG ---- \n" + e);
            }
            System.exit(1);
        }
    }
}
