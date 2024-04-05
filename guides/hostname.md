# Change your devices hostname

## Manually

I've only ever done it this way because I find it easier to modify some text rather than install a package to do it for me.

1. */etc/hostname* should only contain the hostname (**my-hostname**) of the device. 
2. */etc/hosts* will have more information but for debian based systems, the important declaration is ```127.0.1.1    my-hostname``` . On other systems, it will typically be ```127.0.0.1 localhost my-hostname```.

