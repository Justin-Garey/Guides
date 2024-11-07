# Set Your Default Shell

Sometimes you'll get bored of your current shell or a new system uses `sh` instead of `bash` by default (like in [Proxmox](../self_hosting/proxmox.md) for a new user). So you'll want to change the default shell. For example, to change to `bash`:

```sh
chsh -s $(which bash)
```