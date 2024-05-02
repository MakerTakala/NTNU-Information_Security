

if __name__ == "__main__":
    chiphertext_gram1_freq = ["n", "y", "v", "x", "u", "q", "m", "h", "t", "i", "p", "a", "c", "z", "l", "g", "b", "r", "e", "d", "f", "s", "k", "j", "o", "w"]
    gram1_freq             = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "X", "J", "Q", "Z"]
    chiphertext_gram2_freq = ["yt", "tn", "mu", "nh", "vh", "hn", "vu", "nq", "xu", "up", "xh", "yn", "np", "vy", "nu", "qy", "vq", "vi", "gn", "av", "my", "xz", "ym", "yx", "mq", "tv", "qn", "ur"]
    gram2_freq             = ["TH", "OF", "IO", "HE", "ED", "LE", "IN", "IS", "VE", "ER", "IT", "CO", "AN", "AL", "ME", "RE", "AR", "DE", "ON", "ST", "HI", "AT", "TO", "RI", "EN", "NT", "RO", "ND"]
    chiphertext_gram3_freq = ["ytn", "vup", "mur", "ynh", "xzy", "mxu", "gnq", "ytv", "nqy", "vii", "bxh", "lvq", "nuy", "vyn", "uvy", "lmu"]
    gram3_freq             = ["THE", "AND", "THA", "ENT", "ING", "ION", "TIO", "FOR", "NDE", "HAS", "NCE", "EDT", "TIS", "OFT", "STH", "MEN"]


    gram1_mapping = {}
    for i in range(len(gram1_freq)):
        gram1_mapping[chiphertext_gram1_freq[i]] = gram1_freq[i]
    gram2_mapping = {}
    for i in range(len(gram2_freq)):
        gram2_mapping[chiphertext_gram2_freq[i]] = gram2_freq[i]
    gram3_mapping = {}
    for i in range(len(gram3_freq)):
        gram3_mapping[chiphertext_gram3_freq[i]] = gram3_freq[i]

    with open('ciphertext.txt') as f:
        with open('plaintext_gram3.txt', 'w') as out:
            text = f.read()
            i = 0
            while i < len(text):
                if i+2 < len(text) and text[i:i+3] in gram3_mapping:
                    out.write(gram3_mapping[text[i:i+3]])
                    i += 3
                elif i+1 < len(text) and text[i:i+2] in gram2_mapping:
                    out.write(gram2_mapping[text[i:i+2]])
                    i += 2
                elif text[i] in gram1_mapping:
                    out.write(gram1_mapping[text[i]])
                    i += 1
                else:
                    out.write(text[i])
                    i += 1

                        


