package decoder;

import java.math.BigDecimal;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.regex.Pattern;

public class Base85Decoder {
    private final static int ASCII_SHIFT = 33;
    private static int[] BASE85_PW = {
            1,
            85,
            85 * 85,
            85 * 85 * 85,
            85 * 85 * 85 * 85
    };
    private static Pattern REMOVE_WHITESPACE = Pattern.compile("\\s+");


    public static String Base85Decode(String in) {
        if (in == null) { throw new IllegalArgumentException("null value"); }

        final int inputLength = in.length();
        long zCount = in.chars().filter(c -> c == 'z').count();

        BigDecimal uncompressedZLength = BigDecimal.valueOf(zCount).multiply(BigDecimal.valueOf(4));
        BigDecimal uncompressedNonZLength = BigDecimal.valueOf(inputLength - zCount)
                .multiply(BigDecimal.valueOf(4))
                .divide(BigDecimal.valueOf(5));
        BigDecimal uncompressedLength = uncompressedZLength.add(uncompressedNonZLength);
        ByteBuffer byteBuff = ByteBuffer.allocate(uncompressedLength.intValue());

        byte[] payload = in.getBytes(StandardCharsets.US_ASCII);
        byte[] chunk = new byte[5];

        int chunkIndex = 0;
        for (int i=0; i < payload.length; i++) {
            byte currByte = payload[i];

            if (currByte == 'z') {
                chunk[chunkIndex++] = '!';
                chunk[chunkIndex++] = '!';
                chunk[chunkIndex++] = '!';
                chunk[chunkIndex++] = '!';
                chunk[chunkIndex++] = '!';
            } else {
                chunk[chunkIndex++] = currByte;
            }

            if (chunkIndex == 5) {
                byteBuff.put(decodeChunk(chunk));
                Arrays.fill(chunk, (byte) 0);
                chunkIndex = 0;
            }
        }

        if (chunkIndex > 0) {
            int numPadded = chunk.length - chunkIndex;
            Arrays.fill(chunk, chunkIndex, chunk.length, (byte) 'u');
            byte[] paddedDecode = decodeChunk(chunk);
            for (int i=0; i < paddedDecode.length - numPadded; i++) {
                byteBuff.put(paddedDecode[i]);
            }
        }

        byteBuff.flip();
        return new String(Arrays.copyOf(byteBuff.array(), byteBuff.limit()));
    }

    public static String Base85_64Decode(String stringIn) {
        String base64Decoded = _Base64Decoder.Base64Decode(stringIn);
        String base85Decoded = Base85Decode(base64Decoded);

        return base85Decoded;
    }



    private static byte[] intToByte(int value) {
        return new byte[] {
                (byte) (value >>> 24),
                (byte) (value >>> 16),
                (byte) (value >>> 8),
                (byte) (value)
        };
    }

    private static byte[] decodeChunk(byte[] chunk) {
        if (chunk.length != 5) { throw new IllegalArgumentException("chunk size not 5"); }

        int value = 0;
        value += (chunk[0] - ASCII_SHIFT) * BASE85_PW[4];
        value += (chunk[1] - ASCII_SHIFT) * BASE85_PW[3];
        value += (chunk[2] - ASCII_SHIFT) * BASE85_PW[2];
        value += (chunk[3] - ASCII_SHIFT) * BASE85_PW[1];
        value += (chunk[4] - ASCII_SHIFT) * BASE85_PW[0];

        return intToByte(value);
    }
}
