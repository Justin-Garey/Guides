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

## Exit Node

An exit node is used to route all public internet traffic through a node on the Tailnet. This is useful for instances where you have an untrusted Wi-Fi network or are away from home. This essentially sets the default routes to the exit node and is similar to using a traditional VPN.

### Advertise a Device as an Exit Node

- [Tailscale Documentation](https://tailscale.com/docs/features/exit-nodes?tab=linux#advertise-a-device-as-an-exit-node)

For a Linux device as the exit node, first enable IP forwarding:

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```

Now set the advertising flag and re-up Tailscale, assuming Tailscale has already been set up:

```bash
sudo tailscale set --advertise-exit-node
sudo tailscale down
sudo tailscale up
```

### Allow the Exit Node

#### Tailscale Admin Console

From [Tailscale Documentation](https://tailscale.com/docs/features/exit-nodes?tab=linux#allow-the-exit-node-from-the-admin-console):

>- Open the Machines page of the admin console and locate the exit node.
>- Locate the Exit Node badge in the machines list or use the property:exit-node filter to list all devices advertised as exit nodes.

#### Headscale Setup

- [Headscale Documentation](https://tailscale.com/docs/features/exit-nodes?tab=linux#allow-the-exit-node-from-the-admin-console)

Get the Headscale routes:

```bash
sudo headscale nodes list-route
```

Output should be similar to:

```log
ID | Hostname | Approved | Available | Serving (Primary)
18 | e-node   |          | 0.0.0.0/0 |                  
   |          |          | ::/0      |  
```

Enable routes for the advertised node (e-node):

```bash
sudo headscale nodes approve-routes --identifier 18 --routes 0.0.0.0/0
```

Verify the node is enabled:

```bash
sudo headscale nodes list-route
```

Output should be similar to:

```log
ID | Hostname | Approved  | Available | Serving (Primary)
18 | e-node   | 0.0.0.0/0 | 0.0.0.0/0 | 0.0.0.0/0        
   |          | ::/0      | ::/0      | ::/0             
```

### Set the Exit Node

Nodes do not use the exit node by default. They must be set to use the node.
- [Tailscale Documentation](https://tailscale.com/docs/features/exit-nodes?tab=ios#use-the-exit-node)

#### On Linux

```bash
sudo tailscale set --exit-node e-node
```

- The exit node can be set using the node IP or hostname.

To continue allowing LAN access:

```bash
sudo tailscale set --exit-node e-node --exit-node-allow-lan-access true
```

To stop using an exit node:
```bash
sudo tailscale set --exit-node=
```

#### On iOS

The Tailscale app on iOS has a drop down menu at the top of the screen for exit node selection. From here, *allow LAN access* can also be enabled.

#### On Windows

Select the Tailscale icon and select *Use exit node*. Then select the machine name of the exit node. The *Allow local network access* can also be enabled.

### Resources

- [ScaleTail](https://github.com/2Tiny2Scale/ScaleTail): A repository full of examples.