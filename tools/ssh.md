# SSH Tips

## SSH Keys

Using SSH keys allows you to login to other machines without a password. This saves tons of time and comes with little upfront cost. It is also considered more secure because you could then disable password login.

On the machine you plan to ssh from, run ```ssh-keygen```. This will create a new ssh key, most likely, in */home/\<user>/.ssh/id_rsa*. You can give it a different name than id_rsa (mine is called *home_id*) so you know what it is being used for if you ever need to look in your .ssh directory.

After creating the key, you can copy it to the remote machine with `ssh-copy-id -i /home/<user>/.ssh/<key_name>.pub user@remote-addr`. You'll just have to enter your password, then next time you try to ssh in, no password will be needed.

## Create an Easy to Remember Name Instead of the IP Address

Instead of using ssh like ```ssh user@192.168.1.1```, add a name to */etc/hosts* so you can ```ssh user@name```. This is even simpler if your local user is the same, ```ssh name```.

Use ```sudo nano /etc/hosts``` to add a line with the ```192.168.1.1 name```. After saving, you are good to go.

## Simply Login as a Different User

If you are constantly logging in to other computers as a different user, it may be useful to set up a record for that. After creating a hostname for the IP address, an entry can be added to *~/.ssh/config* to make the user ["persistent per-host"](https://superuser.com/a/306159). Start with ```sudo nano ~/.ssh/config``` and add the record.

```conf
Host simple_name
User username
Hostname pc_hostname_or_static_ip_address
```

Now using ```ssh simple_name``` will take you to *username@pc_hostname_or_static_ip_address*

## Enable Root Login Over SSH

**NOTE: This is not recommended and should only be used for a minute amount of time or in a pinch**

Performing as root, start by modifying */etc/ssh/sshd_config*
```bash
nano /etc/ssh/sshd_config
```

In the Authentication section, add a new entry ```PermitRootLogin yes```.

```conf
# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10
```
- Here its just been added under the commented default entry.

After saving the file, restart the sshd server with `service sshd restart`.

**Remember to remove the added line after completing your task**

This guide was created based on [Red Hats Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/v2v_guide/preparation_before_the_p2v_migration-enable_root_login_over_ssh)
