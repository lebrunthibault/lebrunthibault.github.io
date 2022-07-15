# Clean sidechain compression

> See [this video](https://www.youtube.com/watch?v=Gc4pehOp-Y4)

## With compressor

> Good for dynamic source, simpler to setup

- sidechain input pre-fx
- Ratio infinite
- attack the lowest possible without artefacts
- detection mode: peak (especially for drums)

## With LFOTool

> Good for source with fixed velocity

- Do not send directly midi to the lfo tool 
  - create a midi track with an external instrument to have **latency compensation** and copy paste midi notes
  - one midi track and one lfo tool per sidechain source
- Or .. use an instrument rack ?
- LFOTool midi config: note retrigger in **env** mode
- handle clipping on attack : use **smooth** param but sometimes it's good to add punch. don't stop it until the end because then it would not play in ENV mode
- Make it less aggressive by using the **split** button (down right).

# [Have a great kick](https://www.youtube.com/watch?v=0ZOx2o_2Zfw)

