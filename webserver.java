import java.io.*;
import java.net.*;
import java.util.*;

import com.sun.net.httpserver.*;

public class webserver {
    public static int views;

    public static void main(String[] args) throws Exception {
        int PORT = 8000;

        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);
        System.out.println("Server running on: http://localhost:" + PORT);

        server.createContext("/", new MyHandler());
        server.setExecutor(null); // creates a default executor
        server.start();
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            System.out.println("\n[HANDLER]: Start");
            File file = new File("./views.txt");
            Scanner s = null;
            int views = get_views(file, s);

            String response = "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8' /><title>Views</title><style>#views { font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; padding: 15px; margin: 15px, 10, auto; }</style></head><body><h1 id='views'>Views: "
                    + String.valueOf(views) + "</h1></body></html>";
            update_views(file, s, views);

            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }

    public static int get_views(File file, Scanner s) {
        boolean data_found = false;

        try {
            s = new Scanner(file);
            while (s.hasNextLine() && !data_found) {
                String line = s.nextLine();
                if (line.contains("views:")) {
                    data_found = true;
                    views = convert(line.replace("views:", ""));
                    System.out.println("[GET-ViewCount]: " + String.valueOf(views));
                }
            }
        } catch (Exception e) {
            System.out.println("Error reading views file: " + e.getMessage());
        }
        return views;
    }

    public static void update_views(File file, Scanner s, int views) {
        try {
            System.out.println("[UPDATE-ViewCount]: " + String.valueOf(views));
            try (FileWriter filewrite = new FileWriter("views.txt")) {
                filewrite.write("views:" + String.valueOf(views + 1));
            }

        } catch (Exception e) {
            System.out.println("Error writing views file: " + e.getMessage());
        }
    }

    public static int convert(String str) {
        int val = 0;

        try {
            val = Integer.parseInt(str);
        } catch (NumberFormatException e) {
            System.out.println("Error while converting str to int: " + e.getMessage());
        }
        return val;
    }

}
