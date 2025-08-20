/*
Program: write_to_file.c
Author: Justin Garey
Description: Delete contents of a file and write a string to it.
Compiled against: gcc write_to_file.c --std=c99 && ./a.out
*/
#include <stdio.h>
#include <stdlib.h>

void write_string_to_file(const char *filename, const char *string_to_write) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    if (fputs(string_to_write, file) == EOF) {
        perror("Error writing to file");
        fclose(file);
        exit(EXIT_FAILURE);
    }

    if (fclose(file) != 0) {
        perror("Error closing file");
        exit(EXIT_FAILURE);
    }
}

int main() {
    const char *filename = "example.txt";
    const char *string_to_write = "This is the new content of the file.";

    write_string_to_file(filename, string_to_write);

    printf("Successfully wrote to the file: %s\n", filename);
    return 0;
}