import socket
from binascii import hexlify, unhexlify

def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

class PaddingOracle:

    def __init__(self, host, port) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

        ciphertext = self.s.recv(4096).decode().strip()
        self.ctext = unhexlify(ciphertext)

    def decrypt(self, ctext: bytes) -> None:
        self._send(hexlify(ctext))
        return self._recv()

    def _recv(self):
        resp = self.s.recv(4096).decode().strip()
        return resp 

    def _send(self, hexstr: bytes):
        self.s.send(hexstr + b'\n')

    def __del__(self):
        self.s.close()

def decrypt_block(pre_cipher, cur_cipher):
    D = bytearray(16)
    C = bytearray(16)

    for i in range(16):
        D[i] = pre_cipher[i]
        C[i] = 0x00

    print()
    for K in range(1, 17):
        for i in range(256):
            C[16 - K] = i
            status = oracle.decrypt(C + cur_cipher)
            if status == "Valid":
                D[16 - K] = i ^ K
                print("K = " + str(K))
                print("Valid: i = 0x{:02x}".format(i))
                print("C: " + C.hex())
                for j in range(K):
                    C[16 - K + j] = (K + 1) ^ D[16 - K + j]
                print("D: " + D.hex())
                print()
                break

    return xor(pre_cipher, D)


if __name__ == "__main__":
    oracle = PaddingOracle('10.9.0.80', 5000)

    # Get the IV + Ciphertext from the oracle
    iv_and_ctext = bytearray(oracle.ctext)

    ciphertext = []
    for i in range(0, len(iv_and_ctext), 16):
        ciphertext.append(iv_and_ctext[i:i+16])
    
    plaintext = []
    for i in range(1, len(ciphertext)):
        P = decrypt_block(ciphertext[i - 1], ciphertext[i])
        plaintext.append(P)
        print("P" + str(i) + ":  " + P.hex())
        print("P" + str(i) + ":  " + P.decode("ascii"))
        print()


    print("Plain Text(HEX): ", end="")
    for i in range(len(plaintext)):
        print(plaintext[i].hex(), end="")
    print()
    print("Plain Text(ASCII): ", end="")
    for i in range(len(plaintext)):
        print(plaintext[i].decode("ascii"), end="")
    print()
    
