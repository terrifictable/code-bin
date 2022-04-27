package decoder

import java.util.*

class Base64Decoder {
    companion object {
        fun Base64Decode(stringIn: String?): String? {
            val decoder: Base64.Decoder = Base64.getDecoder()
            return String(decoder.decode(stringIn))
        }

        fun Base64RotDecode(stringIn: String?, rotOffset: Int): String {
            val stringOut: String? = Base64Decode(stringIn)
            return RotDecoder.RotDecode(stringOut.toString(), rotOffset)
        }
    }
}
