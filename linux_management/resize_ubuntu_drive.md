# Resizing an Ubuntu Drive
## Problem 

Ubuntu is not using all the available space in its drive.
## Diagnosis

Using `df -h` or `lsblk` will show this happening. There will be a total available space on the drive and a smaller amount for the partition.
## Solution

```bash
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv  
resize2fs /dev/ubuntu-vg/ubuntu-lv
```
- */dev/ubuntu-vg/ubuntu-lv* is the Ubuntu partition name
## References

- [Stack Overflow Answer](https://serverfault.com/questions/1035342/ubuntu-server-only-uses-a-part-of-the-available-disk-space)