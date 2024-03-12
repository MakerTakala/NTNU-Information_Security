#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define KEYSIZE 16
#define START 1524013729
#define END 1524020929
#define FILE_NAME "key.txt"

void generate_key(FILE* file, time_t seed){
    char key[KEYSIZE];
    srand (seed);
    for (int i = 0; i < KEYSIZE; i++){
        key[i] = rand() % 256;
        fprintf(file, "%02x", key[i]);
    }
    
    fprintf(file, "\n");
}

int main() {

    FILE* file = fopen(FILE_NAME, "w");
    if (file == NULL){
        printf("Error opening file\n");
        return 1;
    }

    for (long i = START; i <= END; i++){
        generate_key(file, i);
    }
    fclose(file);
    return 0;
   
}