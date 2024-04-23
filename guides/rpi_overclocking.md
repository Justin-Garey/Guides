# Overclocking a Raspberry Pi
Adequate cooling and heatsinks are required

## For the RPi 4b

Update and upgrade the pis dependencies
```
sudo apt update && sudo apt upgrade -y
sudo apt dist-upgrade
sudo apt install rpi-update
```

Enter an editor for the boot config
```
sudo nano /boot/config.txt
```

There should be a section that reads
```
#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800
```


Add this somewhere in the configuration:
```
over_voltage=6
arm_freq=2000
gpu_freq=750
```

To see the clock speeds or measure cpu temperatures
```
watch -n1 vcgencmd measure_clock arm
watch -n1 vcgencmd measure_temp
```

## For the Pi 3b+

The RPI 3B+ is already set to run at the stable overclock of 1.4GHz and idle at 600MHz. With this in mind, it is better to just increase the idle if really desired. A good cooling system is also a necessity. If the cooling is good enough, the board will operate at 1.4GHz anyways. 