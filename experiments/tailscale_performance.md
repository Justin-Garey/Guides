# How Well Does Tailscale Perform?
## Abstract

Using Tailscale as nodes and Headscale as a control server, the mesh VPN performance was tested using Ping and iPerf with (useless) Traceroute results available. Using the VPN on a home network added very little overhead and in the case of Ping, it was actually better. Thanks to Tailscale setting up the mesh network with WireGuard tunnels creating point-to-point connections, the network sees minimal performance overhead in the connections.
## What is Tailscale and Headscale?

Tailscale is a set of nodes that make up a mesh network and a control server that manages the network orchestration and authentication. A node will authenticate with the control server and create WireGuard tunnels to every other node in the network. To see more about Tailscale and setup, visit the [Tailscale Guide](../self_hosting/tailscale.md).

Headscale is the open source and self-hosted implementation of the Tailscale control server. To see more about Headscale and setup, visit the [Headscale Guide](../self_hosting/headscale.md).
## The Setup

For this test, Tailscale will be used as the software on client devices or *nodes* and Headscale will be used as the *control server*. The Tailscale nodes will be my laptop connected over Wi-Fi (Node A) and a server running on my home network connected over Ethernet (Node B). The Headscale control server is running on an Amazon EC2 t2.micro instance with 1 GiB memory and 1 vCPU.
## Expected Results

Tailscale should add minimal delay when the two nodes are on the same network. Based on how it operates using WireGuard and point-to-point (or node-to-node) links, it should mean little performance overhead.
## Test 1: Default Ping Comparison With Both Nodes on Same Network

### Ping Node B from Node A over home network with 64 bytes:
```bash
ping <node_b_address> -c 10 
```

Ping results:
```log
--- <node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 1.708/4.491/8.716/2.342 ms
```
### Ping Node B from Node A over Tailscale VPN with 64 bytes:
```bash
ping <tailscale_node_b_address> -c 10 
```

Ping results:
```log
--- <tailscale_node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9014ms
rtt min/avg/max/mdev = 2.637/7.192/28.536/7.174 ms
```
## Test 2: 2048 Byte Ping Comparison With Both Nodes on Same Network
### Ping Node B from Node A over home network with 2048 bytes:
```bash
ping <node_b_address> -c 10 -s 2048
```

Ping results:
```log
--- <node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9014ms
rtt min/avg/max/mdev = 4.755/8.880/16.801/3.654 ms
```
### Ping Node B from Node A over Tailscale VPN with 2048 bytes:
```bash
ping <tailscale_node_b_address> -c 10 -s 2048
```

Ping results:
```log
--- <tailscale_node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9011ms
rtt min/avg/max/mdev = 2.315/5.511/12.099/2.463 ms
```
## Test 3: 16384 Byte Ping Comparison With Both Nodes on Same Network
### Ping Node B from Node A over home network with 16384 bytes:
```bash
ping <node_b_address> -c 10 -s 16384
```

Ping results:
```log
--- <node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9010ms
rtt min/avg/max/mdev = 2.725/9.178/42.695/11.341 ms
```
### Ping Node B from Node A over Tailscale VPN with 16384 bytes:
```bash
ping <tailscale_node_b_address> -c 10 -s 16384
```

Ping results:
```log
--- <tailscale_node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 4.129/7.714/20.168/4.648 ms
```
## Test 4: Traceroute to Node B from Node A on Same Network

### Traceroute over home network:
```bash
traceroute <node_b_address>
```

Traceroute results:
```log
traceroute to <node_b_address> (<node_b_address>), 30 hops max, 60 byte packets
 1  <node_b_address> (<node_b_address>)  4.301 ms  4.780 ms  4.667 ms
```
### Traceroute over Tailscale VPN:
```bash
traceroute <tailscale_node_b_address>
```

Traceroute results:
```log
traceroute to <tailscale_node_b_address> (<tailscale_node_b_address>), 30 hops max, 60 byte packets
 1  <tailscale_node_b_address> (<tailscale_node_b_address>)  5.954 ms  5.882 ms  6.633 ms
```
## Test 5: iPerf3 with Node A as Client and Node B as Server
### Over home network with TCP:
```bash
iperf3 -c <node_b_address> --bidir -t 20
```

iPerf Results:
```log
[ ID][Role] Interval           Transfer     Bitrate         Retr
[  5][TX-C]   0.00-20.00  sec   442 MBytes   185 Mbits/sec    0             sender
[  5][TX-C]   0.00-20.01  sec   440 MBytes   185 Mbits/sec                  receiver
[  7][RX-C]   0.00-20.00  sec   517 MBytes   217 Mbits/sec    4             sender
[  7][RX-C]   0.00-20.01  sec   514 MBytes   215 Mbits/sec                  receiver
```
### Over Tailscale VPN with TCP:
```bash
iperf3 -c <tailscale_node_b_address> --bidir -t 20
```

iPerf Results:
```log
[ ID][Role] Interval           Transfer     Bitrate         Retr
[  5][TX-C]   0.00-20.00  sec   489 MBytes   205 Mbits/sec    6             sender
[  5][TX-C]   0.00-20.01  sec   486 MBytes   204 Mbits/sec                  receiver
[  7][RX-C]   0.00-20.00  sec   401 MBytes   168 Mbits/sec  345             sender
[  7][RX-C]   0.00-20.01  sec   398 MBytes   167 Mbits/sec                  receiver
```
## Test 6: Ping and Traceroute to Node B with Node A on a Mobile Hotspot

### Ping Node B from Node A over with 64 bytes:
```bash
ping <tailscale_node_b_address> -c 10 
```

Ping results:
```log
--- <tailscale_node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9013ms
rtt min/avg/max/mdev = 92.001/105.417/157.214/18.336 ms
```
### Ping Node B from Node A over with 2048 bytes:
```bash
ping <tailscale_node_b_address> -c 10 -s 2048
```

Ping results:
```log
--- <tailscale_node_b_address> ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 82.710/136.042/284.544/59.490 ms
```
### Traceroute:
```bash
traceroute <tailscale_node_b_address>
```

Traceroute results:
```log
traceroute to <tailscale_node_b_address> (<tailscale_node_b_address>), 30 hops max, 60 byte packets
 1  <tailscale_node_b_address> (<tailscale_node_b_address>)  88.787 ms  105.186 ms  105.201 ms
```
## Results

Traceroute, of course, returned only one hop since the VPN is communicating over a WireGuard tunnel so that metric is not very useful aside from telling us how long the connection takes.

The Ping results were interesting as when both devices were on the local network, `ping` was faster over the WireGuard tunnel for larger packet sizes.

The iPerf results were inconclusive at best. Over the home network, the downlink was better than that of the Tailscale VPN. The opposite was true of the uplink where the Tailscale VPN had more throughput than the home network.
## Conclusion

More usage is necessary to get a better picture but WireGuard itself is supposed to add very minimal overhead. Tailscale is supposed to work by creating a direct link between nodes meaning there should not be much, if any performance overhead when using services. So far this seems promising for usage of media and/or game servers over the Tailscale VPN.