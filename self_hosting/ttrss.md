# TTRSS

> Tiny Tiny RSS (tt-rss) is a free, flexible, open-source, web-based news feed (RSS/Atom/other) reader and aggregator. ([tt-rss.org](https://tt-rss.org/))

RSS or Really Simple Syndication puts the latest news from a set of sources into one feed in an easy-to-read format.

Atom is a newer format than RSS that is xml based and has enhanced metadata.

## What Kinds of Feeds Are Available?

I'm not quite that interested in the news but I like to learn so I've added some blogs and news for my interests. I've also added Github releases as atom feeds. 

### Github Release As Atom Feed

To track release notes of Kavita, you can take the release page url (https://github.com/Kareadita/Kavita/releases) and append `.atom` to the end of it: (https://github.com/Kareadita/Kavita/releases.atom) which you would then paste into the feed URL in TTRSS. 

## Setup with Docker Compose

The installation [guide](https://tt-rss.org/docs/Installation-Guide.html) is very friendly.

First create an `.env` file:
```env
# Put any local modifications here.

APP_WEB_ROOT=/var/www/html/tt-rss
APP_BASE=

# Run FPM under this UID/GID.
# OWNER_UID=1000
# OWNER_GID=1000

# FPM settings.
# PHP_WORKER_MAX_CHILDREN=5
# PHP_WORKER_MEMORY_LIMIT=256M

# ADMIN_USER_* settings are applied on every startup.

# Set admin user password to this value. If not set, random password
# will be generated on startup, look for it in the 'app' container logs.
ADMIN_USER_PASS=admin

# Sets admin user access level to this value. Valid values:
# -2 - forbidden to login
# -1 - readonly
#  0 - default user
# 10 - admin
# ADMIN_USER_ACCESS_LEVEL=

# Auto create another user (in addition to built-in admin) unless it already exists.
#AUTO_CREATE_USER=
#AUTO_CREATE_USER_PASS=
#AUTO_CREATE_USER_ACCESS_LEVEL=0

# Default database credentials.
TTRSS_DB_USER=postgres
TTRSS_DB_NAME=postgres
TTRSS_DB_PASS=password

# You can customize other config.php defines by setting overrides here.
# See tt-rss/.docker/app/Dockerfile for a complete list.

# You probably shouldn't disable auth_internal unless you know what you're doing.
# TTRSS_PLUGINS=auth_internal,auth_remote
# TTRSS_SINGLE_USER_MODE=true
# TTRSS_SESSION_COOKIE_LIFETIME=2592000
# TTRSS_FORCE_ARTICLE_PURGE=30
# ...

# Bind exposed port to 127.0.0.1 to run behind reverse proxy on the same host.
# If you plan to expose the container, remove "127.0.0.1:".
HTTP_PORT=80
# HTTP_PORT=8280
```
- This has been modified from the base to have the admin password `admin`, to not use `tt-rss` in the base URL, and to be hosted on port 80.

Then create the Docker Compose file:
```yaml
services:
  db:
    image: postgres:18-alpine
    restart: unless-stopped
    env_file:
      - .env
    environment:
      - POSTGRES_USER=${TTRSS_DB_USER}
      - POSTGRES_PASSWORD=${TTRSS_DB_PASS}
      - POSTGRES_DB=${TTRSS_DB_NAME}
    volumes:
      - ./db:/var/lib/postgresql

  app:
    image: ghcr.io/tt-rss/tt-rss:latest
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./app:/var/www/html
      - ./config.d:/opt/tt-rss/config.d:ro
    depends_on:
      - db

  updater:
    image: ghcr.io/tt-rss/tt-rss:latest
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./app:/var/www/html
      - ./config.d:/opt/tt-rss/config.d:ro
    depends_on:
      - app
    command: /opt/tt-rss/updater.sh

  web-nginx:
    image: ghcr.io/tt-rss/tt-rss-web-nginx:latest
    restart: unless-stopped
    env_file:
      - .env
    ports:
      - ${HTTP_PORT}:80
    volumes:
      - ./app:/var/www/html:ro
    depends_on:
      - app

```
- I like to directly see the volumes so I put them as actual paths rather than creating them separately.

## Getting Started

Sign in with the admin account first. If the password is not set in the `.env` file then a random one will be generated and available in the logs.

Once signed in, RSS feeds can be added and categorized. For more customization click on the hamburger menu icon in the top right and select preferences.

## Email Setup

To set up email for TTRSS, use the [SMTP mailer plugin](https://github.com/tt-rss/tt-rss-plugin-mailer-smtp). 

## Backup

TTRSS provides [instructions](https://tt-rss.org/docs/Installation-Guide.html#manually-taking-a-backup) for taking a backup. This guide uses PostgreSQL 18+ so the manual method is used.

```bash
source .env
docker compose exec \
  -e PGPASSWORD="$TTRSS_DB_PASS" \
  db \
  /bin/bash \
  -c "export PGPASSWORD=$TTRSS_DB_PASS \
    && pg_dump -U $TTRSS_DB_USER $TTRSS_DB_NAME" \
  | gzip -9 > backup.sql.gz
```

## Restore

TTRSS also provides [instructions](https://tt-rss.org/docs/Installation-Guide.html#restoring-backups) for restoring the database.