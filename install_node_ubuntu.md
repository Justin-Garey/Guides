# Install Node/npm on Ubuntu

*nodejs* can be installed on Ubuntu using apt but it will install an old version (As of writing this it is version 12). The best way to install node/npm is with the node version manager (nvm).

Start with an update and upgrade.
```
sudo apt update && sudo apt upgrade -y
```

The nvm source is [here](https://github.com/nvm-sh/nvm) on Github and has the updated release information. The install can be done with *curl* or *wget* and will look similar to:
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

After installing, update your session by reloading the bashrc file.
```
source ~/.bashrc
```

Finally install Node and npm with:
```
nvm install --lts
```
- This installs the Long Term Support version.

Check the node and npm versions with:
```
node -v
npm -v
```