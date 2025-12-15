# Minecraft Docker Compose

Finally! An easy to use Docker Compose setup for a Minecraft server. The [GitHub](https://github.com/itzg/docker-minecraft-server) and [docs](https://docker-minecraft-server.readthedocs.io/en/latest/) are available. My current server runs vanilla but the image can also run paper, spigot, and mods.

The Docker Compose YAML:
```yaml
services:
  minecraft:
    image: itzg/minecraft-server:latest
    pull_policy: daily
    tty: true
    stdin_open: true
    ports:
      - "25565:25565"
    environment:
      EULA: "TRUE"
      VERSION: "1.21.10"
      WORLD: "World Name" # World Name
    restart: unless-stopped
    volumes:
      - ./data:/data
```
- If the world doesn't exist it will be created.
- If you want to use an existing world, just copy it to the data directory and specify the "World Name".