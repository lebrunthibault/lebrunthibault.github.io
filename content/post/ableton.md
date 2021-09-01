---
title: "Ableton notes"
draft: true
---

# Ableton
- [download archives](https://www.ableton.com/en/download/archive/)

## Reinstall

- Install removes all the *C:\ProgramData\Ableton\Live 10 Suite\* directory. Including remote scripts
- Backup remote scripts or check nothing to commit
- Backup env file
- Install Ableton
- Change the env var ableton_version
- Copy back :
  - git clone protocol0 and **checkout dev** 
  - Protocol0 script with name **a_protocol_0**
  - Protocol0 midi script
  - Clyphx Pro
  - Push 2 procotol0 with name **a_push2**

Test code for remote script

```python
from _Framework.ControlSurface import ControlSurface

def create_instance(c_instance):  # noqa
    return ControlSurface(c_instance)
```

## Changing tempo from a midi clip in session view

> See [this video](https://www.google.com/search?q=ableton+use+clip+automation+in+session+view+tempo&sxsrf=ALeKk03sqbx6h2aMlrhmod7qNzUIMzUX4A:1630011657440&ei=CQEoYeG1GoedlwSt5rzoBA&start=0&sa=N&ved=2ahUKEwih3sjOys_yAhWHzoUKHS0zD004ChDx0wN6BAgBEEA&biw=1536&bih=722#kpvalbx=_AgEoYevHEsvwaMj1reAN41)

