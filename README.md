# fastapi template

[![DeepSource](https://app.deepsource.com/gh/vsecoder/fastapi-template.svg/?label=active+issues&show_trend=true&token=SiAXmF7RvOQMQkOmh1xrhSlu)](https://app.deepsource.com/gh/vsecoder/fastapi-template/?ref=repository-badge)
[![CodeFactor](https://www.codefactor.io/repository/github/vsecoder/fastapi-template/badge)](https://www.codefactor.io/repository/github/vsecoder/fastapi-template)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![PythonVersions](https://img.shields.io/pypi/pyversions/aiogram)


## Features

* ![fastapi](https://img.shields.io/badge/last-fastapi-green) as a main library
* ![tortoise](https://img.shields.io/badge/last-tortoise-yellow) as ORM

## Run

### Dev

```bash
git clone https://github.com/vsecoder/fastapi-template
cd fastapi-template
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp example.toml config.toml
nano config.toml # <= edit config
python3 -m app
```

### Prod

Enter from Dev and press ```Ctrl+C```

```bash
sudo nano /etc/systemd/system/fastapi.service
```

Enter this:

```
[Unit]
Description=FastApi
[Service]
WorkingDirectory=/home/<USERNAME>/fastapi-template
ExecStart=/home/<USERNAME>/fastapi-template/venv/bin/python3 -m app
Type=simple
Restart=always
RestartSec=1
User=<USERNAME>
[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable fastapi
sudo systemctl start fastapi # <= start bot
sudo systemctl status fastapi # <= get status

sudo systemctl stop fastapi # <= stop bot
```
