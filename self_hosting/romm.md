# RomM

ROM Manager (RomM) is a self hosted application that hosts your game collection. RomM uses EmulatorJS allowing you to play games of supported consoles right in the browser. The high level steps for setting up RomM include:
- Creating a IGDB account (using a Twitch account)
- Installing Docker and Docker Compose
- Organizing ROMs in a format readable by RomM
- Configuring and scanning once RomM is running
## Docker Compose

The Docker Compose file I used is similar to (with passwords and keys removed):
```yaml
services:
  romm:
    image: rommapp/romm:latest
    container_name: romm
    restart: unless-stopped
    environment:
      - DB_HOST=romm-db
      - DB_NAME=romm # Should match MARIADB_DATABASE in mariadb
      - DB_USER=romm-user # Should match MARIADB_USER in mariadb
      - DB_PASSWD= # Should match MARIADB_PASSWORD in mariadb
      - ROMM_AUTH_SECRET_KEY= # Generate a key with `openssl rand -hex 32`
      - IGDB_CLIENT_ID= # Generate an ID and SECRET in IGDB
      - IGDB_CLIENT_SECRET= # https://api-docs.igdb.com/#account-creation
      #- MOBYGAMES_API_KEY= # https://www.mobygames.com/info/api/
      #- STEAMGRIDDB_API_KEY= # https://github.com/rommapp/romm/wiki/Generate-API-Keys#steamgriddb
    volumes:
      - /home/justin/romm/resources:/romm/resources # Resources fetched from IGDB (covers, screenshots, etc.)
      - /home/justin/romm/redis_data:/redis-data # Cached data for background tasks
      - networkshare/Games:/romm/library # Your game library. Check https://github.com/rommapp/romm?tab=readme-ov-file#folder-structure for more details.
      - /home/justin/romm/assets:/romm/assets # Uploaded saves, states, etc.
      - /home/justin/romm/config:/romm/config # Path where config.yml is stored
    ports:
      - 80:8080
    depends_on:
      romm-db:
        condition: service_healthy
        restart: true

  romm-db:
    image: mariadb:latest
    container_name: romm-db
    restart: unless-stopped
    environment:
      - MARIADB_ROOT_PASSWORD= # Use a unique, secure password
      - MARIADB_DATABASE=romm
      - MARIADB_USER=romm-user
      - MARIADB_PASSWORD=
    volumes:
      - /home/justin/romm/mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      start_period: 30s
      start_interval: 10s
      interval: 10s
      timeout: 5s
      retries: 5
```
## ROM Organization

The RomM GitHub has a section on [Folder Structure](https://github.com/rommapp/romm?tab=readme-ov-file#folder-structure) and a separate page for [Supported Platforms](https://github.com/rommapp/romm/wiki/Supported-Platforms) which details the folder name for each system and where the scraped data for the games come from. To find out what formats are supported (likely all the major ROM formats are supported), you can check the [Supported Systems](https://emulatorjs.org/docs/systems) on EmulatorJS to see what cores are used. Once you know the core that is being used, you can verify that your ROM format works with that core.

I will update this as I update my library. The current file structure of my game library looks like:
```text
library/
├─ roms/
│  ├─ gb/
│  │  ├─ rom_1.gb
│  │  ├─ rom_2.gb
│  │
│  ├─ gba/
│  │  ├─ rom_1.gba
│  │  ├─ rom_2.gba
│  │
│  ├─ gbc/
│  │  ├─ rom_1.gbc
│  │  ├─ rom_2.gbc
│  │
│  ├─ n64/
│  │  ├─ rom_1.z64
│  │  ├─ rom_2.z64
│  │
│  ├─ nes/
│  │  ├─ rom_1.nes
│  │  ├─ rom_2.nes
│  │
│  ├─ ps/
│  |  ├─ my_multifile_game/
│  |  │   ├─ my_game.cue
│  |  │   ├─ my_game (Track 01).bin
│  |  │   ├─ my_game (Track 02).bin
│  |  │   ├─ my_game (Track 03).bin
│  |  │   ├─ my_game (Track 04).bin
│  │
│  ├─ snes/
│  │  ├─ rom_1.smf
│  │  ├─ rom_2.smf
│  │
│  ├─ virtualboy/
│     ├─ rom_1.vb
│     ├─ rom_2.vb
```
## Resources

- [RomM Github](https://github.com/rommapp/romm)
- [RomM Website](https://romm.app/)
- [EmulatorJS GitHub](https://github.com/EmulatorJS/EmulatorJS)
- [EmulatorJS Website](https://emulatorjs.org/)