# Windows Dualboot Time Issue

After entering the Windows installation from Ubuntu, the time was consistently wrong by the same number of hours. This, turns out, is caused by how Windows and Linux handle system time. Windows uses local time on the hardware clock while Linux uses UTC.

## The Solution

A quick Google search brings us to a [Reddit post](https://www.reddit.com/r/linuxquestions/comments/13qwk8r/dual_booting_windows_11_and_linux_every_time_i/) which gives a command that sets Windows to use UTC time instead of local time when reading from the hardware clock:
```powershell
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_DWORD /f
```
- Use in command prompt with administrator priveleges.
- `reg add` will add or modify a registry entry.
- `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation` is the registry to modify.
- `/v` sets the value name to `RealTimeIsUniversal`.
- `/d` sets the value data to `1`.
- `/t REG_DWORD` indicates the value type is a 32 bit number.
- `/f` forces the write.

Once this succeeds, Windows will read the RTC as UTC instead of local time.