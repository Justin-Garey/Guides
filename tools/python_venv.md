# Python Virtual Environments

A Python Virtual Environment (venv) exists on top of a base installation of Python but has its own packages installed as to not interfere or be burdened with bloat. This is especially useful when a quick python project or notebook is being made and there is not time to debug system installation issues.

Creating and activating the virtual environment:
```bash
sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
```
- First the venv package is installed for your version of python.
- Then a venv is created and activated.

To use the venv with Jupyter Notebook, do this after creating and activating the venv
```bash
pip install jupyter
ipython kernel install --user --name=venv
jupyter notebook
```
- Now that your session is within the venv, install Jupyter.
- Set up iPython and run the Jupyter server.

Personally, I've been using Jupyter notebook in VSCode. When selecting the version of Python for the notebook, a running notebook server from a venv can be selected.

## Create a Specific Versioned Virtual Environment

This comes in handy when a program requires a different Python version than the one used as default on your system. For example, if your system uses Python 3.10 and a program requires Python 3.12, after installing Python 3.12:

```bash
python3.12 -m venv .venv
```

## Install Packages within the Virtual Environment

The virtual environment provides the Python executables including pip, a requirements file can simply be passed in to the virtual environments executable.

```bash
.venv/bin/pip install -r requirements.txt
```