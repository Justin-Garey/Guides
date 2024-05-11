# Stremio on Ubuntu

The following instructions are based on this Reddit [guide](https://www.reddit.com/r/StremioAddons/comments/yi5jdw/ultimate_guide_to_stremio_torrentio_rd/)

## Step 1: Install Stremio

Going to the [downloads](https://www.stremio.com/downloads) section of their website, there is a link to download the .deb package for Debian/Ubuntu. After that downloads, install stremio onto your system.

When going to launch for the first time, I encountered the error: ```error while loading shared libraries: libcrypto.so.1.1: cannot open shared object file: No such file or directory```. The fix comes from this [Stack Overflow answer](https://askubuntu.com/questions/1403911/stremio-doesnt-launch-on-ubuntu-22-04)
```
wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb

wget http://archive.ubuntu.com/ubuntu/pool/multiverse/f/fdk-aac/libfdk-aac1_0.1.6-1_amd64.deb 
sudo dpkg -i libfdk-aac1_0.1.6-1_amd64.deb
```

## Step 2: Real Debrid

The the service I use is [Real Debrid](https://real-debrid.com/). It's a paid service that subscribes to premium hosters giving the user better speeds and reliability when streaming or downloading content. Lengthier options are cheaper in the long term and will give you almost everything you could want without paying for the big streaming services.

## Step 3: Torrentio

Go to [Torrentio Lite - Stremio Addon](https://torrentio.strem.fun/lite/configure)

Towards the bottom of the page, select the "Debrid Provider" option and select "Real Debrid" from the drop-down menu. This will cause a new text box to appear underneath.

Copy the API key from this link https://real-debrid.com/apitoken and paste it into the "RealDebrid API Key**"** box

In the Debrid Options menu: Check the box "Don't show download to debrid links" and leave the other boxes unchecked.

Click "Install" at the bottom. It should open the Stremio app and prompt you with an "Install Addon" window. Click the green install button at the bottom. If it doesn't open up the stremio app, then paste your clipboard into the stremio search bar. The special addon link was copied when you hit "Install"

Optionally - In Stremio, click the puzzle piece in the top right to view your addons. Click "My Addons" and uninstall the "WatchHub" addon. It's an eyesore and it clutters your streams list.