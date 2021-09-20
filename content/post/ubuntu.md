---
title: "Ubuntu tricks"
draft: true
---

####  Install Jetbrains editor
> Use toolbox app

#### Desktop file

- go to `.local/share/applications/` and create .desktop file



#### Running commands at startup / shutdown

- startup: `crontab -e`
- shutdown : 
  - create script in /*usr/lib/systemd/system-shutdown/* (as sudo) -> **not working**
  - or create a systemd service file (see [this](https://unix.stackexchange.com/questions/39226/how-to-run-a-script-with-systemd-right-before-shutdown))

