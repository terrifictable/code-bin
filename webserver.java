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

    public static int get_views(File file, Scanner s) {
        boolean data_found = false;

        try {
            s = new Scanner(file);
            while (s.hasNextLine() && !data_found) {
                String line = s.nextLine();
                if (line.contains("views:")) {
                    data_found = true;
                    views = convert(line.replace("views:", ""));
                }
            }
        } catch (Exception e) {
            System.out.println("Error reading views file: " + e.getMessage());
        }
        return views;
    }

    public static void update_views(File file, Scanner s) {
        try {
            int views = get_views(file, s);
            try (FileWriter filewrite = new FileWriter("views.txt")) {
                filewrite.write("views:" + String.valueOf(views + 1));
            }

        } catch (Exception e) {
            System.out.println("Error writing views file: " + e.getMessage());
        }
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            File file = new File("./views.txt");
            Scanner s = null;
            update_views(file, s);
            int views = get_views(file, s);

            String response = String.valueOf(views);

            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
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
