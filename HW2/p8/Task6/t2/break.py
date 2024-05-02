

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

if __name__ == "__main__":
    P1 = bytes("This is a known message!", "ascii")
    C1 = bytes.fromhex("a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159")
    C2 = bytes.fromhex("bf73bcd3509299d566c35b5d450337e1bb175f903fafc159")

    P2 = xor_bytes(xor_bytes(C1, P1), C2)
    print(bytes.decode(P2, "ascii"))