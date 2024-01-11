# Hosting A Skyfactory 3 Server on Ubuntu

Starting on [FTBs website](https://www.feed-the-beast.com/modpacks/server-files), we can find the server files for Skyfactory 3 by searching *skyfactory 3*.

After selecting Skyfactory 3, there will be a download option and an install script option.

I used the install script. The command to get the script looks like ```curl -JLO "https://api.modpacks.ch/public/modpack/25/123/server/linux" && chmod +x serverinstall_25_123```.

Before running the script, make a directory for the server. Mine is at ~/MinecraftServers/Skyfactory3. ```mkdir ~/MinecraftServers && mkdir ~/MinecraftServers/Skyfactory3 && cd ~/MinecraftServers/Skyfactory3```, then run the command to get the install script.

Next run the install script, ```./serverinstall_25_123```. Keep entering yes to the questions asked, then within a few seconds, your server will be installed.

There will be quite a few files and folders created. The most important file is the *start.sh* script. Run that to start the server, ```./start.sh```. The first time it runs, you will be asked if you agree to Minecrafts EULA. Just enter *y* for yes.

It might take a few minutes for the server to initialize. Now go ahead and pop open your skyfactory client and have fun!

## Tips

### Screen

Screen is a utility that can be used to run processes in the background so you can disconnect from the computer and the server will still be running.

Use ```sudo apt install screen``` to install.

Then just use ```screen``` to open an instance. 

After starting the server use ctrl+a, d to detach.

To resume the session, use ```screen -r```. This won't work if there are multiple sessions so use ```screen -ls``` to find the session id. Then ```screen -r id``` will get you into the session.