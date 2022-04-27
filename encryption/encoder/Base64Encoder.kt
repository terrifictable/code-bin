package encoder

import java.util.*

class Base64Encoder {
    companion object {
        fun Base64Encode(stringIn: String): String {
            val encoder = Base64.getEncoder()
            return encoder.encodeToString(stringIn.toByteArray())
        }

        fun Base64RotEncode(stringIn: String, rotOffset: Int): String {
            val stringOut: String = RotEncoder.RotEncode(stringIn, rotOffset)
            return Base64Encode(stringOut)
        }
    }
}
