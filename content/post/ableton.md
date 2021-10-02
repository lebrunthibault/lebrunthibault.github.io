---
title: "Ableton notes"
draft: true
---

- [download archives](https://www.ableton.com/en/download/archive/)



# Reducing latency when monitoring

> See [focusrite article](https://focusrite.com/en/news/system-science-part-2-drivers-latency)

- Best solution : use an external mixer that feeds in the audio soundcard and monitor directly to the mixer (analog signal path). *Complicated for me*
- Usual solution: use direct monitoring in the sound card BUT we get the A/D + D/A latency
- Anyway: record in ableton with monitoring off

# Recording external synth with no latency

> See [this video about audio latency](https://www.youtube.com/watch?v=PT5mD2Zd7F8), [this one about midi to audio latency](https://www.youtube.com/watch?v=WkQkzBB6Szc) and [Ableton doc](https://help.ableton.com/hc/fr-fr/articles/360006569179-Le-monitoring-dans-Live)

**Monitoring modes**

- In : signal toujours entendu mais avec latence 
- Auto: signal entendu seulement quand track arm avec latence
- Off : signal non entendu, zero latence

>  With In or Auto: live aligns the audio with what's *heard* (input + output latency)
>
> With off : it's aligned with what you play (delay compensation of soundcard / driver latency and of plugin latency

**Options > Delay compensation**

- Compensates for plugins / effects latency. **leave it on**.
- NB: effect latency is show in the status bar when hovering over effect. 
- All the tracks are started as to sync with the most delayed one
- NB : disabling a plugin does not remove its latency while delay compensation if on (it does when it's off)

**Options > Reduced latency when monitoring**

- For audio tracks, deactivates delay compensation for this track.
- track will start **before** other tracks if it's total effect latency if < the most delayed track
- NB: it is not the same as direct monitoring, the tracks is still heard after all effect processing is done (thus with its own effect latency, as well as master) but is not affected to other tracks own latencies.

**External instrument**

- Adds a latency equals to the system latency (in + out as seen in Preferences > audio > latency)
- record audio by :
  - freezing the track !
  - adding a new audio track

**Recording direct audio (without feeding midi)**

> I'm actually not doing this

- Use monitoring **off** and use soundcard direct monitoring **or** use another track for monitoring (with monitor auto or in).

#### Recording audio by sending midi with no latency and low jitter

- Driver error compensation : **-27ms** to make it work with rev2 (minitaur doesn't need). NB more compensation pushes forward the audio and inversely.

- Buffer size: **128 samples**
- Sample rate : **88200Hz**

**Minitaur**

- Midi track with **external instrument**
- external instrument hardware latency : inverse of driver error compensation (e.g. **27ms**)
- Audio track taking audio from midi track **pre fx**

**Prophet**

- Midi track with **external audio effect**
- external instrument hardware latency : **0ms**
- Audio track taking audio from midi track **post fx** (because we use external audio effect)

# Midi jitter

- Around 10ms at SR 44100
- Around 5ms at SR 88200
- High SR + low buffer size = 2 ms !

**Solution**

- High SR
- Low buffer size

**More**

- Check out focusrite windows optimizing [tutorial](https://support.focusrite.com/hc/en-gb/articles/207355205-Optimising-your-PC-for-Audio-on-Windows-10)

#### Should I use a midi interface ? Possibilities are 

- [E-RM Midi clock](https://www.thomann.de/fr/e_rm_midiclock.htm) : horloge maitre externe mais pas utile pour envoyer du midi aux synthés ?
- [Roland UM-One MkII](https://www.thomann.de/fr/roland_um_one_mkii.htm) : cable usb to 2 * midi : peut permetttre de réduire le jitter de l'ordi au synth par rapport a un cable usb normal
- Use a high end audio soundcard using pll (focusrite [jetpll](https://pro.focusrite.com/what-is-jetpll))
- [Expert sleeper USAMO](https://www.thomann.de/fr/expert_sleepers_usamo.htm): 

# Clean sidechain compression

> See [this video](https://www.youtube.com/watch?v=Gc4pehOp-Y4)

#### Using compressor

> Good for dynamic source, simpler to setup

- sidechain input pre-fx
- Ratio infinite
- attack the lowest possible without artefacts
- detection mode: peak (especially for drums)

#### Using LFOTool

> Good for source with fixed velocity

- Do not send directly midi to the lfo tool 
  - create a midi track with an external instrument to have **latency compensation** and copy paste midi notes
  - one midi track and one lfo tool per sidechain source
- Lfo tool midi conf: note retrigger in **env** mode
- handle clipping on attack : use **smooth** param but sometimes it's good to add punch
- Make it less aggresive by using the **split** button (down right).



# Changing tempo from a midi clip in session view

> See [this video](https://www.google.com/search?q=ableton+use+clip+automation+in+session+view+tempo&sxsrf=ALeKk03sqbx6h2aMlrhmod7qNzUIMzUX4A:1630011657440&ei=CQEoYeG1GoedlwSt5rzoBA&start=0&sa=N&ved=2ahUKEwih3sjOys_yAhWHzoUKHS0zD004ChDx0wN6BAgBEEA&biw=1536&bih=722#kpvalbx=_AgEoYevHEsvwaMj1reAN41)

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
