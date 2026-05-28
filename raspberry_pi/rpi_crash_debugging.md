# Debugging Crashing on Raspberry Pi

Check logs for errors:
- */var/log/messages*
- */var/log/syslog*
- */var/log/dmesg*

Check that the power supply is working using `vcgencmd get_throttled`. It should return *0x0* otherwise there is an issue with power.