# USB Rubber Ducky with a Raspberry Pi Pico

These instructions are based on a Network Chuck [video](https://youtu.be/e_f9p-_JWZw?si=-Pi4_0Et5AeEkKTN) and the [pico-ducky](https://github.com/dbisu/pico-ducky) Github repo.

## Scripts

1. After following the instructions from the pico-ducky repository, I was able to start playing with some duckscript on my Linux machine to do some keystroke injection. It started with a simple [hello world in the terminal](./hello_world.dd)

2. My second and favorite script is a rick roll for Ubuntu. The [script](./linux_rick_roll.dd) downloads the zip file containing the song and will unzip it then play it in the background.

3. A [reverse shell](./linux_rev_shell.dd) could always come in handy and would be fun to just have a proof of concept. Some modifications may be needed such as the IP address to connect to. The script creates a Bash TCP connection sort of in the background which can connect to the attackers machine using ```nc -lvp 4242```. It's very simple and can be very fast. 

## Potential Creations

1. A brute force password cracker would be simple to create but probably not that useful.

2. This could also be used to play a game. It would be more of a novelty program but cool to have.

3. Some more malicious things I could do with this are password extractions, system wipes, lock users out, and command replacements.

## Notes
- The data will seem slower if the DELAYs are included. They are not needed even though the terminal looks a bit jumbled with them there.
- A ducky script doesn't necessarily need to run everything. It could be the injection point to download a malicious script which then runs in the background on your system. Better yet, the ducky script could create a red herring and hide something more malicious on the system.