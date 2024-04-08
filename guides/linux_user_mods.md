# Linux User Modifications

## Change a users username

```
usermod -l newusername oldusername
```
- When trying to do this over ssh, you will need to be logged in as root. Refere to [SSH Tips](./ssh.md) for instructions on how to ssh as root.
- This does not automatically change the users home directory to the new username. See below on how to do that.

## Move the users home directory

```
usermod -m -d /home/new-directory username
```
- You will most likely want to set *new-directory* to be the username but it can be nearly anything.