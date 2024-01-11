# Screensavers I Like

## [Asciiquarium](https://robobunny.com/projects/asciiquarium/html/)

### Installation

This Stack Overflow [thread](https://askubuntu.com/questions/927441/how-do-i-install-asciiquarium) offers both common methods of installation. I used the top voted one (below) but there is a full installation method in the thread.
```
sudo add-apt-repository ppa:ytvwld/asciiquarium
sudo apt-get update && sudo apt-get install asciiquarium
```

### Usage

```asciiquarium```

## [Pipes.sh](https://github.com/pipeseroni/pipes.sh)

### Installation

The github page provides some requirements and installation instructions. Below is a summary of how to install.
```
git clone https://github.com/pipeseroni/pipes.sh.git
cd pipes.sh
sudo make install
```

### Usage

```pipes.sh```

My favorite way to run pipes.sh is ```pipes.sh -t 7 -f 50 -R```. That is pipe type 7 with framerate 50 and randomized start position/direction.

## Cmatrix

### Installation

Cmatrix can be installed with ```sudo apt install cmatrix```.

### Usage

```cmatrix```

Using ```-s``` (screensaver) will make it exit on a keypress and ```-r``` (rainbow) will make the text appear multicolored.

## All At Once

### On the Raspberry Pi with Its Own Screen

In order to go full screen on the Raspberry Pi with Raspbian, I've been using xterm. I was only running asciiquarium but it becomes laggy after running for so long. My solution was to make a loop to start and restart the program. Then I thought *Why not run a random program so I can have the joy of every screen saver*. So I spent way too much time coming up with this command which loops forever and runs a random screen saver every hour.

```
while ((1)); do timeout 3600s $(printf 'xterm -fa monaco -fullscreen -e "asciiquarium"\nxterm -fa dejavu -fs 20 -fullscreen -e "cmatrix"\nxterm -fullscreen -fa dejavu -e "pipes.sh"' | shuf -n 1); done
```