class Rot13:
    def __init__(self):
        self.alphabet = ["A", "B", "C", "D", "E", "F",  "G", "H", "I", "J", "K", "L", "M",
                         "N", "O", "P", "Q",  "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                         "a", "b", "c", "d", "e", "f",  "g", "h", "i", "j", "k", "l", "m",
                         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def encode(self, string):
        result = []
        for char in string:
            try:
                index = self.alphabet.index(char)+13
                if index > len(self.alphabet):
                    index = index-len(self.alphabet)
                result.append(self.alphabet[index])
            except:
                result.append(char)
        return "".join(result)

    def decode(self, string):
        result = []
        for char in string:
            try:
                index = self.alphabet.index(char)-13
                if index > len(self.alphabet):
                    index = index+len(self.alphabet)
                result.append(self.alphabet[index])
            except:
                result.append(char)
        return "".join(result)


rot13 = Rot13()
encode = rot13.encode("Hello World!")
decode = rot13.decode(encode)

print(encode)
print(decode)
