## Removing the Ubuntu Boot Logo

If you ever get annoyed of the Ubuntu boot logo, there is a pretty easy way to remove it. 

Start by modifying the grub configuration with ```sudo nano /etc/default/grub```. Then change quiet splash to nothing “”. The line
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```
should become
```
GRUB_CMDLINE_LINUX_DEFAULT=""
```
After, gub needs updated and the system rebooted.
```
sudo update-grub
sudo reboot
```
