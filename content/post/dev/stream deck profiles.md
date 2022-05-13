- See [this reddit](https://www.reddit.com/r/StreamDeckSDK/comments/ofrmgv/creating_profiles_in_streamdeck_with_sdk/)
- And [this one](https://www.reddit.com/r/StreamDeckSDK/comments/odx9od/using_sdk_to_automate_canvas_configuration/)

profiles stored in %appdata%\elgato\streamdeck\profilesV2

Should I create profile as a manifest.json in the code base and reference it ?

`$SD.api.switchToProfile($SD.uuid, $SD.deviceId, "Protocol 0")` not working

See barraider repo (in _playground)