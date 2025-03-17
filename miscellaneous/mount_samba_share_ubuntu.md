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
## References

- Wikipedia page for [Samba](https://en.wikipedia.org/wiki/Samba_(software))
- Wikipedia page for [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)