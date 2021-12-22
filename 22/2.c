#include<stdlib.h>
#include<stdio.h>
#include<string.h>

#define print printf
#define xstep 77
#define ystep 1662
#define zstep 811

static int block_size = xstep * ystep * zstep;

void set(char* block, int x, int y, int z, char value) {
        block[x + 77 * y + 77 * 1662 * z] = value;
}

void reset(char* block) {
        memset(block, 0, block_size);
}

int main() {
        FILE* file = fopen("input", "r");
        char* buffer = malloc(1);
        int step = 1;
        int read = 0;
        do {
                new_buffer = malloc(step * 64);
                memcpy(
                buffer = realloc(buffer, step * 64);
                read = fread(buffer + 64 * (step++ - 1), 64, 1, file);
        } while (read == 1);
        fclose(file); // Forgetting to close the file will fuck shit up for reasons which I am presently unaware
        print("%s\n", buffer);
        int line_start = 0;
        int line_end = 0;
        while (line_end <= strlen(buffer)) {
                while (buffer[line_end] != '\n' || buffer[line_end] != 0) {
                        line_end++;
                        print("here %s\n", buffer[line_end]);
                }
                int command;
                sscanf(buffer + line_start, "%d", command);
                print("%d\n", command);
                line_start = line_end;
        }
        char* my_block = (char*)malloc(block_size);
        set(my_block, 76, 1661, 810, 1);
        reset(my_block);
        print("Done\n");
}
