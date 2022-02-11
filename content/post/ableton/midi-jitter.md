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

