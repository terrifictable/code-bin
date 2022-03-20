import base64 as b64


def xor_enc(string, key):
    lkey = len(key)
    secret = []
    num = 0
    for each in string:
        if num >= lkey:
            num = num % lkey
        secret.append(chr(ord(each) ^ ord(key[num])))
        num += 1

    return b64.b64encode("".join(secret).encode()).decode()


def xor_dec(string, key):
    leter = b64.b64decode(string.encode()).decode()
    lkey = len(key)
    string = []
    num = 0
    for each in leter:
        if num >= lkey:
            num = num % lkey
        string.append(chr(ord(each) ^ ord(key[num])))
        num += 1

    return "".join(string)


encoded = xor_enc("Hello", "abc")
print("Encoded (key: abc): " + encoded)
print("Decoded (key: abc): " + xor_dec(encoded, "abc"))
