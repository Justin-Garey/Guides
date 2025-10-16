# Issues While Using a Second or Multiple Monitors in Ubuntu with NVIDIA

The following is not necessarily *The Solution* but are things I've tried while troubleshooting issues with a second monitor and an NVIDIA driver. The following is listed as issues with their proposed solutions as starting points. If I encounter this again, I will update the guide with more detailed instructions and tips.
## When Connecting a Second Monitor, The Monitor Remains Blank
### Recently Suggested

Simply run:
```bash
nvidia-detector
```

I'm not sure yet what this does or if it works, but I've been told by one source that it solved the issue for them.
### Install a Different Driver

Usually when this happens to me, I either haven't used a second monitor in a bit or I've just installed some updates. Sometimes the newer NVIDIA drivers available in Ubuntu don't have the kinks worked out and struggle to fulfil their duties. Reverting the NVIDIA driver to an older version is a good way to mitigate the issue.
## Color is Off on the Monitor
### Change the Color Profile

Ubuntu has color profiles for the displays. This one is an easy fix once you find the color profiles option in settings. The color profiles are supposed to automatically be set for the type of monitor that is connected, but sometimes the system will have a hiccup.

On Ubuntu 22.04, the color profiles are found under **Settings** -> **Color** -> **Device**.

## Primary Monitor Appears Yellow

Simply updating, upgrading, and rebooting seem to solve this.