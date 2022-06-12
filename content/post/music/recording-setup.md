# Prophet recording setup

![image-20220211150534142](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220211150534142.png)



And [diagram here](https://app.diagrams.net/#G1O35YGEMWm0MctmqZmRg2sVx-kob9ZtqC)



# Detailed configuration:

Prophet local off : no duplication

## Midi playing and recording

- Usamo off : we don't need duplicated midi (done on arming track)
- Rev2 editor on on channel 1 : handles midi notes / cc and program change (set default)
- Rev2 editor : local on ? (if we use prophet local on)

## Audio Recording

- Usamo on : handled by the recorder
- Rev2 editor off
- Even when rev2 editor is off it's recording cc changes ! Thanks to usamo probably

## Audio playback

- Usamo off
- Rev2 editor on (or off doesn't matter)

# Another possible (simpler) solution

> Never use the prophet editor (except for the instance feature) and just use the prophet local on / or usamo for rec audio

- turn always editor off
- turn either always usamo on or only on for rec audio and if so turn prophet local on

#### But we loose program change 

- but maybe we can send program change to the usamo device instead
- problem it will pc all devices (minitaur and rev2)
- maybe it's not so important because we could store the current minitaur pc in the track data
- or maybe we use one usamo per device and send program change to the dedicated usamo (need to buy one more usamo for this)