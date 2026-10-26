# USB Rubber Ducky with a Raspberry Pi Pico

These instructions are based on a Network Chuck [video](https://youtu.be/e_f9p-_JWZw?si=-Pi4_0Et5AeEkKTN) and the [pico-ducky](https://github.com/dbisu/pico-ducky) Github repo.

## Scripts

1. After following the instructions from the pico-ducky repository, I was able to start playing with some duckscript on my Linux machine to do some keystroke injection. It started with a simple [hello world in the terminal](./hello_world.dd)

2. My second and favorite script is a rick roll for Ubuntu. The [script](./linux_rick_roll.dd) downloads the zip file containing the song and will unzip it then play it in the background.

3. A [reverse shell](./linux_rev_shell.dd) could always come in handy and would be fun to just have a proof of concept. Some modifications may be needed such as the IP address to connect to. The script creates a Bash TCP connection sort of in the background which can connect to the attackers machine using ```nc -lvp 4242```. It's very simple and can be very fast. 

4. I've created some more maliciously aligned scripts such as getting the linux filesystem structure, getting ssh credentials - the private keys, getting environment and configuration settings which often have API keys, and getting any available cloud credentials. For these I'm only printing out the found information rather than having a whole setup to send it or retrieve it for later use.

5. I made a game that's not really a game, it just says it's a game then tells you it's stealing your bitcoin funds.

6. I realized that ASCII art would be a cool way to use this so I made a generate script for creating an ASCII star ducky script file. 

## Potential Creations

1. A brute force password cracker would is not effective with modern lockouts on most systems. The Bad USB has no way of knowing that a lockout has occurred or if extra steps are required such as on Windows after inputting an incorrect pin multiple times, it requires you to type out a string before continuing.

2. The most useful aspect of this may actually be in its ability to basically be a script without being a script. If you ever have to start working on new devices and can't download or copy over your setup scripts, this could be used to replace that setup since it's essentially a keyboard automation and won't impact any security requirements.

3. Some more malicious things that could be done with this are password extractions, system wipes, lock users out, and command replacements. I've attempted some of this as just printing out the information to see what it actually accesses and how useful it would be.

## Notes
- The data will seem slower if the DELAYs are included. They are not needed even though the terminal looks a bit jumbled with them there.
- A ducky script doesn't necessarily need to run everything. It could be the injection point to download a malicious script which then runs in the background on your system. Better yet, the ducky script could create a red herring and hide something more malicious on the system.