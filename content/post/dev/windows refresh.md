### Windows

- PATH : sauver et remettre (au moins C:\bin et C:\Users\thiba\dev\scripts\scripts)
- [Geek uninstaller](https://geekuninstaller.com/download) (apps & windows apps - fast)
- ubuntu
- windows terminal profiles
- windows start icons (screenshot)

- regedit overrides (ShellNew ..)
- [Restore windows 10 context menu](https://allthings.how/how-to-show-more-options-by-default-in-windows-11-file-explorer/#:~:text=If%20you%20ever%20want%20to,key%20and%20restart%20your%20computer.&text=Then%2C%20right%2Dclick%20the%20key,context%20menu%20on%20your%20system.)
- [Readd new > text file to context menu](https://superuser.com/questions/1685353/re-add-create-new-text-file-to-windows-11-context-menu)
- Windows terminal config file (back it up)

### Ableton setup

- live preferences (screenshot)
  - Audio : Input : 5/6 stereo, 7/8 mono
  - Output : 1/2 stereo, 3/4 mono (for usamo)
- [install focusrite 1st gen download](https://downloads.focusrite.com/focusrite/scarlett-1st-gen/scarlett-18i8-1st-gen)
  - don't forget to set the sound to max in focusrite control and reconfigure focusrite control
  - routing : ![image-20220727153821330](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220727153821330.png?token=AEHIPTMBOA7HBZ7RAPB3GL3C4FAA4)
- Loop Midi ports (names: see P0 backend Config) : P0_IN_MIDI, P0_IN_HTTP, P0_OUT, P0_BACKEND_LOOPBACK, REV2_AUX
- midi remote scripts
- stream deck profiles : -> saved here : C:\Users\thiba\google_drive\music\software presets\StreamDeck Elgato
- ProphetRev2 Editor : keep a copy : DO NOT REINSTALL on refresh
- live user library : change location
- See plugins reinstall links [here](https://docs.google.com/spreadsheets/d/14L4IwBuCZ3-GR_l-DN0vsgq_xhOSW_4kcWa5046AUW8/edit?usp=sharing)
- Options.txt is wiped

### Python

- env file of all projects
- Sentry, environment can only contain strings : need to set SENTRY_RELEASE env var : get it [here](https://sentry.io/organizations/thibaultlebrun/releases/?project=6573865)
- Are venv outdated ? Restore them including blog

#### Pycharm

- pycharm content roots. Readd : 
  - C:\Users\thiba\dev\ableton\Midi Remote Scripts Uncompyled 10
  - C:\Users\thiba\dev\ableton\AbletonLive-API-Stub\
- pycharm external tools
- pycharm settings (please export to file before refresh). Or enable sync and then disable it because it slows down the os
- French dictionnary : download [here](https://intellij-support.jetbrains.com/hc/en-us/community/posts/206844865-Spelling-Use-a-French-dictionary). Or better use editor > natural languages from Settings
- Custom dictionnary (typos) : export
- external tools config : [don't forget quotes](https://github.com/psf/black/issues/1299)



- [python launcher for windows](https://docs.python.org/3/using/windows.html#python-launcher-for-windows):(PY_PYTHON, nessary ?) and `ftype Python.File="C:\Python27\bin\python.exe" "%1" %*` ([see stack](https://stackoverflow.com/questions/8196314/how-do-you-change-file-association-for-py-python-files-in-xp)) for python lauching on 2 instead of 3
