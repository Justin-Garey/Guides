# Mount a Samba Share in Ubuntu
## Install Support and Mount the Samba File Server

Ubuntu does not support the Common Internet File System (CIFS) by default and will need CIFS utilities installed.
```bash
sudo apt-get install cifs-utils
```

Once CIFS support is installed, the Samba file server can be mounted by specifying the type with `-t cifs` then passing int the server address and path as `//x.x.x.x/path` with the mount path on your device. The options are passed in with `-o options`. The following command sets the directories and files to have read, write, and execute permissions.
```bash
sudo mount -v -t cifs //<server-ip-address>/<location> <path-to-mount-to> -o guest,vers=2.0,dir_mode=0777,file_mode=0777,nounix
```

## Encountered Issues

### mount error(112)

`mount error(112): Host is down` with a comment on the SMB version possibly being a mismatch. This ended up being an entirely different problem. There was another device with the same username with the Samba share mounted. If the `user=<username>` was specified with a different username than the user on the device; or if the Samba share was unmounted on the other device, the Samba share can be mounted. I've modified one of the devices to use the command with the username specified:
```bash
sudo mount -v -t cifs //<server-ip-address>/<location> <path-to-mount-to> -o guest,vers=2.0,dir_mode=0777,file_mode=0777,nounix,user=<name>
```

## References

- Wikipedia page for [Samba](https://en.wikipedia.org/wiki/Samba_(software))
- Wikipedia page for [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)
