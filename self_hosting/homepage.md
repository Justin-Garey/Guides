# Homepage

[Homepage](https://gethomepage.dev/) is a highly customizable dashboard to centralize management and monitoring of services.

## Setup

### Simple Setup with Docker Compose

```yaml
services:
    homepage:
        image: ghcr.io/gethomepage/homepage:latest
        container_name: homepage
        volumes:
            - ./config:/app/config
        environment:
            - TZ=America/New_York
        # Host on port 80
        ports:
            - "80:3000"
        restart: unless-stopped
```

This will bring up the non-configured dashboard and you're ready to go!

### Using Tailscale Sidecar

If you are using [Tailscale](./tailscale.md) and want multiple services configured from a single Docker Compose file, then a Tailscale sidecar can be used to orchestrate the network for Homepage.

```yaml
services:
    homepage-ts-sidecar:
        image: tailscale/tailscale:stable
        container_name: homepage-ts-sidecar
        hostname: homepage
        cap_add:
            - NET_ADMIN
            - SYS_MODULE
        volumes:
            - ./tailscale-config:/config
            - ./tailscale-persistence/homepage:/var/lib/tailscale
        devices:
            - /dev/net/tun:/dev/net/tun
        environment:
            - TS_AUTHKEY=INSERT_AUTH_KEY
            - TS_STATE_DIR=/var/lib/tailscale
            - TS_EXTRA_ARGS=--login-server=LOGIN_SERVER_URL --accept-routes=true --reset --advertise-routes=100.64.0.0/24
            - TS_SERVE_CONFIG=/config/homepage-serve.json
        restart: unless-stopped
        healthcheck:
            test: ["CMD", "tailscale", "status"]
            interval: 10s
            timeout: 5s
            retries: 6
            start_period: 5s

    homepage:
        image: ghcr.io/gethomepage/homepage:latest
        container_name: homepage
        volumes:
            - ./homepage/config:/app/config
        environment:
            - TZ=America/New_York
            - HOMEPAGE_ALLOWED_HOSTS=TAILNET_ADDRESS # e.g. hompage.my-tailnet.com
        restart: unless-stopped
        network_mode: service:homepage-ts-sidecar
        depends_on:
            homepage-ts-sidecar:
                condition: service_healthy
```

The serve file:
```json
{
  "TCP": {
    "80": {
      "HTTP": true
    }
  },
  "Web": {
    "hompage.my-tailnet.com:80": {
      "Handlers": {
        "/": {
          "Proxy": "http://127.0.0.1:3000"
        }
      }
    }
  }
}
```