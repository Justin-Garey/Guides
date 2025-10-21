# Issues Printing Application Installed by Snap

Snap packages by default have less permissions. In order to print from a Snap application, the `cups-control` must be connected.

## Brave Browser Could Not Print

I faced this problem for two years before finding out why and how to fix it. Just use this command and close out then reopen Brave. 

```bash
sudo snap connect brave:cups-control
```