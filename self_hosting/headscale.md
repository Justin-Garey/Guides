# [Headscale](https://headscale.net/)

This is a self hosted and open source alternative to the [Tailscale](./tailscale.md) control server.
## Host Setup

Since the control server for the Tailnet needs to be hosted outside of my home network, I am using an EC2 instance on Amazon. The EC2 instance is configured with:
- Ubuntu Server 24.04 OS, 64-bit (x86)
- A t2.micro instance type. This has 1vCPU and 1 GiB memory
- Allow HTTP traffic from the internet
- 8 GiB of storage (this is probably overkill)
## Installation

1. Update and upgrade:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Download the latest version from [GitHub](https://github.com/juanfont/headscale/releases)
```bash 
wget --output-document=headscale.deb https://github.com/juanfont/headscale/releases/download/v0.23.0/headscale_0.23.0_linux_amd64.deb
```

3. Install headscale:
```bash
sudo apt install ./headscale.deb
```

4. Configure headscale:
```bash
sudo nano /etc/headscale/config.yaml
```
- `server_url: http://<EC2_INSTANCE_ADDRESS>:80`
- `listen_addr: 0.0.0.0:80`
- `base_domain: something.local`
	- You can access a service with *hostname.something.local*
	- The default is *example.com* which will work

5. Enable and start headscale:
```bash
sudo systemctl enable --now headscale
sudo systemctl status headscale
```
## Add a User

Before adding any clients, some users will need added in the headscale machine. This is done with:
```bash
sudo headscale users create <USER_NAME>
```
## Create a User Key

A key is needed to add a client device to the Tailnet.

The default key creation will make a new key for a user that can be used once and expires after one hour:
```bash
sudo headscale preauthkeys create --user <USER_NAME>
```
- As long as the machine is not disconnected from Headscale, it will always reconnect on boot.

The output will confirm the key creation with an expiry:
```log
2024-12-14T04:05:36Z TRC expiration has been set expiration=3600000
```

To make a key that will not expire and reusable:
```bash
sudo headscale preauthkeys create -e 99y --reusable --user <USER_NAME>
```
- This came in handy on my laptop which was having issues connecting after a reboot.
## Connect the Tailscale Node (Linux)

See the [Tailscale](./tailscale.md) doc for more on setting up Tailscale. If you have already connected Tailscale to a control server previously, run `sudo apt purge tailscale -y && sudo apt install tailscale -y` as Tailscale has some hiccups when it comes to making new connections. This also goes for when you've already connected to the same Headscale server before.

To connect to the Headscale control server:
```bash
sudo tailscale up --login-server http://<EC2_INSTANCE_ADDRESS> --auth-key <AUTH_KEY>
```
- This should only need done once and persist across reboots of both the control server and the client device. If the control server goes offline, some of the client devices may need restarted once it is back online to establish a proper connection.
## Connect the Tailscale Node (Windows)

First, install the [Windows Client](https://tailscale.com/download/windows). Then open up CMD to connect to the Headscale control server:
```powershell
tailscale up --accept-routes --login-server http://<EC2_INSTANCE_ADDRESS> --auth-key <AUTH_KEY>
```
- This will persist across reboots.
## Connect the Tailscale Node (iOS)

1. Install the Tailscale app on the iOS device. Go through the set up process but do not log in. If you are already logged in, log out. Close out of the app.
2. In Settings, go to VPN settings where the Tailscale VPN is set as the *Device VPN*. Click the info icon and turn off *Connect on Demand*. This will come back on later but I was having some issues with connecting to a non *ts.net* control server (Headscale or Tailscale Enterprise)
3. Also in Settings, search *Tailscale*. Click on the app settings and toggle *Reset Keychain* to on.
4. Go back to the Tailscale app, click on the account profile icon in the top right. Select *Log In...* then click the three dots in the top right. Select *Use a custom coordination server*.
5. Enter the address of the Headscale server (i.e. `http://<EC2_INSTANCE_ADDRESS>`) and select login.
6. Instructions for what to enter into the Headscale server should pop up. Make sure the user is created first then the instructions are similar to:
```bash
sudo headscale nodes register --user <USER_NAME> --key mkey:<MKEY>
```
## Headscale Operation

View the available users with:
```bash
sudo headscale users list
```

View the available nodes with:
```bash
sudo headscale nodes list
```
## Headscale Configuration

If you make any changes to the configuration, make sure to restart Headscale after:
```bash
sudo systemctl restart --now headscale
```
- Some of the client devices will need rebooted after this to create a proper connection. Do this with caution.
