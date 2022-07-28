# Minitaur editor disconnected

- only minitaur out / track is necessary
- **simply reload the minitaur editor**
- If not working unplug / plug the usb cable and reload editor

# Minitaur no sound

- change preset


# [Usamo](https://www.expert-sleepers.co.uk/usamo.html) setup not working

> See the [recording setup diagram](https://app.diagrams.net/#G1O35YGEMWm0MctmqZmRg2sVx-kob9ZtqC)

### Launch the test mode using focusrite midi (in any set)

if there is no Midi recevied

- Check the headphones 2 out is full volume on the soundcard

if there is garbage midi received

- Open focusrite control
- Power down & up soundcard

NB : the midi thru is normally never in cause, no need to check the cables



# Audio export not offline

- at least one external instrument is enabled

# Prophet white noise

> There is electrical interference between some components

- Check if volume is boosted in the device chain
- Power cycle sound card
- Reboot pc



# Ctrl-C Ctrl-V / Ctrl-D bug

> not copying clips on expected scene

- Clear - restore the in between scene. It should work



# Latency is not zero when recording

- test usamo
- launch test usamo command
- re boot computer
- play with sample rate (?)



# Prophet noise floor a bit high & recording interferences

- Current solution : using hum destroyer + sym cables to input 5/6
- Tests asym / sym vs with box or not

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220616225521942.png?token=AEHIPTOAKXQZFSCZIQZ53CLCVO2RQ" alt="image-20220616225521942" style="zoom:50%;" />

- [How to record synths with no background noise reddit](https://www.reddit.com/r/synthesizers/comments/93pat4/how_to_record_synths_with_no_background_noise/): end of story : **gain staging** (but it cannot be done on scarlett back inputs imo)
- Le volume du prophet doit toujours etre au max



# Clips are duplicated on the wrong scene

- See https://trello.com/c/kMrRJEBn/646-try-to-reproduce-ctrl-c-ctrl-v-not-copying-clips-on-right-scene
- remove some tracks and ctrl-z
- or reload set

# Ableton freezes and cannot be killed

- restart the computer

# Vsts disabled

- [Vst rescan button + Alt](https://forum.ableton.com/viewtopic.php?t=171579)
