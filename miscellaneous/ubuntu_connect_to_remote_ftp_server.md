# Connect to a Remote FTP Server from Ubuntu
## From the Files App

In the Files App, under `Other Locations`, you can connect to a remote server by pasting in the address in the bottom bar.
![Connect to remote file server](files_connect_remote_server.png)
## From the CLI

Install `curlftpfs`:
```
sudo apt install curlftpfs
```

Create a directory to use:
```
mkdir ~/RemoteFTP
```

Connect the remote storage to the created folder:
```
curlftpfs <user>:<pass>@ftp://<address>:<port> ~/RemoteFTP
```

## Remove the FTP Directory from the CLI

```
umount ~/RemoteFTP
```