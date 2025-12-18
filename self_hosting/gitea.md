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