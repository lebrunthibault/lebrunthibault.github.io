# Push2 Session system

### Responsibilities

- Exposing objects (track / scenes / clips) to higher layer and buttons
- Dependent layers are the bottom part of the push2 specifically the pad matrix, the scenes launcher buttons, the navigation (top) / bank (bottom) buttons + context buttons (add / new / duplicate ..)
- it exposes "session" objects as a grid (normally 8 x 8 to match the pads, but can changed)

### Initialization

- the main script uses pushbase and ableton/v2 components : SessionComponent, SessionRingComponent
- components are instantiated (indirectly) in `initialize()` and `_create_components()`

### The SessionRingComponent

> Provider for track and scenes for the session. Interesting.

- Low level session provider component using song listeners (track_list, visible_tracks, scene_list)
- Exposes low level access to :
  - `tracks_to_use`: session tracks
  - offsets (get / set) : (x / y session position against all the session clips)
  - num_tracks / num_scenes getters
  - `_update_track_list` every time something changes

### The SessionComponent

> handle buttons. Not so interesting

- Given a session ring at object creation. session ring is also listened to
- sets up all the context sensitive buttons and pads (launchers, stoppers, edit / delete .. )



# Protocol 0 Extended classes

> NB : instantiated Protocol0Push2 instead of Push2

### Push2



- `_init_session_ring` to override session ring
- matrix mode default: "session"
- code to change midi clip grid quantization

### SessionRingTrackProvider

> Handles the session box (tracks / scenes) as it appears on the screen / pads

- overridden with my implementation of `tracks_to_user()`
- connected to `SessionUpdatedEvent`

### SessionNavigationComponent

> React when navigation buttons are pressed

- Sync the selected scene in live when using push2 navigation buttons



# Push2 performance

Push2 adds 1.5 to 2s (even only the script)

`caps.TYPE_KEY: u'push2',  # this takes some time` in `__init__.py`