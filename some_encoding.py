from random import Random


def gen_bytes_for_seed(seed: int, message: str) -> bytearray:
    data = Random(seed)
    garbage = Random(seed*2)

    res = bytearray()
    data.seed(seed)
    i = 0
    while i < len(message):
        m = message[i]
        if data.randrange(2):
            res.append(ord(m) ^ data.randrange(256))
            i += 1
        else:
            res.append(garbage.randrange(256))
    return res


def str_from_bytearray(seed: int, arr: bytearray) -> str:
    import random

    random.seed(seed)
    return(''.join(
        chr(random.randrange(256) ^ c)
        for c in bytes.fromhex(str(arr))
        if random.randrange(2)
    ))


seed = 69422
message = "Abend"


print(f"""
import random
random.seed({seed})
print(''.join(
        chr(random.randrange(256) ^ c)
        for c in bytes.fromhex({repr(gen_bytes_for_seed(seed, message).hex().upper())})
        if random.randrange(2)
))""")
