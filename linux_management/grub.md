# GRUB

GRUB is the GRand Unified Bootloader. It can be used for recovery, dual booting between operating systems, or for using multiple kernel versions.

## Accessing GRUB

To access GRUB on a BIOS system, hold shift during startup. On a UEFI system, press escape.

## Setting a Device to Always Launch GRUB

GRUB can be set to always launch on boot by setting the `GRUB_TIMEOUT` option to a non-zero value in */etc/default/grub*. 
```conf
GRUB_TIMEOUT=-1
```

To edit the file:
```bash
sudoedit /etc/default/grub
```

After setting `GRUB_TIMEOUT` and saving the changes, update GRUB to use the changes.
```bash
sudo update-grub
```
