# Python Virtual Environments

A Python Virtual Environment (venv) exists on top of a base installation of Python but has its own packages installed as to not interfere or be burdened with bloat. This is especially useful when a quick python project or notebook is being made and there is not time to debug system installation issues.

Creating and activating the venv.
```bash
sudo apt install python3.10-venv
python3 -m venv my_venv
source my_venv/bin/activate
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