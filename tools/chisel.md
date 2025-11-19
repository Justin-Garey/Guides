# Canonical Chisel Tool

The [Chisel](https://documentation.ubuntu.com/chisel/en/latest/) tool is used to slice up packages within a docker container. The slices are sets of files based on the package information. These slices can then be removed from a Docker Container environment if it's unneeded. This can be helpful for making a Docker Container smaller and more secure.

## Installation

The Chisel tool [tutorial](https://documentation.ubuntu.com/chisel/en/latest/tutorial/getting-started/) will have the most up to date information on installation and usage. The steps are essentially:
1. Visit the [release page](https://github.com/canonical/chisel/releases/latest) for the latest release. 
2. Download with wget or curl
```bash
wget https://github.com/canonical/chisel/releases/download/v1.3.0/chisel_v1.3.0_linux_amd64.tar.gz
```
3. Extract the binary:
```bash
tar zxvf chisel_v1.3.0_linux_amd64.tar.gz
```
4. Install the tool:
```bash
sudo mv chisel /usr/local/bin
```
5. Verify the installation:
```bash
chisel
```
- This should output usage instructions.

## Chiseling a Docker File

Ubuntu provides a [guide](https://documentation.ubuntu.com/chisel/en/latest/how-to/use-chisel-in-dockerfile/) on how to do this with an Ubuntu image installing the python3 standard slice.