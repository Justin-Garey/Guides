# Cron

[Cron](https://en.wikipedia.org/wiki/Cron) is a command line tool for scheduling jobs that need to automatically happen at a predetermined time. An example of when to use Cron is for a server that should be rebooted once a week. Using this [Cron editor tool](https://crontab.guru/), I can plan a job to happen every Thursday at 3 A.M. with `0 3 * * 4`. The example from Wikipedia shows how the timing is configured:
```text
# * * * * * <command to execute>
# | | | | |
# | | | | day of the week (0–6) (Sunday to Saturday; 
# | | | month (1–12)             7 is also Sunday on some systems)
# | | day of the month (1–31)
# | hour (0–23)
# minute (0–59)
```

Back to rebooting a machine once a week on Thursday at 3 A.M., the job will look like:
```cron
0 3 * * 4 root /usr/sbin/reboot
```

Add this to */etc/crontab* with:
```bash
echo "0 3 * * 4 root /usr/sbin/reboot" | sudo tee --append /etc/crontab
```

Cron will figure out the rest and reboot the machine at the scheduled time.