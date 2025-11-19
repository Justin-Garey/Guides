# Docker Scout

[Docker Scout](https://docs.docker.com/scout/) is an image analysis tool that can report packages and vulnerabilities within a package.

## CLI Installation

The simplest method from the [documentation](https://docs.docker.com/scout/install/) is to use the install script:
```bash
curl -fsSL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh -o install-scout.sh
sh install-scout.sh
```

## How to Use Docker Scout

The [CLI Reference](https://docs.docker.com/reference/cli/docker/scout/) contains good information on everything that can be done with an image, but I will focus on the `quickview` and `cves` subcommands.

### quickview

`docker scout quickview` displays a quick overview of an image. It can be done as:
```bash
docker scout quickview hello-world
```

### cves

`docker scout cves` will show any vulnerabilities found within the image and offer information on remediation if possible.
```bash
docker scout cves hello-world
```

Useful options include:
- `--only-fixed`
- `--only-unfixed`
- `--ignore-base`
- `--only-base`

## CI/CD

Docker Scout has prepared integration [configurations](https://docs.docker.com/scout/integrations/ci/) for GitHub Actions, GitLab, Microsoft Azure DevOps Pipelines, Circle CI, and Jenkins. It can be used to check for vulnerabilities in your development pipeline before software ever reaches the end users.