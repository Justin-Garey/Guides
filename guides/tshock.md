# Terraria-Server
Basic server setup using tshock for Terraria designed for a Raspberry Pi

## Requirements

Must use a 64 bit operating system on the Raspberry Pi

## Create Shell Scripts

*setup*
```

```

## Usage

The process for setting up a system to run the TShock server is shown here. There may be newer versions of TShock out so make sure to check that the versions are up to date.
```
# Install dependencies
sudo apt install -y wget screen

# Install server
wget https://github.com/Pryaxis/TShock/releases/download/v5.2.0/TShock-5.2-for-Terraria-1.4.4.9-linux-arm64-Release.zip
unzip TShock*.zip
tar -xvf TShock*.tar

# Install .net
wget https://dot.net/v1/dotnet-install.sh
sudo bash ./dotnet-install.sh --channel LTS --install-dir /opt/dotnet/
sudo ln -s /opt/dotnet/dotnet /usr/local/bin
echo 'export DOTNET_ROOT=/opt/dotnet' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/.dotnet' >> ~/.bashrc
source ~/.bashrc

# Create worlds folder
mkdir Worlds
```
- This should only be done once on a system as it will reinstall and add some clutter

TShock offers a lot of configuration. To create a simple world for use, run the commands below. 
```
WORLD_NAME="world"

echo exit | ./TShock.Server -port 7777 -world ./Worlds/$WORLD_NAME.wld -maxplayers 8 -autocreate 1 -worldevil random -difficulty 0
```
- Look at the [tshock docs](https://ikebukuro.tshock.co/#/command-line-parameters) for more command line parameters

Launching the world is very simple but I would recommend creating a shell script called *launch* for ease. That script would look like:
```
#!/bin/bash

WORLD_NAME="world"

./TShock.Server -world ./Worlds/$WORLD_NAME.wld
```
- Change WORLD_NAME to the name of your world

## Other useful tools

### Screen
If you have the server running and you would like to ssh into the machine to see the logs or run commands, I recommend using screen. It allows you to run a task and put it in the background by detaching from it. You can later re-attach to interact again.

To install
```
sudo apt install screen
```

To use
```
screen
```

Once the server is running; detach with ctrl+a, d.

When you want to re-attach, use
```
screen -r
```
- If you have multiple instances of screen you will need to specify the id to re-attach

## References

[TShock Github](https://github.com/Pryaxis/TShock)

[Auto-restart with tmux](https://www.reddit.com/r/Terraria/comments/3gl5kk/installing_and_running_a_terraria_server_with/)

[The docs](https://ikebukuro.tshock.co/)