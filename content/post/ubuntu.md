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
  - create script in /*usr/lib/systemd/system-shutdown/* (as sudo) -> doesn't seem to work with python
  - or create a systemd service file (see [this](https://unix.stackexchange.com/questions/39226/how-to-run-a-script-with-systemd-right-before-shutdown)) 
    - IExecuting as my user : see [this](https://askubuntu.com/questions/676007/how-do-i-make-my-systemd-service-run-via-specific-user-and-start-on-boot)
    - Testing with : `sudo systemctl restart backup-repos.service && sudo systemctl stop backup-repos.service && sudo systemctl status backup-repos.service`
  - remodif

