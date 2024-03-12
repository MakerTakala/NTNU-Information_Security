from Crypto.Cipher import AES


plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
init_vector = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")
ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")


def main():
    with open("key.txt", "r") as f:
        keys = f.readlines()
    
    for key in keys:
        key = bytes.fromhex(key.strip())
        cipher = AES.new(key, AES.MODE_CBC, init_vector)
        encrypted_text = cipher.encrypt(plaintext)
        

        if ciphertext == encrypted_text:
            print("Key found!")
            print("Key: " + key.hex())
            print("Encrypted: " + encrypted_text.hex())

main()