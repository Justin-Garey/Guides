# Vikunja

[Vikunja](https://vikunja.io/) is a self-hosted to-do list app. It offers lists, Gantt, Kanban, and table views.

I was looking for something to track my to-do lists and have a Jira like interface with the kanban chart. This ended up being perfect, very simple and easy to use.

## Docker Compose

Setup is easy using the docker compose. After the docker containers are up, simply create an account and start your to-do list.

```yaml
services:
  vikunja:
    image: vikunja/vikunja
    environment:
      VIKUNJA_SERVICE_PUBLICURL: http://localhost:3456
      VIKUNJA_DATABASE_HOST: db
      VIKUNJA_DATABASE_PASSWORD: changeme
      VIKUNJA_DATABASE_TYPE: postgres
      VIKUNJA_DATABASE_USER: vikunja
      VIKUNJA_DATABASE_DATABASE: vikunja
      VIKUNJA_SERVICE_JWTSECRET: secret
    ports:
      - 3456:3456
    volumes:
      - ./files:/app/vikunja/files
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
  db:
    image: postgres:18
    environment:
      POSTGRES_PASSWORD: changeme
      POSTGRES_USER: vikunja
    volumes:
      - ./db:/var/lib/postgresql
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 2s
      start_period: 30s
```