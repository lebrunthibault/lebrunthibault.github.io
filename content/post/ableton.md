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
- Sample rate : **44100Hz**

**Minitaur**

- Midi track with **external instrument** and **Minitaur Editor(x64)**
- external instrument hardware latency : **1.4ms**
- Audio track taking audio from midi track **pre fx**

**Prophet**

- Midi track with **external audio effect**
- external instrument hardware latency : **3.20ms**
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

- [Roland UM-One MkII](https://www.thomann.de/fr/roland_um_one_mkii.htm) : cable usb to 2 * midi : peut permetttre de réduire le jitter de l'ordi au synth par rapport a un cable usb normal
- Use a high end audio soundcard using pll (focusrite [jetpll](https://pro.focusrite.com/what-is-jetpll))



 # Recording CC automation with Rev2 editor

### Problems

- The automation isn't always recorded when the editor is toggled off
- But when the editor is toggled on we (probably) have midi feedback and notes off messages just after note on (very short notes)

### Solutions considered:

- Toggling on / off the editor to "force" it to react to parameters change and react to automation (current solution)
- Find a way to work with the editor turned on : **didn't work (at all)**
- Record nrpn or cc automation in live directly by playing with midi ports

### The midi port solution

> The idea is to record cc automation without using the editor. There is two main problems with this approchach :
>
> - It's going to be hard to have more than 8 parameters
> - The setup with midi ports doesn't work with the rev2 editor

- Setup two loop back ports : REV2_EDITOR and REV2_ABLETON that both wraps the rev2 ports
- Possibly translate nrpn to cc on the REV2_ABLETON input port and then record it by e.g. grouping the editor and using macro controls.
- Or Use the NRPN gen 2 max device to work directly with nrpn (limited to 8 parameters)

Unfortunately the rev2 editor works well with the loop back input port **but not with the loopback output port**.

It could be that it sends binary data to the synth that does not work with the loop back port ..

### Current solution : the toggling of the editor

It works partially well, but sometimes the encoder move is not caught (at all) by the editor.

Still after toggling it manually it's gonna work well. **Should we increase the delay of the toggling ?**

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



# Speed up sets load time



See https://docs.google.com/spreadsheets/d/1m4vL2dqWhx6PyerJknqP2iwtY84NHFEjbPKmC1VfdUE/edit#gid=0

### Push2

​	Push2 adds 1.5 to 2s (even only the script)

​	`caps.TYPE_KEY: u'push2',  # this takes some time` in `__init__.py`

# Midi ports

See https://help.ableton.com/hc/fr-fr/articles/209774205-Les-ports-MIDI-de-Live-comment-%C3%A7a-marche

- Track : Note on, Note off, CC, program change
- Sync : clock info
- Remote : Assignation midi (input) and assigned midi parameters change



# Usamo

debug steps :

- Open focusrite control !
- Power down & up soundcard
- Launch empty set with usamo testing

# The ideal audio setup

https://gearspace.com/board/music-computers/991372-what-audio-interface-synths-not-mics.html

Utiliser des boites de direct ? http://chambinator.free.fr/english/diboxus.htm

e.g : https://www.thomann.de/fr/radial_engineering_jdi.htm

maybe not : https://forum.vintagesynth.com/viewtopic.php?t=34109#:~:text=Since%20synths%20are%20almost%20always,can%20great%20results%20without%20one.&text=There%20is%20no%20reason%20to,a%20line%20level%20synth%20output.

Motu interface with midi timestamps ? https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/1112683-do-usb-midi-interfaces-send-midi-faster-than-midi-spec-3.html


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



# Electrical buzz

### Plug (us)

- Hot hole (right) : black, goes to circuit breaker
- Neutral hole (left) : white, goes to circuit breaker **neutral bar**
- Ground hole (down): goes to circuit breaker **ground bar** then **neutral bar**  

### How to remove ground loop issues

See https://www.youtube.com/watch?v=DSxvNtW5n6c

Using https://www.thomann.de/fr/radial_engineering_pro_d2.htm : interrupteur de masse + signal stereo asym vers sym (jack ts vers xlr). **passif**

Remove ground on audio cables to the speakers with : https://www.sescom.com/products/view/product/productslug/il-19-pro-audio-hum-eliminator-inline-with-isolation. xlr to xlr. **passif**

Remove ground on usb cables  ! https://www.amazon.fr/iDefender-Type-A-%C3%A0/dp/B0849J33T9?th=1. **actif** avec alim **sans** ground



# Gear

[Presonus FaderPort 8](https://www.youtube.com/watch?v=0Ej6Tn0wF-4) : motorized faders, lcd screen per fader, 500 euros

[Panorama P1 Nektar](https://www.youtube.com/watch?v=awgTN91bRsM) ? 
