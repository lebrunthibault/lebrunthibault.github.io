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

- Use live to save a [fxb file](https://www.lifewire.com/fxb-file-2621469) on your hard drive.  You can use the folder button to the left to load the preset bank.
- use the vst plugin to save the preset file to disk

# Midi ports

See https://help.ableton.com/hc/fr-fr/articles/209774205-Les-ports-MIDI-de-Live-comment-%C3%A7a-marche

- Track : Note on, Note off, CC, program change
- Sync : clock info
- Remote : Assignation midi (input) and assigned midi parameters change

# VST2 / VST3

- vst3 détectent si du signal passent et se désactivent. 

# Recording CC automation with Rev2 editor

## Problems

- The automation isn't always recorded when the editor is toggled off
- But when the editor is toggled on we have double midi output to the rev2 (very short notes due to note off messages)
  - Midi output from the vst (with jitter)
  - And from the usamo (sample accurate)

## Solutions considered:

### Current solution : editor off / on / off

- Work with editor turned off
- Briefly toggle if on to catch cc / nrpn messages for automation

### Kind of ok working solution : editor off when recording, and on when recording audio !

- This will work but we cannot record parameter change on the first recording.

### Not working solution : work with editor on

- This solution never worked
- because we cannot filter out the jittery midi output from the editor, we get duplicate (unsynchronized) midi

### Work with editor off and redirect CC / NRPN back in love

> The idea is to record cc automation without using the editor. There is two main problems with this approach :
>
> - It's going to be hard to have more than 8 parameters
> - **The setup with midi ports doesn't work with the rev2 editor**

- Setup two loop back ports : REV2_EDITOR and REV2_ABLETON that both wraps the rev2 ports
- Possibly translate nrpn to cc on the REV2_ABLETON input port and then record it by e.g. grouping the editor and using macro controls.
- Or Use the NRPN gen 2 max device to work directly with nrpn (limited to 8 parameters)

Unfortunately the rev2 editor works well with the loop back input port **but not with the loopback output port**.

It could be that it sends binary data to the synth that does not work with the loop back port .



