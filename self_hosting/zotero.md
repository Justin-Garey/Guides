# Zotero

## Self Hosting a Backup Server

A WebDAV server can be used to synchronize devices. This solution is simple and all that's needed on devices using Zotero is the information for connecting to the server. This removes the free data limit imposed by Zotero's online sync service. The only drawback is that you will not have a web interface to interact with your Zotero documents and notes.

The first method is fairly simple if using a NAS as it may already have WebDAV server functionality. Synology NAS's are confirmed to have WebDAV plugins.

An alternative for those who do not have a NAS is to set up a WebDAV server in a docker image. 
Some guides I found on others setting up a self hosted WebDAV server:
- [Self-hosting WebDAV Storage for Zotero](https://ism.engineer/technotes/self-hosted-zotero.html)
- [With tears and joy: backing up my precious data & self-hosting Zotero WebDAV](https://medium.com/@bbkilboz/with-tears-and-joy-backing-up-my-precious-data-self-hosting-zotero-webdav-cdc6fe707dbd)

## Self Hosting Zotero 

A more complete solution is to fully self host Zotero. There have been multiple implementations over the years with one of the most recent and upkept being [ZotPrime](https://github.com/uniuuu/zotprime). This can also be used by organizations that need an on-premise platform.