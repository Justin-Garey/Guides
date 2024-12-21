# Install Node/npm on Ubuntu

*nodejs* can be installed on Ubuntu using apt but it will install an old version (As of writing this it is version 12). The best way to install node/npm is with the node version manager (nvm).

Start with an update and upgrade.
```bash
sudo apt update && sudo apt upgrade -y
```

The nvm source is [here](https://github.com/nvm-sh/nvm) on GitHub and has the updated release information. The install can be done with *curl* or *wget* and will look similar to:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

After installing, update your session by reloading the bashrc file.
```bash
source ~/.bashrc
```

Finally install Node and npm with:
```bash
nvm install --lts
```
- This installs the Long Term Support version.

Check the node and npm versions with:
```bash
node -v
npm -v
```