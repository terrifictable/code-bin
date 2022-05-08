class XOR:
    def __init__(self) -> None:
        pass

    def _getHexChar(self, inp: str) -> str:
        char = hex(ord(inp))
        char = "0x" + char[2:len(char)].upper()
        return char

    def _str_hex(inp: str) -> hex:
        return int(inp, 16)



    def encode(inp: list, xor: hex) -> str:
        result = ""
        for char in inp:
            try:
                result += chr(int(char, 16) ^ xor)
            except ValueError:
                pass
        return result

    def decode(inp: list, xor: hex) -> str:
        result = ""
        for char in inp:
            try:
                result += chr(int(char, 16) ^ xor)
            except ValueError:
                pass

        return result

xor: XOR = XOR
res = xor.encode("0x41", 0x2E)
print(xor.decode("0x6f", 0x2E))
