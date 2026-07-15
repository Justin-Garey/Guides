# Gitea

Gitea is a self-hosted git server with web features for collaboration, review, and CI/CD. It is very similar to GitHub and is very inexpensive to use. Gitea is just git with a cup of tea.
## Setup with Docker Compose

I recommend using their [docs](https://docs.gitea.com/installation/install-with-docker) for the docker compose setup. It's pretty much copy and paste, then you are good to go.

I used the configuration with a MySQL database. The volumes cannot not use a networked file system, otherwise you will receive errors in the web configuration process. This ended up being my working configuration.
```yaml
services:
  server:
    image: gitea/gitea:1.22.3
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=db:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea
    restart: unless-stopped
    networks:
      gitea:
        ipv4_address: "10.100.100.2"
    volumes:
      - ./data:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "80:3000"
      - "2020:22"
    depends_on:
      - db

  db:
    image: mysql:8 
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=gitea
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=gitea
      - MYSQL_DATABASE=gitea
    networks:
      gitea:
        ipv4_address: "10.100.100.3"
    volumes:
      - ./mysql:/var/lib/mysql
    ports:
      - "3306:3306"

networks:
  gitea:
    ipam:
      driver: default
      config:
        - subnet: 10.100.100.0/24
```
## Initializing Gitea

Upon first accessing Gitea, you will be greeted with initial configuration settings. Most of these can be left as is, I did change the *Site Title* to something more suited towards me. Also set the *SSH_PORT* as *2020* to be in line with the above Docker Compose configuration. Make sure to leave the *SSH_LISTEN_PORT* as *22*. Next you will be able to register your account. The first registered account automatically gains admin privileges.

Now Gitea is ready to be used!
## Encountered Issues
### Unable to use ssh to clone or push a repository

While trying to push my first self hosted repository, I ran into an issue with how the given address was formatted. I was told to add the repository like so:
```bash
git remote add origin git@192.168.0.101:Justin-Garey/Notebook.git
git push -u origin main
```

The git repository should be in the format of ```ssh://it@192.168.0.101:2020/Justin-Garey/Notebook.git```. There are two steps to fixing this:
1. Set ```SSH_PORT``` to `2020` in *~/data/gitea/conf/app.ini*
2. Add `USE_COMPAT_SSH_URI = false` under `[repository]` in *~/data/gitea/conf/app.ini*
### While using a VPN with DNS, Gitea wants to clone from local network IP address

In *~/data/gitea/conf/app.ini*, set `DOMAIN`, `SSH_DOMAIN`, and `ROOT_URL` to use the domain name given to the server. In my case the server settings were changed to:
```ini
DOMAIN = gitea.micasa.local
SSH_DOMAIN = gitea.micasa.local
HTTP_PORT = 3000
ROOT_URL = http://gitea.micasa.local/
```

## Gitea Actions

[Gitea Actions](./gitea-actions.md) is just like GitHub Actions and enables CI/CD workflows. 

## Email Setup

Gitea provides their own [instructions](https://docs.gitea.com/administration/email-setup) on setting up email. 

To enable email, start a text editor into the *app.ini* file. This will enable usage through an SMTP server. Set this up easily with [Google SMTP](./google_smtp.md) and create an app password. Under the mailer section:
```conf
[mailer]
ENABLED = true
SMTP_ADDR = smtp.gmail.com
SMTP_PORT = 465
FROM = "Gitea Admin" <YOUR-GMAIL-ACCOUNT@gmail.com>
USER = YOUR-GMAIL-ACCOUNT@gmail.com
PASSWD = GENERATED-APP-PASSWORD
PROTOCOL = smtps
```
- Restart Gitea so the configuration takes effect.

Test the mail server in Gitea. Go to Gitea > Site Administration > Configuration > Summary -> Mailer Configuration. Enter an email to send to for the test and hit send. Once it's sent the page will refresh and a bar will appear at the top saying the email has been sent. 

Once that is working, enable notification settings (e.g. an issue was created). By default, the setting is false.
```conf
[service]
...
ENABLE_NOTIFY_MAIL = true 
...
```
- The configuration will take effect the next time Gitea restarts.

## Backup

I have a backup script to handle backing up the instance:

```bash
#!/bin/bash

# Ensure root permissions
sudo -v

# Get the time
TIME=$(date +"%Y-%m-%d_%H-%M-%S")

# Make the backups directory
mkdir -p backups

# Dump the Gitea configuration and database to a temporary directory within the Gitea container.
DUMPFILE=$(docker exec -u git -it -w /tmp $(docker ps -qf 'name=^gitea$') bash -c '/usr/local/bin/gitea dump -c /data/gitea/conf/app.ini' | awk '/Finish dumping in file/ {print $NF}')

DUMPFILE=${DUMPFILE//[[:space:]]/}

# Copy the dump file out from the Gitea container
docker cp $(docker ps -qf 'name=^gitea$'):$DUMPFILE ./backups

# Clear the tmp directory within the Gitea container
docker exec -u git -it -w /tmp $(docker ps -qf 'name=^gitea$') bash -c 'rm -rf /tmp/*'

# Copy backup to remote storage
mv ./backups/$(basename $DUMPFILE) ./backups/gitea-backup-$TIME.zip
```

## Restore

*NOTE*: These instructions are partially incomplete.

1. Use `scp` or another method to copy the zip to the new host.

2. Setup the Gitea instance.

2. Unzip, Copy, and Restore - do this step by step:

```bash
# Unzip
unzip gitea-dump-*.zip -d gitea-dump
cd gitea-dump

# Copy and restore the server files
docker cp ./data/. gitea:/data/gitea
cp -r repos/* ~/gitea/data/git/repositories/
docker exec --user git -it gitea bash
chown -R git:git /data

# Make account here on web interface - should this be done first?

/usr/local/bin/gitea -c '/data/gitea/conf/app.ini' admin regenerate hooks
exit

# Copy and restore the mysql db - Use the restore db instructions instead
docker cp ./gitea-db.sql gitea-db:/tmp/gitea-db.sql
docker exec -it gitea-db bash
mysql --default-character-set=utf8mb4 -uroot -pgitea gitea < /tmp/gitea-db.sql
exit
```