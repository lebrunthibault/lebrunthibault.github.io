---
title: "Windows tricks"
draft: true
---

# Windows tricks

- [Pin to start any file](https://answers.microsoft.com/en-us/windows/forum/all/pin-to-start-any-file-windows-10-pro/acb769bc-e5d9-4be9-8a76-0aff7cdab6c8)
- [Execute task at logon](https://www.tenforums.com/tutorials/173596-how-create-task-run-app-script-logon-windows-10-a.html): using task scheduler
- [Execute task at restart](https://superuser.com/questions/773651/run-a-script-just-before-shutdown-or-reboot-on-windows-home-edition): Group policy editor (gpedit.msc) > User configuration > Windows Settings > Startup / Shutdown
- [Run program as administrator](https://www.digitalcitizen.life/run-as-admin/)
  - See Point 12 for having a program always execute as admin
- [Edit the context menu "New" options](https://www.youtube.com/watch?v=dJes3l_VW70)




# Audio

**Links :**

- Interesting article about multiple audio interfaces : https://www.soundonsound.com/techniques/using-multiple-audio-interfaces-together
- Windows audio architecture : https://docs.microsoft.com/en-us/windows-hardware/drivers/audio/windows-audio-architecture
- Wasapi example code : https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/WindowsAudioSession
- Windows vs linux audio : https://www.learndigitalaudio.com/how-linux-audio-works-vs-windows-audio-2017Sound control panel : https://oxen.tech/blog/using-sounds-settings-control-panel/

**Drivers :**

- Asio, Windows Core Audio (using WASAPI)

To use a professional audio interface in Windows you will need to download the drivers from the manufacturers web site and install them. These will almost certainly include an ASIO driver. This type of special driver created by Steinberg will bypass the operating system as much as is possible and enable low latency high quality sound. 

There will probably be another driver included for general Windows use. This is for software that does not support ASIO, and it will probably be Windows Core Audio which uses WASAPI. This is the current type of driver used in Windows 10, and supersedes **MME (1991), DirectSound (1995), and WDM (1998).**

Windows Core Audio can also bypass the operating system as much as is possible, and get low latency in ‘exclusive’ mode, but ASIO is still the most widely used pro audio standard.

![img](https://lh4.googleusercontent.com/pkTV0y4Rs0pWWgSc-BtHAX3SMVfre1DtmwMpD6UIoa8mKqeGDO4XMnVvIpN2NJ_3WHZafLw5amwovg07Vz3H6Qtt3L_DSY7mH6T_vR-GZ_GL5Q0kV3bnv8TJl9CQCQBVEfXZAt7d=s0)https://msdn.microsoft.com/library/windows/desktop/dd742875)



# Free space on C:

Install ubuntu on D: see https://kontext.tech/column/tools/308/how-to-install-windows-subsystem-for-linux-on-a-non-c-drive

Move Pagefile.sys or delete it : https://www.ionos.fr/digitalguide/serveur/configuration/pagefilesys/

Remove hiberfile.sys ? https://www.commentcamarche.net/informatique/windows/227-supprimer-le-fichier-hiberfil-sys-de-windows/



# Windows is slow, GPU spikes

- https://www.windowsphoneinfo.com/threads/desktop-window-manager-random-gpu-spikes.460412/
- https://windowsreport.com/desktop-window-manager-high-gpu/#:~:text=On%20Windows%2010%2C%20type%20in,Select%20Search%20automatically%20for%20drivers.
- Use nvidia control panel to change the gpu
- Edit System Configuration > Services



# Windows reinstall / refresh

### Microsoft Visual C++ 14.0 missing (when install pyton -rtmidi)

- Install [Visual studio installer](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)
- Workload : Desktop Development with C++
- MSVC v142 - VS 2019 + Windows 10 SDK

# Stress tests

- See [this](https://appuals.com/how-to-run-a-computer-performance-benchmark-test-on-windows/)
- Win-R : `perfmon /report` : general testing. Supposed to take 1 min but takes much longer (20 min ..?)
- or [Prime95](https://www.mersenne.org/download/#download) : cpu tests



# Cleaning steps

- Defrag ssd with smart defrag 8 by IO bits