

if __name__ == "__main__":
    chiphertext_correct = ["y", "t", "n", "v", "u", "p"]
    correct             = ["T", "H", "E", "A", "N", "D"]
    chiphertext_gram1_freq = ["x", "q", "m", "h", "i", "a", "c", "z", "l", "g", "b", "r", "e", "d", "f", "s", "k", "j", "o", "w"]
    gram1_freq             = ["O", "I", "S", "R", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "X", "J", "Q", "Z"]


    correct_mapping = {}
    for i in range(len(chiphertext_correct)):
        correct_mapping[chiphertext_correct[i]] = correct[i]

    gram1_mapping = {}
    for i in range(len(gram1_freq)):
        gram1_mapping[chiphertext_gram1_freq[i]] = gram1_freq[i]
    


    with open('ciphertext.txt') as f:
        with open('plaintext_sub.txt', 'w') as out:
            text = f.read()
            for i in range(len(text)):
                if text[i] in chiphertext_correct:
                    out.write(correct_mapping[text[i]])
                elif text[i] in chiphertext_gram1_freq:
                    out.write(gram1_mapping[text[i]])
                else:
                    out.write(text[i])


                        


