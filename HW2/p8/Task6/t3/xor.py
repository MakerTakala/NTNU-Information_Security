def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


if __name__ == "__main__":

    mes = bytes.fromhex("5965730d0d0d0d0d0d0d0d0d0d0d0d0d")
    IV0 = bytes.fromhex("a99e809f35c564fe3ff22a6fb7b3e5af")
    IV = bytes.fromhex("5aff7da935c564fe3ff22a6fb7b3e5af")

    m_ = xor_bytes(xor_bytes(IV0, mes), IV)
    print("M':", m_.hex())