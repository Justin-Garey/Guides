# How to Kill a Process Taking Up a Port on Ubuntu
## Find and Kill the Process

```bash
sudo kill -9 $(sudo lsof -t -i:2592)
```
### What's it Doing?

The first part of the command `sudo kill -9` sends the signal *SIGKILL* to the specified process. The PID or process identifier is retrieved with the `$(sudo lsof -t -i:2592)`. Using command interpolation the PID is passed into the `kill` command.

The PID of the process on port *2592* is returned from `sudo lsof -t -i:2592`. The `lsof` (list open files) command, with the `-t` option, will output only the process identifier. The option `-i:2592` selects the files which match the specified port *2592*.
### References

- Solution comes from this [answer](https://stackoverflow.com/questions/9346211/how-to-kill-a-process-on-a-port-on-ubuntu/9346231#9346231) to a [question](https://stackoverflow.com/questions/9346211/how-to-kill-a-process-on-a-port-on-ubuntu) posted on Stack Overflow.