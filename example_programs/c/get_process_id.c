/*
Program: get_process_id.c
Author: Justin Garey
Description: Get the process ID using the pidof command and the process name.
Compiled against: gcc get_process_id.c --std=c99 && ./a.out
*/

// Need the define to compile with c99
// https://narkive.com/vbALyAva:5.1332.19
#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_process_id(const char *process_name, char *process_id)
{
    char command[256];
    snprintf(command, sizeof(command), "pidof %s", process_name);

    // Execute
    FILE *fp = popen(command, "r");
    if (fp == NULL)
    {
        perror("pidof failed");
        return 1;
    }

    // Get the process ID
    if (fgets(process_id, 64, fp) == NULL)
    {
        printf("not found");
        pclose(fp);
        return 2;
    }
    pclose(fp);

    size_t len = strlen(process_id);
    if (len > 0 && process_id[len - 1] == '\n')
    {
        process_id[len - 1] = '\0';
    }

    return 0;
}

int main()
{
    const char *process_name = "htop";
    char process_id[64] = {0};
    get_process_id(process_name, process_id);
    printf("Process ID: %s\n", process_id);
    return 0;
}