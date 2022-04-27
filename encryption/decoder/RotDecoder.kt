package decoder

class RotDecoder {
    companion object {
        private const val alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!§$%&/()=?"


        fun RotDecode(stringIn: String, offset: Int): String {
            val stringOut = StringBuilder()
            for (i in stringIn.indices) {
                try {
                    var index: Int = alphabet.indexOf(stringIn[i]) - offset

                    if (index > alphabet.length) {
                        index += alphabet.length
                    }
                    if (stringIn[i] != ' ') {
                        stringOut.append(alphabet[index])
                    } else {
                        stringOut.append(" ")
                    }
                } catch (e: Exception) {
                    stringOut.append(stringIn[i])
                }
            }
            return stringOut.toString()
        }
    }
}
