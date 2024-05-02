

if __name__ == "__main__":
    chiphertext_gram1_freq = ["n", "y", "v", "x", "u", "q", "m", "h", "t", "i", "p", "a", "c", "z", "l", "g", "b", "r", "e", "d", "f", "s", "k", "j", "o", "w"]
    gram1_freq             = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "X", "J", "Q", "Z"]

    gram1_mapping = {}
    for i in range(len(gram1_freq)):
        gram1_mapping[chiphertext_gram1_freq[i]] = gram1_freq[i]
    gram2_mapping = {}


    with open('ciphertext.txt') as f:
        with open('plaintext_gram1.txt', 'w') as out:
            text = f.read()
            for i in range(len(text)):
                if text[i] in gram1_mapping:
                    out.write(gram1_mapping[text[i]])
                else:
                    out.write(text[i])

                        


