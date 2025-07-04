# Making a Pwnagatchi

## Hardware

## Step 1: Putting it together

Start by soldering the headers onto the Raspberry Pi Zero (unless you have one with headers already installed).

The next step is to attach the UPS-Lite to the Pi Zero.

Lastly, slide the E-Ink display onto the headers of the Raspberry Pi Zero.

## Step 2: Verify the E-Ink display works

From https://www.waveshare.com/wiki/2.13inch_Touch_e-Paper_HAT_Manual#Raspberry_Pi

- Flash the micro SD card with Raspberry Pi OS Lite (32 Bit) in the Raspberry Pi Imager
- Before hitting the write button after selecting the OS and SD card, hit the settings button
[settings button](./images/step_1.png)
- Lastly, the ip address needs found. Either use your routers web interface or just run ```sudo nmap -sn 192.168.1.0/24```.
- Now you can ssh into the pi with ```ssh pi@ip.address```