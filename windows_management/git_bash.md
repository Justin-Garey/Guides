# Git Bash

After installing Git Bash, Git can then be used. For SSH connections, there is some extra setup required. Thanks to this [guide](https://gist.github.com/bsara/5c4d90db3016814a3d2fe38d314f9c23) on GitHub, it was up and running in no time. The following primarily that guide but with some modifications for quicker setup.

## Prepararation

Launch Git Bash and at the root of your user directory, create a directory `.ssh` and the files `.ssh/config`, `.bash_profile`, `.bashrc`:
```bash
cd ~
mkdir .ssh
touch .ssh/config
touch .bash_profile
touch .bashrc
```

## Create a New SSH Key

Follow the steps in the section named "Generating a new SSH
Key" found in the following documentation from GitHub:
*[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows#generating-a-new-ssh-key)*

From that documentation: `ssh-keygen -t ed25519 -C "your_email@example.com"`


## Configure SSH for Git Hosting Server

Add the following text to `.ssh/config`

```
Host github.com
 Hostname github.com
 IdentityFile ~/.ssh/id_ed25519
```
- The `Host` and `Hostname` can just be the domain of whatever Git service you are using. 
- This tells the ssh process where to find your credentials for the service.
- This block can be repeated in the `.ssh/config` for multiple Git services or accounts.


## Enable SSH Agent Startup Whenever Git Bash is Started

First, ensure that following lines are added to `.bash_profile`,
which should be found in your root user home folder:

```sh
test -f ~/.profile && . ~/.profile
test -f ~/.bashrc && . ~/.bashrc
```

Now, add the following text to `.bashrc`, which should be found
in your root user home folder:

```sh
# Start SSH Agent
#----------------------------

SSH_ENV="$HOME/.ssh/environment"

function run_ssh_env {
  . "${SSH_ENV}" > /dev/null
}

function start_ssh_agent {
  echo "Initializing new SSH agent..."
  ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
  echo "succeeded"
  chmod 600 "${SSH_ENV}"

  run_ssh_env;

  ssh-add ~/.ssh/id_ed25519;
}

if [ -f "${SSH_ENV}" ]; then
  run_ssh_env;
  ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
    start_ssh_agent;
  }
else
  start_ssh_agent;
fi
```

## Other Notes

### Launch Git Bash from Powershell

```powershell
& 'C:\Program Files\Git\bin\bash.exe' --login -i
```
- The call operator `&` runs the command that follows it.
- `--login` starts the shell as a login shell.
- `-i` puts the shell in interactive mode.