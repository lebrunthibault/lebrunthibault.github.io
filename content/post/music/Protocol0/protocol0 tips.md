


# Reinstall

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


