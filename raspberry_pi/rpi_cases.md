# Raspberry Pi Cases

An (incomplete) list of Raspberry Pi Cases with use cases and setup instructions.

## Argon One M.2 

### Use
- Fits the Raspberry Pi 4b
- The primary use of this case is to attach a M.2 SATA SSD
  - The board accepts B Key and B+M Key
- Also offers a power button with some software defined functionality and an Infrared Reciever

### Setup 
- Once built and connected to the internet, install the Argon One Pi 4 script in order to use the power button, modify the fan speeds, and configure the Infrared Receiver
```
curl https://download.argon40.com/argon1.sh | bash
```
- To configure the fan:
```
argonone-config
```
- To uninstall:
```
argonone-uninstall
```

### Other Usage
- The built-in infrared receiver can be configured with:
```
argonone-ir
```
- The power button has extra functionality as well
  - When off, click the button to turn on
  - When on:
    - A double tap will reboot
    - A press of 3 or more seconds will soft shutdown (power cut)
    - A press of 5 or more seconds will force shutdown

## Miuzei 4 inch HDMI Display

### Use
- Designed for the RPi 4b, but also works with the RPi 3b+.
- Can be used as just a display connected to the pi or as a touch screen.

### Setup
Display
- Connect the pi to the display then power the pi. The resolution should automatically be configured.
- The screen may be rotated incorrectly for your use. To configure the orientation:
  - Click the Raspberry in the top left
  - Select Preferences
  - Enter the Screen Configuration
  - Right click the hmdi image
  - Select Orientation
  - Select your desired orientation
    - It will revert back if you don't approve it within 10 seconds

Touch Capabilities
```
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./MPI4008-show
```
- Using the touchscreen will mess up some functionality on the pi.

### Other Usage
The touch screen has a power button. 
- Short press to increase brightness by 10%. After reaching 100%, it will cycle to 1%.
- Long press for 3 seconds to set the backlight to off, then short press to restore backlight brigtness

Run Linux screen savers
- Need xterm
```
sudo apt update
sudo apt install -y xterm
```
- Install CMatrix
```
sudo apt install -y cmatrix
```
- Run CMatrix
```
xterm -fa monac -fs 20 -fullscreen
cmatrix
```
- Install Asciiquarium
```
sudo apt install -y libcurses-perl
cd /tmp
wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.6.tar.gz
tar -zxvf Term-Animation-2.6.tar.gz
cd Term-Animation-2.6
perl Makefile.PL && make &&  make test
sudo make install
cd /tmp
wget --no-check-certificate http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
tar -zxvf asciiquarium.tar.gz
cd asciiquarium_1.1
sudo cp asciiquarium /usr/local/bin/
sudo chmod 0755 /usr/local/bin/asciiquarium
```
- Run Asciiquarium
```
xterm -fullscreen
asciiquarium
```
- Install pipes.sh
```
git clone https://github.com/pipeseroni/pipes.sh.git
cd pipes.sh
sudo make install
```
- Run pipes.sh
```
pipes.sh
```
