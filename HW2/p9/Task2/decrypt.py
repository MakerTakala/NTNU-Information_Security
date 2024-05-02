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


if __name__ == "__main__":
    oracle = PaddingOracle('10.9.0.80', 6000)

    # Get the IV + Ciphertext from the oracle
    iv_and_ctext = bytearray(oracle.ctext)
    IV    = iv_and_ctext[00:16]
    C1    = iv_and_ctext[16:32]  # 1st block of ciphertext
    C2    = iv_and_ctext[32:48]  # 2nd block of ciphertext
    print("C1:  " + C1.hex())
    print("C2:  " + C2.hex())

    D2 = bytearray(16)
    D1 = bytearray(16)
    CC1 = bytearray(16)
    CIV = bytearray(16)

    for i in range(16):
        D2[i] = C1[i]
        D1[i] = IV[i]
        CC1[i] = 0x00
        CIV[i] = 0x00

    print()
    for K in range(1, 17):
        for i in range(256):
            CC1[16 - K] = i
            status = oracle.decrypt(CC1 + C2)
            if status == "Valid":
                D2[16 - K] = i ^ K
                print("K = " + str(K))
                print("Valid: i = 0x{:02x}".format(i))
                print("CC1: " + CC1.hex())
                for j in range(K):
                    CC1[16 - K + j] = (K + 1) ^ D2[16 - K + j]
                print("D2: " + D2.hex())
                print()
                break
    P2 = xor(C1, D2)
    print("P2:  " + P2.hex())

    print()
    for K in range(1, 17):
        for i in range(256):
            CIV[16 - K] = i
            status = oracle.decrypt(CIV + C1)
            if status == "Valid":
                D1[16 - K] = i ^ K
                print("K = " + str(K))
                print("Valid: i = 0x{:02x}".format(i))
                print("CIV: " + CIV.hex())
                for j in range(K):
                    CIV[16 - K + j] = (K + 1) ^ D1[16 - K + j]
                print("D1: " + D1.hex())
                print()
                break
    P1 = xor(IV, D1)
    print("P1:  " + P1.hex())

    
