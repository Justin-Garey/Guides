# Dockhand

Dockhand is a simple and convenient docker container management system. I was specifically interested in a tool that could monitor the status of containers and check for updates on the images. Dockhand does both and more replacing common tools such as Portainer, Watchtower, Diun, WUD, Komodo, and more.

## Setup

Using Docker Compose, I went with the given example using Postgres and modified it to use a mapped volume rather than a managed volume.

```yaml
services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: dockhand
      POSTGRES_PASSWORD: changeme
      POSTGRES_DB: dockhand
    volumes:
      - ./dockhand/db:/var/lib/postgresql/data

  dockhand:
    image: fnsys/dockhand:latest
    ports:
      - 3000:3000
    environment:
      DATABASE_URL: postgres://dockhand:changeme@postgres:5432/dockhand
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./dockhand/data:/app/data
    depends_on:
      - postgres
    restart: unless-stopped
```

## Usage

For notifications, I went with email. I already have a [gmail address specifically for the SMTP service](./google_smtp.md). With that I just had to provide:
- Name: Mail
- SMTP Host: smtp.gmail.com
- Username: The email
- Password: An app password - see the note on [Google SMTP](./google_smtp.md) for how to make one.
- From email: The email
- From Name: Dockhand Alerts
- Recipients: The email(s) you want to send to

**Note**: The emails can get annoying if not configured correctly. I only need to know of failures and available updates, but by default, it will tell you every time a service comes online.

## Connecting A Remote Server

In Dockhand, under Settings, then Environment; locations for services to monitor can be added. To add a service that is on another, reachable machine, use the "Direct connection" *Connection type*. Then specify the host and the port. The port can be left at 2375 as the following instructions for how to expose it use that. This will need exposed on the machine the service is on.

### Expose Docker Daemon Port

Edit the *docker.service*
```
sudo systemctl edit docker.service
```

Add the service details:
```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375
```

Then reload and restart:
```
sudo systemctl daemon-reload
sudo systemctl restart docker.service
```

A reboot after is helpful if it is not available as expected.