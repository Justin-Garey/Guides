/*
Program: get_interface_ip.c
Author: Justin Garey
Description: Get the IPv4 address of a supplied network interface name.
Compiled against: gcc get_interface_ip.c --std=c99 && ./a.out
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <sys/socket.h>
#include <unistd.h>
#include <linux/if.h>
#include <arpa/inet.h>

int get_interface_ip(const char *interface_name, char *ip_string)
{
    struct ifreq ifr;
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1)
    {
        perror("Could not create socket");
        return 0;
    }

    // Set for IPv4 on the interface_name
    ifr.ifr_addr.sa_family = AF_INET;
    strncpy(ifr.ifr_name, interface_name, IFNAMSIZ - 1);

    // Get IP
    if (ioctl(sock, SIOCGIFADDR, &ifr) == -1)
    {
        perror("Could not acquire IP address");
        close(sock);
        return 0;
    }
    close(sock);

    // Copy the IP address from
    strncpy(ip_string, inet_ntoa(((struct sockaddr_in *)&ifr.ifr_addr)->sin_addr), INET_ADDRSTRLEN - 1);
    return 1;
}

int main()
{
    char *interface_name = "eno1";
    char ip_address[INET_ADDRSTRLEN] = {0};
    int ret = get_interface_ip(interface_name, ip_address);
    if (ip_address == NULL || ret == 0)
    {
        printf("No IP address found");
        return 0;
    }
    printf("Interface address: %s\n", ip_address);
    return 1;
}