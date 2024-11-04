# Proxmox
### Installation

1. [Download](https://www.proxmox.com/en/downloads) the Proxmox image
2. Flash the image to a USB drive: [instructions](https://pve.proxmox.com/wiki/Prepare_Installation_Media)
	1. Balena Etcher did not work for me on Ubuntu
	2. Use `lsblk` to get the name of the USB drive
	3. Run `dd bs=1M conv=fdatasync if=./PATH_TO_ISO/proxmox-ve_*.iso of=/dev/USB_DRIVE_NAME`
		1. Make sure to insert the name of the USB drive and the path to the Proxmox ISO
### Boot from ISO

- You'll need to boot from the iso file on the flash drive. This can be done a few ways, either using the function keys to get into the boot menu.
### Terminal UI Setup

1. After booting up Proxmox, there will be an option to Install the Graphical or Terminal UI version. Select the Terminal UI installation.
2. Agree to the EULA.
3. Make sure the target hard disk is correct.
4. Verify or set the country, timezone, and keyboard layout.
5. Set the root password and administrator email.
6. Configure basic networking settings and a hostname. The hostname should be in the form of `hostname.domain`. I set the domain to `local` as its on my local network.
7. Verify the information and hit install.
### Entering the Web Based Management Interface

- The management interface is available on port `8006` at the address given to the Proxmox machine.
- The web interface will probably be considered a security risk by the browser due to the certificate being self signed and not recognized. The best solution is to just proceed. This [Reddit post](https://www.reddit.com/r/Proxmox/comments/17e0l7z/understanding_implications_of_proxmoxs_selfsigned/) highlights the issue with more options to mitigate it.
- Upon first time access, you will need to sign in with `root` and the password created at during the set up process.
## References

- [Proxmox Website](https://www.proxmox.com/en/)
- [Reddit post](https://www.reddit.com/r/Proxmox/comments/17e0l7z/understanding_implications_of_proxmoxs_selfsigned/) highlighting the self signed certificate warning on web browsers.