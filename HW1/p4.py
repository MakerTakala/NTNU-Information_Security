def main():
    ori_encryption = bytes.fromhex("49913FF7731C1E74510611018BE35110495CCAA7")
    ori_message =  bytes("I love cryptography.", 'ascii')
    new_message = bytes("I hate cryptography.", 'ascii')

    key = xor_bytes(ori_encryption, ori_message)
    print("Key:", key.hex())
    new_chiphertext = xor_bytes(new_message, key).hex()
    print("New Encryption:", new_chiphertext)


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


main()
