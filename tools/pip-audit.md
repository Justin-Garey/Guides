# pip-audit

pip-audit is a scanning tool that reports known vulnerabilities within environment packages.

## Installation

```bash
pip install pip-audit
```

## Usage

- Support for CI/CD such as GitHub Actions
- Pre-commit support

Audit dependencies in the current environment:
```bash
pip-audit
```

Audit dependencies for a given requirements file:
```bash
pip-audit -r ./requirements.txt
```

Attempt to fix vulnerable packages:
```bash
pip-audit --fix
```

Perform a dry run before deciding to fix:
```bash
pip-audit --fix --dry-run
```

## Resources

- [PyPI Documentation](https://pypi.org/project/pip-audit/)