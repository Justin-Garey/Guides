# Debian Security Analyzer - debsecan

The [Debian Security Analyzer](https://wiki.debian.org/DebianSecurity/debsecan) can analyze installed packages on a system and report the vulnerabilities discovered. 

## Installation

```bash
sudo apt-get install debsecan
```

The above will ask about email preferences for the reports; it can otherwise be installed with:
```bash
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y debsecan
```

## Usage

Discover vulnerabilities on host packages:
```bash
debsecan
```

Useful Options:
- `--suite` is the release code name of the Ubuntu or Debian version. This is important for looking at the correctly looking up vulnerabilities.
- `--only-fixed` tells `debsecan` to only report fixable packages.

## Man Page Examples

Print all packages that can be fixed:
```bash
debsecan --suite suite --format packages --only-fixed
```
- `suite` is the release code name of the Ubuntu or Debian version.
- Use `lsb_release -cs` to get the code name.

Passing the list to apt-get can install the fixed packages
```bash
apt-get install $(debsecan --suite $(lsb_release -cs) --format packages --only-fixed)
```
- This one was modified from the man page example to include `lsb_release -cs`.

## Resources

- [Man Page](https://manpages.ubuntu.com/manpages/trusty//man1/debsecan.1.html)
- [Source Code](https://gitlab.com/fweimer/debsecan)