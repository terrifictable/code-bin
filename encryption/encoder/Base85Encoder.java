package encoder;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.regex.Pattern;

public class Base85Encoder {
    private final static int ASCII_SHIFT = 33;
    private static int[] BASE85_PW = {
            1,
            85,
            85 * 85,
            85 * 85 * 85,
            85 * 85 * 85 * 85
    };
    private static Pattern REMOVE_WHITESPACE = Pattern.compile("\\s+");


    public static String Base85Encode(String stringIn) {
        byte[] in = stringIn.getBytes();

        if (in == null) { throw new IllegalArgumentException("null value"); }

        StringBuffer stringBuffer = new StringBuffer(in.length * 5 / 4);
        byte[] chunk = new byte[4];
        int chunkIndex = 0;

        for (int i=0; i < in.length; i++) {

            byte currByte = in[i];

            chunk[chunkIndex++] = currByte;

            if (chunkIndex == 4) {
                int value = byteToInt(chunk);

                if (value == 0) {
                    stringBuffer.append("z");
                } else {
                    stringBuffer.append(encodeChunk(value));
                }
                Arrays.fill(chunk, (byte) 0);
                chunkIndex = 0;
            }
        }

        if (chunkIndex > 0) {
            int numPadded = chunk.length - chunkIndex;
            Arrays.fill(chunk, chunkIndex, chunk.length, (byte) 0);
            int value = byteToInt(chunk);
            char[] encodedChunk = encodeChunk(value);
            for (int i=0; i < encodedChunk.length - numPadded; i++) {
                stringBuffer.append(encodedChunk[i]);
            }
        }

        return stringBuffer.toString();
    }

    public static String Base85_64Encoder(String stringIn) {
        String base85Encoded = Base85Encode(stringIn);
        String base64Encoded = Base64Encoder.Companion.Base64Encode(base85Encoded);

        return base64Encoded;
    }
    




    private static int byteToInt(byte[] value) {
        if (value == null || value.length != 4) { throw new IllegalArgumentException("value not 4 bytes long"); }

        return ByteBuffer.wrap(value).getInt();
    }

    private static char[] encodeChunk(int value) {
        long longVal = value & 0x00000000ffffffffL;
        char[] encodedChunk = new char[5];
        for (int i=0; i < encodedChunk.length; i++) {
            encodedChunk[i] = (char) ((longVal / BASE85_PW[4 - i]) + ASCII_SHIFT);
            longVal = longVal % BASE85_PW[4 - i];
        }
        return encodedChunk;
    }
}
