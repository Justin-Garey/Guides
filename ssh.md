# SSH Tips

## SSH Keys

Using SSH keys allows you to login to other machines without a password. This saves tons of time and comes with little upfront cost. It is also considered more secure because you could then disable password login.

On the machine you plan to ssh from, run ```ssh-keygen```. This will create a new ssh key, most likely, in */home/\<user>/.ssh/id_rsa*. You can give it a different name than id_rsa so you know what it is being used for if you ever need to look in your .ssh directory. 

After creating the key, you can copy it to the remote machine with ```ssh-copy-id -i /home/<user>/.ssh/<key_name>.pub user@remote-addr```. You'll just have to enter your password, then next time you try to ssh in, no password will be needed. 

## Create an easy to remember name instead of the IP address

Instead of using ssh like ```ssh user@192.168.1.1```, add a name to */etc/hosts* so you can ```ssh user@name```. This is even simpler if your local user is the same, ```ssh name```.

Use ```sudo nano /etc/hosts``` to add a line with the ```192.168.1.1 name```. After saving, you are good to go.