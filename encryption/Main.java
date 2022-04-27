import decoder.*;
import encoder.*;

public class Main {
    public static void main(String[] args) {
        String encodedRot = RotEncoder.Companion.RotEncode("Hello World!", 18);
        String decodedRot = RotDecoder.Companion.RotDecode(encodedRot, 18);


        String encoded64 = Base64Encoder.Companion.Base64Encode("Hello World!");
        String decoded64 = Base64Decoder.Companion.Base64Decode(encoded64);

        String encoded64_Rot = Base64Encoder.Companion.Base64RotEncode("Hello World!", 18);
        String decoded64_Rot = Base64Decoder.Companion.Base64RotDecode(encoded64_Rot, 18);


        String encoded85 = Base85Encoder.Base85Encode("Hello World!");
        String decoded85 = Base85Decoder.Base85Decode(encoded85);

        String encoded85_64 = Base85Encoder.Base85_64Encoder("Hello World!");
        String decoded85_64 = Base85Decoder.Base85_64Decode(encoded85_64);


        System.out.println("=== ROT ===");
        System.out.println(encodedRot);
        System.out.println(decodedRot);
        System.out.println("=== ROT ===\n");

        System.out.println("=== BASE64 ===");
        System.out.println(encoded64);
        System.out.println(decoded64);
        System.out.println(" == rot ==");
        System.out.println(encoded64_Rot);
        System.out.println(decoded64_Rot);
        System.out.println("=== BASE64 ===\n");

        System.out.println("=== BASE85 ===");
        System.out.println(encoded85);
        System.out.println(decoded85);
        System.out.println(" == 85_64 ==");
        System.out.println(encoded85_64);
        System.out.println(decoded85_64);
        System.out.println("=== BASE85 ===\n");
    }
}
