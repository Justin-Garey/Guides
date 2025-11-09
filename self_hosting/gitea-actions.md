# Gitea Actions

Gitea Actions are designed to be fully compatible with GitHub actions. They can even be directly integrated from existing GitHub Action Workflows. 

## Set Up A Runner

The first step to start using Gitea Actions is to set up a runner. I've done this in a VM with a Docker Compose configuration. The VM has access to two cores and 2 GiB of memory. Before running the Docker Compose configuration, you will need to acquire the registration token from Gitea. The registration token can be found by:
- Clicking on the user icon in the top left
- Selecting Settings from the drop down menu
- Clicking on Actions -> Runners on the left side navigation menu
- Clicking on the Create new Runner button in the top right of the Runners Management window
- Copying the Registration Token

This should be included in the Docker Compose configuration along with a name for the runner, and the IP Address of Gitea:
```yaml
services:
  runner:
    image: gitea/act_runner:latest
    container_name: runner
    environment:
      - GITEA_INSTANCE_URL=http://<IP_ADDRESS_OF_GITEA>
      - GITEA_RUNNER_REGISTRATION_TOKEN=<TOKEN>
      - GITEA_RUNNER_NAME=<GIVEN_NAME
    restart: unless-stopped
    volumes:
      - ./data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    healthcheck:
      test: ["CMD", "curl", "-f", "http://<IP_ADDRESS_OF_GITEA>:80"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```
- Also included in this configuration is a healthcheck to see if Gitea is up before starting the Runner.