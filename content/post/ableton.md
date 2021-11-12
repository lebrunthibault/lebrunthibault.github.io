---
title: "Ableton notes"
draft: true
---

- [download archives](https://www.ableton.com/en/download/archive/)



# Bugs

- Minitaur editor disconnected :
  - only minitaur out / track is necessary
  - **simply reload the minitaur editor**
  - If not working unplug / plug the usb cable and reload editor

# MIDI Jitter

http://www.audiodesignguide.com/DAC_final/how.htm

https://www.ableton.com/en/manual/midi-fact-sheet/

[Midi latency analyzer](http://www.users.on.net/~mcdds001/mmmmqac/midi_jitter.html)

[how to eliminate midi jitter reddit](https://www.reddit.com/r/linuxaudio/comments/9kg418/how_to_eliminate_midi_jitter/)

https://www.thomann.de/fr/e_rm_multiclock_usb.htm : 500 balles mais apparemment top: clock sync via un signal audio. [moins cher ici](https://reverb.com/fr/item/41066860-erm-multiclock-usb)

### Midi connections comparison

- DIN 5-pin classic MIDI:
  - A latency/jitter of minimum 1ms (time to process a 3 byte midi message)
  - Jitter acceptable
- Usb:
  - More throughput
  - Usually higher jitter
- Ethernet / IP
  - better ?

**Possibilities**:

- https://www.iconnectivity.com/mioxm

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

- Driver error compensation : **0ms**

- Buffer size: **128 samples**
- Sample rate : **88200Hz**

**Minitaur**

- Midi track with **external instrument** and **Minitaur Editor(x64)**
- external instrument hardware latency : **3ms**
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



# VST2 / VST3

- vst3 détectent si du signal passent et se désactivent. 

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



# Quantization

- **Global launch quantization** (up left) == `Song.clip_trigger_quantization`. The launch clip quantization (set to **1 bar**)
- Edit->Record Quantization == `Song.midi_recording_quantization`. The automatic quantization (used for midi clips).
- We can independently quantize a clip / specific notes with the **quantize command** (`ctrl+u`)



# Presets
**Preset files**

- Fxp file : FX preset
- [Fxb file](https://www.lifewire.com/fxb-file-2621469) : FX bank
- Files are plugin specific. A bank is made of presets, save as fxp and you save the current patch, save as fxb and you save all the presets loaded in your synth as one bank (*Example : Sylenth*)

**Save / Load presets**

- ![img](https://lh5.googleusercontent.com/7LGlz_RzXxxTO3dT8G6QiIdrFH3BSIftiZCJZiT92A8bTWCdg0a6vlsuUuBatM6JtcLvdP5iM2xVt3AkNgfw9Yad2if80xk4uIk_uW3JHBvofsZhpht8c-OcTpxwwGU9YaQq_Ww-=s0) : Use live to save a [fxb file](https://www.lifewire.com/fxb-file-2621469) on your hard drive.  You can use the folder button to the left to load the preset bank.
- ![img](https://lh5.googleusercontent.com/Pm6Ls_ZbqPjPu-vXHhRHIy_jyoIv2g0JRxoBgsb-GcearzMw8cdoEkpaZXsqdSXnOex-OR1Jpbd_D8wTWP1ldNeWCOY4c6pNOQ4aMdxIXPURXE5IVhAmxLVyLdgncjJGCWCTld_c=s0)(*LFOTool example*) : use the vst plugin to save the preset file to disk



# Profiling

See https://docs.google.com/spreadsheets/d/1m4vL2dqWhx6PyerJknqP2iwtY84NHFEjbPKmC1VfdUE/edit#gid=0

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
