# iPerf3 Docker Compose Configuration

I've been repeatedly setting up an iPerf server for some testing and decided to make the server semi-permanent by adding it as a service to the docker compose configuration running on the same machine. It is contained in a [gist](https://gist.github.com/Justin-Garey/d0b3f1218290415e2f23298aa8b70f05) on GitHub.

```conf
services:
  iperf3-server:
    image: 'networkstatic/iperf3:latest'
    container_name: iperf3-server
    command: -s
    networks:
      privnet:
        ipv4_address: 10.10.10.10
        aliases:
          - iperf3
    ports:
      - "5201:5201"
```