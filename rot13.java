import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Rot13 {
    private static String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";


    public static void main(String[] args) throws IOException {
        BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));
        String error, option;
        System.out.print("\n=== Rot13 ===\n > Encode | 1\n > Decode | 2\n>>> ");

        try {
            option = scanner.readLine();
            error = "";
        } catch (Exception e) {
            option = "";
            error = e.getMessage();
        }

        if (option.equals("")) {
            System.out.println("Invalid Input");
            if (!error.equals("")) {
                System.out.println("Error: "+ error);
            }
            System.exit(1);
        }

        if (option.equals("1")) {
            System.out.print("String > ");
            String input = scanner.readLine();

            System.out.println("Encoded: " + encode(input));

        } else if (option.equals("2")) {
            System.out.print("String > ");
            String encoded_input = scanner.readLine();

            System.out.println("Decoded: " + decode(encoded_input));

        } else {
            System.out.println("Invalid Input: " + option);
            System.exit(1);
        }

        System.exit(0);
    }

    public static String encode(String input) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            try {
                int index = alphabet.indexOf(input.charAt(i)) + 13;

                if (index > alphabet.length()) {
                    index = index - alphabet.length();
                }

                // add spaces to result
                if (input.charAt(i) != ' ') {
                    result.append(alphabet.charAt(index));
                } else {
                    result.append(" ");
                }
            } catch (Exception e) {
                result.append(input.charAt(i));
            }
        }

        return result.toString();
    }

    public static String decode(String input) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            try {
                int index = alphabet.indexOf(input.charAt(i)) - 13;

                if (index > alphabet.length()) {
                    index = index + alphabet.length();
                }

                // add spaces to result
                if (input.charAt(i) != ' ') {
                    result.append(alphabet.charAt(index));
                } else {
                    result.append(" ");
                }
            } catch (Exception e) {
                result.append(input.charAt(i));
            }
        }

        return result.toString();
    }
}
