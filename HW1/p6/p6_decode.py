from p6_text import *

def main():

    ciphertexts = [bytes.fromhex(ciphertext_hextext.replace(" ", "")) for ciphertext_hextext in ciphertexts_hextexts]
    challenge_ciphertext = bytes.fromhex(challenge_ciphertext_hextext)
    challenge_message = bytes(challenge_message_ascii, 'ascii')

    key = xor_bytes(challenge_ciphertext, challenge_message)
    print("Key:", key.hex())


    for ciphertext in ciphertexts:
        print(bytes.decode(xor_bytes(ciphertext, key), 'ascii'))

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


main()