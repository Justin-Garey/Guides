# [Tailscale](https://tailscale.com/)

Tailscale allows a user to set up a mesh VPN called the Tailnet. Each device on the network is considered a node and Tailscale manages a central control server for authentication and coordination. The links between nodes do not travel over the control server as lightweight tunnels are setup for point to point encryption creating a mesh network using WireGuard. The control server only handles data on the control plane and is very much like a hub and spoke networking model. The user plane is the mesh network where nodes are capable of peer to peer communication.

For users who don't want a 3rd party managing the authentication and coordination of their network, there is an open source option called [Headscale](./headscale.md). Headscale is the self hosted implementation of the Tailscale control server.
## Client Installation on Linux

1. Update and upgrade:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Add the apt repository and install Tailscale:
```bash
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/noble.noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/noble.tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list
sudo apt update
sudo apt install tailscale -y
```
## Helpful Linux Commands

To see the most recent logs Tailscale logs:
```bash
journalctl -u tailscaled | tail
```

## Tailscale Sidecar

The sidecar service can be used to aggregate services into a single Docker Compose and to improve security by only allowing the service on the Tailnet. Each service in a Docker Compose configuration will receive its own sidecar service. The sidecar must also be provided with a config file for how to serve the Docker service.

See the [Homepage](./homepage.md) configuration for more details on what a basic sidecar service looks like. 

If you are using [Headscale](./headscale.md), you will not be able to use the funnel feature but the serve configuration will still be functional.

### Resources

- [ScaleTail](https://github.com/2Tiny2Scale/ScaleTail): A repository full of examples.