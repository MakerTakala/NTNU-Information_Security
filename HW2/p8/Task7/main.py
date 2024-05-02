import Crypto.Cipher.AES as AES
import Crypto.Util.Padding as Padding

if __name__ == "__main__":
    plaintext = bytes("This is a top secret.", "ascii")
    ciphertext = bytes.fromhex("764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2")
    initial_vector = bytes.fromhex("aabbccddeeff00998877665544332211")

    with open("words.txt", "r") as f:
        for word in f.readlines():
            word = word.strip()
            if len(word) > 16:
                continue

            key = word + '#' * (16 - len(word))
            key = bytes(key, "ascii")
            cipher = AES.new(key, AES.MODE_CBC, initial_vector)
            result = cipher.encrypt(Padding.pad(plaintext, 16))
            if result == ciphertext:
                print(f"Key: {key.decode('ascii')}")
                break
