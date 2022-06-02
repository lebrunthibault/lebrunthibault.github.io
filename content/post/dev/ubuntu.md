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
  - example: ` @reboot /home/thibault/bin/pull-blog.sh`
- shutdown : 
  - create script in /*usr/lib/systemd/system-shutdown/* (as sudo) -> doesn't seem to work with python
  - or create a systemd service file (see [this](https://unix.stackexchange.com/questions/39226/how-to-run-a-script-with-systemd-right-before-shutdown)) 
    - The executable path should be absolute 
    - IExecuting as my user : see [this](https://askubuntu.com/questions/676007/how-do-i-make-my-systemd-service-run-via-specific-user-and-start-on-boot)

Working solution for running python script as user:

`sudo vim  /etc/systemd/system/backup-repos.service`

```ini
[Unit]
Description=backing up my repos

[Service]
Type=oneshot
RemainAfterExit=true
User=thibault
Group=thibault
ExecStart=true
ExecStop=/usr/bin/python3 /home/thibault/bin/backup-repos.py

[Install]
WantedBy=multi-user.target
```

`sudo systemctl daemon-reload`

Test with :

`sudo systemctl restart backup-repos.service && sudo systemctl stop backup-repos.service && sudo systemctl status backup-repos.service`



# Keyboard

use setxkbmap

invert alt and win : setxkbmap -option altwin:swap_alt_win

### Fn Keys

see https://askubuntu.com/questions/818413/how-can-i-toggle-the-fn-function-key

reconfigure with 

```
sudo apt-get install keyboard-configuration
sudo dpkg-reconfigure keyboard-configuration
```



# Network

- port scan : nmap -p <port> <ip>
- who's pinging me : `sudo tcpdump -i ethX icmp` and `icmp[icmptype]=icmp-echo`
- who's listening on local : sudo netstat -plnt





# Storage

- Clean trash
- rm -rf ~/.local/share/Trash/*
- sudo apt-get clean
- sudo apt autoremove --purge
- sudo journalctl --vacuum-time=2d
- sudo purge-old-kernels;
  (nécessite package byobu)
- trash-empty
- bleach bit
