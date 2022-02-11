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
>  With off : it's aligned with what you play (delay compensation of soundcard / driver latency and of plugin latency

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