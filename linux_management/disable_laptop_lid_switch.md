# Disable Laptop Lid Switch in Ubuntu

These instructions are based on an [answer](https://askubuntu.com/a/372616) on Ask Ubuntu. This will make closing the laptop lid do nothing. 

First, edit the */etc/systemd/logind.conf* file as root.

```bash
sudo nano /etc/systemd/logind.conf
```

Then, set `HandleLidSwitch` to `ignore`. You may have to uncomment the property.

```text
HandleLidSwitch=ignore
```

Lastly, restart the systemd daemon (you will be logged out).

```bash 
sudo service systemd-logind restart
```

**Note**: There may be some BIOS settings that need modified too.