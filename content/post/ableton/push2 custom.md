# Modified

- ableton\v2\control_surface\session_navigation_component : __on_offset_changed: updated selected scene when using navigation buttons in session mode
- push2\track_selection : SessionRingTrackProvider : 
  - replaced track_to_use by scene_tracks
  - added _on_selected_scene_changed listener. So that the track list is updated on scene change (we keep only scene tracks)
- push2\push2 : Push2.initialize : dispatched Push2InitializedEvent so that protocol0 connects to it
- ableton\v2\control_surface\components\session_ring : SessionRingComponent : replaced tracks_to_use by scene_tracks (to have the session pad following the scene tracks)