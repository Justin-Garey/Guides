# Proxmox
## Setup Process
### Installation

1. [Download](https://www.proxmox.com/en/downloads) the Proxmox image
2. Flash the image to a USB drive: [instructions](https://pve.proxmox.com/wiki/Prepare_Installation_Media)
	1. Balena Etcher did not work for me on Ubuntu
	2. Use `lsblk` to get the name of the USB drive
	3. Run `dd bs=1M conv=fdatasync if=./PATH_TO_ISO/proxmox-ve_*.iso of=/dev/USB_DRIVE_NAME`
		1. Make sure to insert the name of the USB drive and the path to the Proxmox ISO
### Boot from ISO

- You'll need to boot from the iso file on the flash drive. This can be done a few ways, either using the function keys to get into the boot menu or by using a command to reboot into the bios ([linux method](../linux_management/enter_bios.md)).
### Terminal UI Setup

1. After booting up Proxmox, there will be an option to Install the Graphical or Terminal UI version. Select the Terminal UI installation.
2. Agree to the EULA.
3. Make sure the target hard disk is correct.
4. Verify or set the country, timezone, and keyboard layout.
5. Set the root password and administrator email.
6. Configure basic networking settings and a hostname. The hostname should be in the form of `hostname.domain`. I set the domain to `local` as its on my local network.
7. Verify the information and hit install.
### Update the System

After it is setup, as root, run:
```bash
apt update
apt upgrade -y
```
### Entering the Web Based Management Interface

- The management interface is available on port `8006` at the address given to the Proxmox machine.
- The web interface will probably be considered a security risk by the browser due to the certificate being self signed and not recognized. The best solution is to just proceed. This [Reddit post](https://www.reddit.com/r/Proxmox/comments/17e0l7z/understanding_implications_of_proxmoxs_selfsigned/) highlights the issue with more options to mitigate it.
- Upon first time access, you will need to sign in with `root` and the password created at during the set up process.
## Machine Modifications

- In the BIOS menu, I've set the computer to boot up when being powered on again. Not necessary, but its useful for automating the services I want to run.
## Using Proxmox
### Creating User Accounts

Step one is creating the user in the terminal so ssh into the machine, then run `adduser user_name` and `passwd user_name` to create the password. Lastly, run `usermod -aG sudo user_name` to add the user to the group of sudoers. (Note: You will need to install `sudo` to use it as that user)

The new user, by default will use `sh` instead of `bash`. See my [note](../miscellaneous/set_shell.md) on setting your default shell.

With `Server View` selected on the left dropdown and `Datacenter` in focus, select the `Users` tab under `Permissions`.
![Create a user account in Proxmox step 1](proxmox_creating_user_account_step_1.png)

- Hit `Add` and enter the information for the user. Make sure the `Linux PAM standard authentication` realm is selected.

Next, select `Permissions` and `Add`, then `User Permission`. Now for an administrative user, select `Path`: `/`, the user you just created, `Role`: `Administrator`, and make sure the box for `Propagate` is checked.
![Create a user account in Proxmox step 2](proxmox_creating_user_account_step_2.png)
### Add an ISO Image to Proxmox

Drop down the server under `Datacenter` on the left side bar. Click `local` and select `ISO Images`. From here, an image can be uploaded or downloaded from a URL.
![Add ISO image in Proxmox step 1](proxmox_add_iso_step_1.png)
### Creating a VM

In the upper right, click the `Create VM` button. Then name the VM.
![Create a VM in Proxmox step 1](proxmox_create_vm_step_1.png)

Hit `Next`, then select an ISO image that you loaded earlier.
![Create a VM in Proxmox step 2](proxmox_create_vm_step_2.png)

Hit `Next`, the defaults under `System` are fine for basic use cases. For more advanced uses, you may need to set up a OVMF bios.
![Create a VM in Proxmox step 3](proxmox_create_vm_step_3.png)

Hit `Next`, the main item under `Disks` to pay attention to is the `Disk size`. This can always be changed later but it would be easier to set it to whatever you need for your desired application.
![Create a VM in Proxmox step 4](proxmox_create_vm_step_4.png)

Hit `Next`, then determine how many sockets and cores you need for the machine. Also pay attention to the `type` of CPU as some programs need certain features from the CPU. Using `host` will give all of the host machine features to the VM.
![Create a VM in Proxmox step 5](proxmox_create_vm_step_5.png)

Hit `Next`, and set the RAM for the VM.
![Create a VM in Proxmox step 6](proxmox_create_vm_step_6.png)

Hit `Next`. The `Network` section doesn't need any modification.
![Create a VM in Proxmox step 7](proxmox_create_vm_step_7.png)

Hit `Next` and look over the configuration. If satisfied, click `Finish`.
![Create a VM in Proxmox step 8](proxmox_create_vm_step_8.png)
### Managing a VM

The VM is fairly intuitive for basic operations. There are options to start, stop, shutdown, etc. in the lower menu bar at the top right of the management interface. These can also be accessed by right clicking on the VM's name.

The `Summary` tab within the VM window will share the status of the VM and how well it is performing. The `Console` tab grants you a console through the web which comes in handy if the VM is easy to set up.
### Automatically Start a VM When Proxmox is Powered On

To set a VM to auto start when Proxmox powers on, select the `Options` tab. Then set `Start at boot` to `Yes`.
## Quality of Life Changes
### Install `sudo` for Added Users

`sudo` is not installed by default in Debian, so it will need installed for added administrative users. As root:
```bash
apt install sudo
```
### Remove Root SSH Login for Security

The `PermitRootLogin` line in */etc/ssh/sshd_config* needs commented out to disable root login. Refer to the *[[ssh#Enable Root Login Over SSH|Enable Root Login Over SSH]]* section in the [SSH usage tips guide](../tools/ssh.md)
### Nagging Proxmox Subscription Messages

Upon logging into the management interface, I am greeted with this message:
> You do not have a valid subscription for this server. Please visit [www.proxmox.com](https://www.proxmox.com/en/proxmox-virtual-environment/pricing) to get a list of available options.
- This [Reddit discussion](https://www.reddit.com/r/Proxmox/comments/tgojp1/removing_proxmox_subscription_notice/) has some solutions.
- I ended up modifying the [suggested script](https://github.com/foundObjects/pve-nag-buster) from GitHub
	- [My script](https://github.com/Justin-Garey/pve-nag-buster) is updated for Proxmox version 8.2

**How I Fixed It**:
1. SSH into the machine
2. Then download and run the install script
```bash
wget https://raw.githubusercontent.com/Justin-Garey/pve-nag-buster/fixed_repository_links/install.sh && sudo bash install.sh
```
### Errors and Warnings from Enterprise PVE apt Repositories

Proxmox tries to update from the paid repositories, producing warnings and errors if you are not a paying customer:
```none
Hit:1 http://ftp.us.debian.org/debian bookworm InRelease
Hit:2 http://ftp.us.debian.org/debian bookworm-updates InRelease
Err:3 https://enterprise.proxmox.com/debian/ceph-quincy bookworm InRelease
  401  Unauthorized [IP: 66.70.154.82 443]
Err:4 https://enterprise.proxmox.com/debian/pve bookworm InRelease
  401  Unauthorized [IP: 66.70.154.82 443]
Hit:5 http://security.debian.org bookworm-security InRelease
Reading package lists... Done
E: Failed to fetch https://enterprise.proxmox.com/debian/ceph-quincy/dists/bookworm/InRelease  401  Unauthorized [IP: 66.70.154.82 443]
E: The repository 'https://enterprise.proxmox.com/debian/ceph-quincy bookworm InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E: Failed to fetch https://enterprise.proxmox.com/debian/pve/dists/bookworm/InRelease  401  Unauthorized [IP: 66.70.154.82 443]
E: The repository 'https://enterprise.proxmox.com/debian/pve bookworm InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```
- The solution for this is couple with [[#Nagging Proxmox Subscription Messages]]
## Miscellaneous
### Check the Version of Proxmox

The full version information can be seen within the command line by running ```pveversion```. The output will look like:
```bash
pve-manager/8.2.2/9355359cd7afbae4 (running kernel: 6.8.4-2-pve)
```

Running ```pveversion --verbose``` will result in much more detailed information.
## References

- [Proxmox Website](https://www.proxmox.com/en/)
- [Reddit post](https://www.reddit.com/r/Proxmox/comments/17e0l7z/understanding_implications_of_proxmoxs_selfsigned/) highlighting the self signed certificate warning on web browsers.
- [Reddit post](https://www.reddit.com/r/Proxmox/comments/tgojp1/removing_proxmox_subscription_notice/) on the subscription pop up on Proxmox
	- [Scripted solution](https://github.com/foundObjects/pve-nag-buster) from GitHub
	- [My updated solution](https://github.com/Justin-Garey/pve-nag-buster) for Proxmox version 8.2 on GitHub