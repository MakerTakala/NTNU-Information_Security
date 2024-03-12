from p6_text import *
THRESHOLD = 7

def main():
    
    ciphertexts = [bytes.fromhex(ciphertext_hextext.replace(" ", "")) for ciphertext_hextext in ciphertexts_hextexts]
    challenge_ciphertext = bytes.fromhex(challenge_ciphertext_hextext)

    part_key = [0] * max(len(x) for x in ciphertexts)
    
    for ciphertext1 in ciphertexts:
        xor_results = []
        for ciphertext2 in ciphertexts:
            if ciphertext1 != ciphertext2:
                xor_results.append(xor_bytes(ciphertext1, ciphertext2))

        
        for i, ciphertext in enumerate(ciphertext1):
            vaild = 0
            for xor_result in xor_results:
                if i < len(xor_result) and is_text(xor_result[i]):
                    vaild += 1
            if vaild >= THRESHOLD:
                part_key[i] = ciphertext ^ ord(" ")

    decode_message = ""
    for i, ciphertext in enumerate(challenge_ciphertext):
        if part_key[i] == 0:
            decode_message += "_"
        else:
            decode_message += chr(ciphertext ^ part_key[i])
    print(decode_message)


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def is_text(c):
    return c == 0 or (ord("A") <= c <= ord("Z")) or (ord("a") <= c <= ord("z"))
        

main()