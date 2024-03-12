#include <stdio.h>
#include <stdlib.h>


int main() {
    FILE* out = fopen("./test/data.Crandom", "w");
   
    srand(0);


    for (int i = 0; i < 1040000; i++) {
        char c = rand() % 2;
        fprintf(out, "%c", c + '0');
    }
    
}

