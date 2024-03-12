#include <stdio.h>
#include <stdlib.h>


#define LEN 32 // 256 bits


void char_to_hex(unsigned char *key, char *hex) {
    for (int i = 0; i < LEN; i++) {
        sprintf(hex + 2*i, "%02x", key[i]);
    }
}

int main() {
    unsigned char *key = (unsigned char *) malloc(sizeof(unsigned char)*LEN);
    FILE* random = fopen("/dev/urandom", "r");
    fread(key, sizeof(unsigned char) * LEN, 1, random);
    fclose(random);

    char hex[2 * LEN + 1];
    char_to_hex(key, hex);

    printf("%s\n", hex);
    

    return 0;
}