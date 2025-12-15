# Check if the Underlying Storage is an HDD or SDD

First, find the name of the device to check:
```bash
$ lsblk
NAME                      MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0 931.5G  0 disk 
├─sda1                      8:1    0     1M  0 part 
├─sda2                      8:2    0     2G  0 part /boot
└─sda3                      8:3    0 929.5G  0 part 
```

In this case, check `sda`:
```bash
$ cat /sys/block/sda/queue/rotational
1
```
- 0 means SSD
- 1 means HDD

The device `sda` is a HDD.