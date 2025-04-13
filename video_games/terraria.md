# Terraria Server

## Getting Started

Install some tools and update:
```bash
sudo apt update && sudo apt install -y wget screen unzip
```
- ```curl``` can be used instead of ```wget```.
- ```tmux``` or Systemd can be used instead of ```screen```.
## Vanilla Terraria Server

The following process is based on the guide by the [Terraria Fandom](https://terraria.fandom.com/wiki/Server#How_to_(Linux)).
### Setup

Find the link to the latest [download](https://terraria.fandom.com/wiki/Server#Downloads) then use ```wget <LINK>``` to download. Then unzip with:
```bash
unzip terraria-server*
```

```cd``` into the created directory, then ```cd Linux``` for the Linux server location.

Add executable permissions to the binary:
```bash
chmod +x TerrariaServer.bin.x86*
```

Now launch the server with
```bash
./TerrariaServer.bin.x86_64
```
- When this is ran, you can select or create a new world
- To launch it in the background, first start a screen session

Finally, any world files can be placed in ```~/.local/share/Terraria/Worlds/```
### Multiplayer

There are a couple things that need to be done to configure multiplayer

1. Port forward to the machine running the Terraria server
2. Get your public IP address
3. Give the address to your friends
## Playing a Modded Terraria World

In Steam, install tModLoader. After it has installed (assuming Terraria is also installed), hit play.

To View/Modify/Add Mods, select ```Workshop``` in the tModLoader Terraria menu.
- Select ```Download Mods``` to install mods. There is a search bar in the top right of the menu.
- Select ```Manage Mods``` to see mods already on your system. Mods can be enabled and disabled from here by clicking the ```Enabled``` or ```Disabled``` text.

Go to ```~/.local/share/Terraria/tModLoader``` on Ubuntu to locate the mod files and world files.
### Quality of Life (QoL) Mods

There are a few QoL mods that I like
- ```Recipe Browser```: Allows you to view crafting recipes, search based on items, and search based on names.
- ```AlchemistNPC Lite```: Adds an Alchemist NPC which sells potions.
- ```Fargo's Mutant Mod```: Adds lots of NPCs and some items to make certain parts of the game less grindy.
- ```Ore Excavator```: Allows you to veinmine ores and other blocks (Only ores are whitelisted initially).
- ```Magic Storage```: Adds in a condensed storage system to remove the hassle of sorting through chests.
- ```Boss Checklist```: Gives a list of bosses and information about them. The list will tell you which ones you have and have not defeated or tried.
- ```Shared World Map```: Allows players to share their world maps.
### Playing With the Mods

Just start a world and have fun!
## Modded Terraria Server
### Hosting on Your Computer Running Terraria

There are 4 ways to host the world from your local computer
- Host via Steam
- Host via IP
- Non-Dedicated host via IP
- Non-Dedicated host via Steam

The *Host via Steam* option is the default when you select ```Host & Play```. You can disable the ```Steam Multiplayer``` to host via IP but you'll have to configure port forwarding and telling your friends where the server can be found.

The *Non-Dedicated host via IP/Steam* options from the computer you are playing on would be fine if you are connected to Ethernet and want to leave the server running longer without you directly playing but this requires you to leave said computer alone while it is running the server. This can be done on an Ubuntu machine by running ```./start-tModLoaderServer.sh``` located in ```~/.local/share/Steam/steamapps/common/tModLoader```. Just follow the prompts to get your world running.
### Setting up a Dedicated Host

Here is the only good [guide](https://youtu.be/vN8LqgKPN0s?si=6UuSWAfut8d-h6TY) I could find online.

Start by creating a directory for your Terraria Servers
```bash
mkdir TerrariaServers
cd TerrariaServers
```

Then make a directory for tModLoader
```bash
mkdir tModLoader
cd tModLoader
```

Download the latest tModLoader release from [GitHub](https://github.com/tModLoader/tModLoader/releases) by copying the link and running, for example,
```bash
wget https://github.com/tModLoader/tModLoader/releases/download/v2025.02.3.2/tModLoader.zip
unzip tModLoader.zip tModLoader
rm tModLoader.zip
```

Add execution permissions to the start server script
```bash
chmod +x ./start-tModLoaderServer.sh
```
- If you are getting a steam error then you are using the wrong script. I banged my head against the wall for a while because I was trying to run ```./start-tModLoader.sh``` instead of the server.

Now run the start script
```bash
./star-tModLoaderServer.sh
```
- This will prompt you if you want to use steam; enter ```n``` for no.
- Then it will install the dotnet files if necessary.
- Lastly it will prompt you for the world setup.
#### Adding the Mods
##### Method 1: Copying From Computer being Played On

On Ubuntu, navigate to ```~/.local/share/Steam/steamapps/workshop/content/<some number>/```. Each directory here contains one of the mods. Enter each one, then enter the newest folder by date. Each directory has a date as the name. Now you should see the ```.tmod``` file for the mod. Copy that to some easy to access folder.

After each mod is copied into your easy to access folder, enter the directory with your terminal and run shell copy.
```bash
scp * machine:~/.local/share/Terraria/tModLoader/Mods
```

Now the mods can be enabled through the tModLoader server terminal upon starting up a world.
##### Method 2: Use `steamcmd` to Download

Install `steamcmd`
```bash
sudo add-apt-repository multiverse; sudo dpkg --add-architecture i386; sudo apt update
sudo apt install steamcmd
```

With more time, a shell script could be developed to take a list of mod ids and download them using `steamcmd`. Refer to the [steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD) wiki and this [Docker implementation](https://github.com/JACOBSMILE/tmodloader1.4) that has download capabilities built in.
#### Moving a Pre-Existing World to the Server

First, make sure a *Terraria* directory exists on the server.
```bash
mkdir ~/.local
mkdir ~/.local/share
mkdir ~/.local/share/Terraria
```

On Linux (Ubuntu), the world and mod files are located in ```~/.local/share/Terraria/tModLoader```. That is also where tModLoader on the dedicated server expects the files to be. Easy to just shell copy the files over.
```bash
scp -r ~/.local/share/Terraria/tModLoader/ machine:/home/justin/.local/share/Terraria/
```
- This will copy over the Worlds but not the mods. See above to finish copying those over.
#### Server Configurations

It is much easier to use a configuration file and command line parameters than it is to keep manually setting up the world. The command structure I am using is:
```bash
./start-tModLoaderServer.sh -nosteam -port 7777 -maxplayers 2 -password "" -world ~/.local/share/Terraria/tModLoader/Worlds/Spiky_Tree_Time.wld | tee -a server-logs.log
```
- I've included the tee command above as I am using that to save the log files. I've seen a lot of internet bots try to see whats available on that port. A quick scan ensures no one is actually connecting to my server aside from those I want.
- Using `-password ""` means no password. Definitely have a password if this server is externally visible from the network it is on.

A configuration file could also be created but isn't necessary for the basics unless you have multiple worlds with different permissions you would like to put up. The above could be done in a configuration file such as *spiky_tree_time_config.txt*. The command would be ```./start-tModLoaderServer.sh -config ./spiky_tree_time_config.txt```.
### Updating tModLoader

With the manual installation of tModLoader for a server, the files will also need manually updated with a new stable release. This can be done by downloading the tModLoader zip file and unzipping it over the old tModLoader files then giving the start server script permissions. This will look like:
```bash
wget https://github.com/tModLoader/tModLoader/releases/download/v2025.02.3.2/tModLoader.zip
unzip -o tModLoader.zip -d tModLoader/
chmod +x tModLoader/*.sh
rm tModLoader.zip
```

## TShock on a Raspberry Pi
Basic server setup using tshock for Terraria designed for a Raspberry Pi

**Note**: TShock does not support mods
### Requirements

Must use a 64 bit operating system on the Raspberry Pi
### Usage

The process for setting up a system to run the TShock server is shown here. There may be newer versions of TShock out so make sure to check that the versions are up to date.
```bash
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
```bash
WORLD_NAME="world"

echo exit | ./TShock.Server -port 7777 -world ./Worlds/$WORLD_NAME.wld -maxplayers 8 -autocreate 1 -worldevil random -difficulty 0
```
- Look at the [tshock docs](https://ikebukuro.tshock.co/#/command-line-parameters) for more command line parameters

Launching the world is very simple but I would recommend creating a shell script called *launch* for ease. That script would look like:
```bash
#!/bin/bash

WORLD_NAME="world"

./TShock.Server -world ./Worlds/$WORLD_NAME.wld
```
- Change WORLD_NAME to the name of your world
### Other useful tools
#### Screen

If you have the server running and you would like to ssh into the machine to see the logs or run commands, I recommend using screen. It allows you to run a task and put it in the background by detaching from it. You can later re-attach to interact again.

To install
```bash
sudo apt install screen
```

To use
```bash
screen
```

Once the server is running; detach with ctrl+a, d.

When you want to re-attach, use
```bash
screen -r
```
- If you have multiple instances of screen you will need to specify the id to re-attach
#### Systemd

This is useful if the server is a dedicated host, meaning the Terraria server should always be running and should restart in case of a crash or the machine losing power and coming back online. Start by figuring out the start command and options for the server. The following example is going to be for a modded Terraria server using tModLoader. The start command will be ran as root and will look like:
```bash
/home/<USER>/TerrariaServers/tModLoader/start-tModLoaderServer.sh -nosteam -world /home/<USER>/.local/share/Terraria/tModLoader/Worlds/Spiky_Tree_Time.wld -maxplayers 2 -port 7777 -password "" -modpath /home/<USER>/.local/share/Terraria/tModLoader/Mods/
```
- Replace `<USER>` with your user.

Now, the tModLoader service can be created with `sudo nano /etc/systemd/system/tmodloader.service` and the service file is:
```ini
[Unit]
Description=tModLoader Terraria Server
After=network.target network-online.target

[Service]
Type=simple
ExecStart=/home/<USER>/TerrariaServers/tModLoader/start-tModLoaderServer.sh -nosteam -world /home/<USER>/.local/share/Terraria/tModLoader/Worlds/Spiky_Tree_Time.wld -maxplayers 2 -port 7777 -password "" -modpath /home/<USER>/.local/share/Terraria/tModLoader/Mods/
Restart=always

[Install]
WantedBy=multi-user.target
```

Once that is saved; reload, start, and enable the service:
```bash
sudo systemctl daemon-reload
sudo systemctl start tmodloader
sudo systemctl enable tmodloader
sudo systemctl status tmodloader
```
### References

- [Terraria Fandom Linux Server](https://terraria.fandom.com/wiki/Server#How_to_(Linux))
- [Terraria Fandom Linux Server Downloads](https://terraria.fandom.com/wiki/Server#Downloads)
- [tModLoader Dedicated Linux Server Video Guide](https://youtu.be/vN8LqgKPN0s?si=6UuSWAfut8d-h6TY)
- [tModLoader GitHub](https://github.com/tModLoader/tModLoader/releases)
- [TShock Github](https://github.com/Pryaxis/TShock)
- [Auto-restart with tmux](https://www.reddit.com/r/Terraria/comments/3gl5kk/installing_and_running_a_terraria_server_with/)
- [TShock Documentation](https://ikebukuro.tshock.co/)