# USB Rubber Ducky with a Raspberry Pi Pico

These instructions are based on a Network Chuck [video](https://youtu.be/e_f9p-_JWZw?si=-Pi4_0Et5AeEkKTN) and the [pico-ducky](https://github.com/dbisu/pico-ducky) Github repo.

## Scripts

1. After following the instructions from the pico-ducky repository, I was able to start playing with some duckscript on my Linux machine to do some keystroke injection. It started with a simple [hello world in the terminal](./hello_world.dd)

2. My second and favorite script is a rick roll for Ubuntu. The [script](./linux_rick_roll.dd) downloads the zip file containing the song and will unzip it then play it in the background.

3. A reverse shell could always come in handy and would be fun to just have a proof of concept. 

4. Not sure how well it would work, but a password cracker would be possible.

## Notes so far
- The data will seem slower if the DELAYs are included. They are not needed even though the terminal looks a bit jumbled with them there.
- A ducky script doesn't necessarily need to run everything. It could be the injection point to download a malicious script which then runs in the background on your system. Better yet, the ducky script could create a red herring and hide something more malicious on the system.