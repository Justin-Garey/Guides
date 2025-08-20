/*
Program: get_process_start_time.c
Author: Justin Garey
Description: Get the process start time using the get_process_id function
             and the ps command. The get_process_id function comes from another
             file.
Compiled against: gcc get_process_start_time.c --std=c99 && ./a.out
*/

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

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

int get_process_uptime(const char *process_id, char *process_uptime)
{
    char command[256];
    snprintf(command, sizeof(command), "ps -o etime= -p %s", process_id);

    // Execute
    FILE *fp = popen(command, "r");
    if (fp == NULL)
    {
        perror("command failed");
        return 1;
    }

    if (fgets(process_uptime, 256, fp) == NULL)
    {
        printf("Failed to retrieve process uptime\n");
        pclose(fp);
        return 2;
    }
    pclose(fp);

    size_t len = strlen(process_uptime);
    if (len > 0 && process_uptime[len - 1] == '\n')
    {
        process_uptime[len - 1] = '\0';
    }

    //printf("Process uptime: %s\n", process_uptime);

    // Convert to seconds
    int days = 0, hours = 0, minutes = 0, seconds = 0;
    if (strchr(process_uptime, '-')) // Days
    {
        sscanf(process_uptime, "%d-%d:%d:%d", &days, &hours, &minutes, &seconds);
    }
    else if (strchr(process_uptime, ':') && strchr(process_uptime, ':') != strrchr(process_uptime, ':')) // Hours
    {
        sscanf(process_uptime, "%d:%d:%d", &hours, &minutes, &seconds);
    }
    else // Only minutes and seconds
    {
        sscanf(process_uptime, "%d:%d", &minutes, &seconds);
    }

    snprintf(process_uptime, 256, "%d", days * 86400 + hours * 3600 + minutes * 60 + seconds);

    return 0;
}

int main()
{
    const char *process_name = "htop";
    char process_id[64] = {0};
    char process_uptime[256] = {0};

    if (get_process_id(process_name, process_id) == 0)
    {
        printf("Process ID: %s\n", process_id);
        get_process_uptime(process_id, process_uptime);
        printf("Process Uptime: %s seconds\n", process_uptime);
    }

    return 0;
}