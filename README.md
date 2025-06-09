# gitsint
### Installation

```
$ git clone https://github.com/fishystock/gitsint
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Usage

```
$ python3 gitsint.py --help
usage: gitsint.py [-h] repo_path

Extract emails and timezones from a local GitHub repository

positional arguments:
  repo_path   Path to the local GitHub repository

options:
  -h, --help  show this help message and exit
```

```
$ python3 gitsint.py /tmp/python3-ransomware
Fetching information from /tmp/python3-ransomware. This may take awhile on large repositories.
+--------------------------+-------------+
| Email                    |   Timezones |
+==========================+=============+
| ferrogiacomo26@gmail.com |       +0100 |
+--------------------------+-------------+
```
