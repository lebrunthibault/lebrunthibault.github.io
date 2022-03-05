---
title: "Protocol0 technical overview"
description: "Protocol0 Ableton Surface Script technical overview and discussion"
keywords:
  - Ableton 
  - Ableton Remote Script
  - Ableton Control Surface Script
  - Python
---

> This is technical documentation for my [Protocol0 Ableton control surface script](https://github.com/lebrunthibault/Protocol-0-Surface-Script). Context and goals on the [GitHub readme](https://github.com/lebrunthibault/Protocol-0-Surface-Script). Some global remote scripting tips in [this google doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing)

_This doc is here to shed some light on the script’s object model, a few techniques I’ve set up and the tools I’m using for development. It goes from global discussion on remote scripting concepts / problems to tiny details about the script but is not a full technical documentation._ Please read the GitHub readme first.

<u>NB</u> : This script is a selected_track/clip/scene_control kindof script.  Actions dispatched after moving knobs always apply to what is selected in the set.

I’ve decided to start with an explanation of the most complex stuff of my object model : tracks. What are the different track objects, and how do I generate them at script initialization and when the LOM changes.

<br/>


# Object Model {#object-model}

I’ve wrapped most of the Live objects I’m using in my own classes (tracks, clip_slots, clips, devices, parameters.. ). The most complex part is the handling of tracks (not surprisingly).


## Track Classes {#track-classes}

TLDR :

* A `Live.Track.Track` is wrapped in a `SimpleTrack`
* A `SimpleTrack` that is also a group track is mapped to an `AbstractGroupTrack` allowing seamless manipulation of different type of group tracks.
* All track objects inherits from `AbstractTrack` enforcing a common interface. 
* Indeed the track layout uses the Composite design pattern

Mini Glossary :

* When I speak about `Live.Track.Track` I speak about the LOM object representing a track
* When I speak about `SimpleTrack` or `AbstractGroupTrack`  I’m talking about the classes I defined.
* When I speak about a group track, I just mean a group track in a set (that is foldable and has sub_tracks).



### Contextual Explanation

> This was tricky to setup so I went in depth with this explanation

I’ve created the `SimpleTrack` class originally to make handling tracks easier than with the stock `Live.Track.Track` objects (because I can add my listeners, events, methods etc) and also to get a stronger typing experience. Conceptually they are simple and a one to one mapping to a track. In reality I pimped them quite a bit.

But what I really wanted when I started the script was to be able to manipulate group tracks as if they were a non group track (e.g. arming / soloing / recording etc …). This is because I wanted to record midi and audio in a group track at the same time, the group track representing actually one instrument (e.g. my prophet rev2).

So I created the `AbstractGroupTrack` which is another way of representing a group track and wraps a `SimpleTrack` (because all tracks are still `SimpleTrack`s). But because all my tracks are already wrapped by a `SimpleTrack`, sub tracks of an `AbstractGroupTrack` are either `SimpleTrack` or `AbstractGroupTrack` (the Composite pattern !). and `AbstractGroupTrack.base_track` is this `SimpleTrack` while `SimpleTrack.abstract_group_track` is the opposite relationship. This base_track property somehow breaks the composite pattern so I could maybe remove it one day.

What is conceptual here is that I’m creating a double mapping layer (iterating twice on the track list on set startup). The first layer is just `SimpleTrack` creation and is straightforward.

The second layer is the `AbstractGroupTrack` creation and is not as straightforward. I’m effectively mapping all group tracks of the set into subclasses of `AbstractGroupTrack`. But I’m still keeping the `SimpleTrack` mapping, it is necessary for several reasons, notably that the `SimpleTrack` handles access to the underlying LOM objects, but also because non foldable tracks are always simply `SimpleTrack`s

The only thing complicated here is that each group track is both a `SimpleTrack` and an `AbstractGroupTrack` . Both objects can access the other and that’s part of the glue between the 2 layers.

One touchy thing with this setup is for example if we have nested group tracks then we will effectively have the two layer setup with `SimpleTrack` group track objects having `SimpleTrack` sub tracks and `AbstractGroupTrack` having either `AbstractGroupTrack` or `SimpleTrack` sub tracks.

So it means that when accessing an `AbstractGroupTrack` sub tracks we have either classes (so actually : `List[AbstractTrack]`). But when accessing the same Live track from its `SimpleTrack` wrapper object the sub_tracks are : `List[SimpleTrack]`.

It’s a bit convoluted but for me it means `AbstractTrack`s are the interface to the controller and what the interface sees. They handle logic but leave implementation details to the lower `SimpleTrack`s layer. The lower layer handles all the tiny lom logic and listeners and emit their own events when necessary.

Details :

* `SimpleTrack`: one to one mapping with `Live.Track.Track`. Subclassed by
* `AbstractGroupTrack` (abstract) : One to one on a Live group track (`SimpleTrack`) and handling actions on sub_tracks.

    Sub tracks of an `AbstractGroupTrack` can access their `SimpleTrack` group_track by `self.group_track` (as any grouped track) and abstract_group_track (`AbstractGroupTrack`) by `self.abstract_group_track`.
    Subclassed by
    
    * `SimpleGroupTrack` : A group track with no specific behavior.
    * `ExternalSynthTrack`. Allows recording an external synth easily: abstraction track wrapping :
        * A midi `SimpleMidiTrack`
        * An audio `SimpleAudioTrack`
        * An audio `SimpleAudioTailTrack` : to record clip tails
        * One or many `SimpleDummyTrack`s : because clip automation doesn't exist for group tracks. 
* `AbstractTrack `: top of the inheritance hierarchy for any track object (and an abstract class). This class groups all common attributes and methods that are indeed the interface of any track object. Including :
  
    * `self.base_track` is always the track itself or the group_track in the case of an `AbstractGroupTrack`
    * `self._track` is the underlying `Live.Track.Track` object (and == `self.base_track._track`)
    * `self.group_track` is the `SimpleTrack` mapping of `self._track.group_track`
    * `self.abstract_group_track` is the `AbstractGroupTrack` parent if it exists


## Global track objects and lists {#global-track-objects-and-lists}


### SongManager private track lists {#songmanager-private-track-lists}

Starting with a `Live.Track.Track` object, 2 layers of abstraction are necessary to map the Live track object to our own tracAbstractGroupTrackk object:

* _live_track_id_to_simple_track : maps a `Live.Track.Track` id to a `SimpleTrack` object
* The `AbstractGroupTrack` are reached through the `SimpleTrack`s

With these 2 lists we can reach the right level of abstraction from e.g. `Live.Song.Song.selected_track`


### Track Lists in Song {#track-lists-in-song}



* `song.simple_tracks` : a List of `SimpleTrack` (that is `len(song.simple_tracks) == len(tracks)` (in a Live set except master and return tracks)
* `song.abstract_tracks` : the top track layer as they most specific form (that is `SimpleTrack` for lone tracks and `AbstractGroupTrack`s for the group tracks). It also equals the sum of :
    * `song.abstract_group_tracks`
    * `song.simple_tracks` MINUS simple_tracks that belong to an `AbstractGroupTrack`

Regarding my explanation above, the first list is the lower level and the second a part (because only top tracks) the higher level of the 2 layers track mapping. Actually the controller sees both layers because some controls are specific to `SimpleTrack` objects.


### Track Objects in Song {#track-objects-in-song}



* `song.selected_track` : the selected `SimpleTrack` object
* `song.current_track` : the most iconic property of the script. It equals `song.selected_track.abstract_group_track or song.selected_track`. And indeed always outputs the appropriate abstraction level from the currently selected_track.

    This property allows transparent track manipulation from the controller



## Track, Clip_slot and Clip generation {#track-clip_slot-and-clip-generation}


### Maintaining state through LOM changes {#maintaining-state-through-lom-changes}

The underlying lom objects do not change (even though the index in e.g. `<Track.Track object at 0x000000009AFAD6C8>)` changes ..). Moreover the `_live_ptr` property on all objects will stay the same. It took me a long time to realize this simple fact god knows why.

As objects don’t change it is possible to reuse existing objects so that’s what I’m doing when I have a track change or scene change. Reusing all my tracks objects and taking care of re building my clip slots (e.g. on scene add) while reusing existing ones. Like this my state is preserved while the set is open.


# Asynchronous tasks and scheduling {#asynchronous-tasks-and-scheduling}

**Tl;dr** : _When the code cannot be executed synchronously (some LOM changes are asynchronous, dispatching keystrokes and clicks is also asynchronous etc ..) we need to defer callbacks to be run later. There are 2 ways to handle this : either by listening on LOM properties (when possible) or by delaying callbacks using a timer._

Here are the 2 ways of scheduling asynchronous tasks in the code :

* The clean one is to listen to changes on the LOM by setting up listeners. It should be used wherever it is possible (See explanations [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing)). Obviously this technique works only when the changes can be observed by listening to observable properties.
* The other way is to wait for a constant duration instead of having a reactive workflow. This usually happens in the following cases :
    * We cannot set up listeners on objects (some properties are not listenable) or even the changes will not be reflected in the LOM (e.g. showing a VST doesn’t trigger changes in the LOM).
    * The scheduling does not imply LOM changes (e.g. overcoming the *changes cannot be triggered by notifications*)
    * It just seems easier to define a duration in ms than to setup some complicated listener pattern

    This second way works by leveraging a timer loop given by the Live API. It seems to be the only way possible as using `threading.timer` does not work and is detailed in the timer scheduling following section.

## Using listeners {#using-listeners}

* Using listeners directly [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing). This means attaching callbacks to listeners in some way and implies setting at least one callback variable. This method is **not** used in the script.
* Using the Sequence class (see doc in code).

**Tl;dr **: The sequence class uses both scheduling workflows (listener and timer). For the listener workflow it makes it easier to work with listeners by handling the callback registration on the listeners themselves and also makes the syntax cleaner when splitting a functionality in different asynchronous steps(reducing boilerplate code). This is possible when using the p0_subject_slot decorator instead of the subject_slot framework decorator. I like this class a lot ^^. Part of this is probably already obsolete as of Live 11 because now we might use asyncio.


### The Sequence class {#the-sequence-class}

Replacement of the _Framework Task as it does not seem to allow variable timeouts like triggers from listeners.



* A `Sequence` usually represents a number of statements (usually a whole method) and a `SequenceStep` one statement (usually a method call)
* A `SequenceStep` is very often a function call that could return a `Sequence`.
  That is `Sequence`s can be nested allowing deep asynchronous function calls.
* A `Sequence` should never be passed to the called code but instead the called code should return it's own sequence to be appended (and executed) to the calling one.
* A `Sequence` instantiation should always finish by calling `Sequence.done()` which is an alias of `Sequence.start()`
  * Why should the sequence always be started explicitely by the inner code ? Well it's because it allows the Sequence pattern to be hidden from the calling code. A method using the Sequence pattern can be called synchronously and we are insured the Sequence will be called.
  * The exception to this rule is if you want to trigger a sequence from within a running sequence (creating a non linear / parallel execution paths). Much can be done without resorting to this somewhat obscure pattern. Notably using listeners.

**Attention**: The called code is gonna be called synchronously, any data lookup (e.g. on Live API) is gonna be computed at sequence instantiation time and not at sequence runtime.

If you don't want this behavior to happen, wrap your lookup calls in a method as a single step. But the fast way to solve this is to do lookups in lambda functions.

### Asynchronous behavior declaration 

The code can declare asynchronous behavior in 3 ways:


* via  `seq.add(wait=<ticks>)` which leverages `Live.Base.Timer` fast tick for tasks where we have a rough idea of the delay and guess without too much hassle (see [below](#using-timers-using-timers))
* via `seq.add(wait_beats=<beats)` (or `wait_bars`) that leverages the `current_song_time` Live event (see `SyncedScheduler` which notifies when beats change)
* via the `seq.add(on_complete=<listener>)` that defers the completion of the step until a listener is called.

This listener should be :

a function decorated by `@p0_subject_slot`  which returns a `CallbackDescriptor` decorated function : the step executes when the function is called next (usually by Live listener system). Just replace `@subject_slot` by `@p0_subject_slot` and the listener will integrate in the Sequence pattern.

This is the best part because it allows us to react to the execution of Live listeners or even our own listeners.
To be clearer it is equivalent to defining a method listening on a subject (that is : a listener) that would call back the sequence when executed.

NB : instead of giving a listener method to `complete_on`, we could instead pass an object and an event. But that would spread event strings and we would loose a central place to see which events are being used throughout the script. So a listener method needs to be defined for each event that we want to use in the Sequence pattern. Hence, some listeners in the code do nothing and are meant just for Sequence execution. 

##### Example usage

```python
def duplicate_track(self, index):
    # type: (Song, int) -> Sequence
    seq = Sequence()  # instantiate the Sequence class
    # add the callable to the sequence
    seq.add(partial(self._song.duplicate_track, index), complete_on=self.parent.songManager.tracks_listener)  # declare the completion step
    seq.add(wait=1)  # waits one tick (around 17ms on my system, often needed to let live process changes)
    return seq.done()  # call seq.done to trigger the sequence
```

* A sequence step should always define its completion step and not expect the next step to handle any timeout or checks. Like this any step can always be assured that it executes after the previous one has succeeded or failed (thus ending the sequence).


## Using timers {#using-timers}

_They are (to my knowledge) 2 ways of scheduling asynchronous tasks via timers using the Live API. Both leverage a timer that runs every n millisecond so that a task (a callable) can not be called faster than this interval_


### Via `ControlSurface.schedule_message` {#via-controlsurface-schedule_message}



* The tick interval is about 100ms +- 20ms (roughly)
* called via `ControlSurface.schedule_messag`e(`delay_in_ticks: int, callable: Callable`)
* This seem to be the historical way of scheduling tasks using timers and the easiest way also as the tasks and timing management is handled by the framework


### Via `Live.Base.Timer` {#via-live-base-timer}

* The tick interval is much shorter (around 17ms +- 3ms on my system)
* This way the handling of the task queue needs to be done by the script (not so complicated)
* This technique is used by the push2 code and also by a famous remote script

As the 2nd method is the fastest that’s what I used. The numbers associated to wait parameters always refer to this tick interval.


# Changes cannot be triggered by notification error {#changes-cannot-be-triggered-by-notification-error}

This infamous error appears when we want to apply modifications to the LOM in the same tick as we received a notification (that is a listener was triggered somewhere). Not all changes to the LOM trigger this error, only certain property changes.

It is quite boring and there might be a clean solution to handling this. I didn’t find it and so there are a lot of places where I defer changes by using the `self.parent.defer` methods. This just delays the callable execution to the next tick (equivalent to doing `sequence.add(wait=1)`. It is inconvenient for 2 reasons :

* First it means wrapping assignments in syntax of the type partial(`settattr`, …)) which is not clear and not as well understood by `pycharm` as normal assignments or method calls.
* Second it is not so clear why there are all these defers because deferring can be done for other reasons as well


## Potential solution {#potential-solution}

The solution is to defer all actions done after a listener. Adding a defer in the @p0_subject_slot would be a start. I didn’t do this because I used to work with the 100 ms tick and didn’t want to slow down all the code for this trivial issue, as the deferring could potentially add up to more than one tick and noticeably slow down the interface for complex tasks. Now I’m using the faster `Live.Base.Timer` tick so it might be a better choice indeed.

**Old Solution** : I used to use a decorator on properties setter that would catch this error and defer the call to the next tick. It worked perfectly but I stopped using it because I didn’t like the fact that I didn’t know if the property was changed or not. Didn’t cause any problems but I thought it could (or had) potentially introduce subtle bugs.

**Current Solution **:

it is not such a big issue because it doesn’t happen often and is very easy to fix. So for now I’m just deferring stuff. Also I’m always deferring callback execution when they are attached to a listener.


# Interface and controls {#interface-and-controls}

The interface is exposed in the `components/actionGroup`s folder. It is targeted at my FaderFox ec4 which is composed of 16 knobs. knobs (or encoders) can send notes via press or CC via scroll.


### Classes {#classes}

* `AbstractActionGroup` : corresponds to a midi configuration (or group) for the 16 knobs (the ec4 has many groups). A channel is assigned to it and all knobs of the group should trigger CC/Notes on that channel
* `MultiEncoder` : corresponds to a knob on the EC4 and is assigned a midi identifier (for cc or Note).

As such, any controller with configurable note / cc can be used with this interface. But the controller should be configured to match the script Midi ids and channels.

The `MultiEncoder` class handles difference “moves” :

* presses
* long presses
* scroll

Any of this theses moves will trigger “actions” (that is execute a callable)


# Development {#development}

> headstart for remote scripting

## Editor {#editor}

Pycharm of course.


#### Autocompletion {#autocompletion}

Is done by adding some folders as content roots.

* Adding decompiled version of framework or Ableton v2 is really necessary as it allows Pycharm to make it’s autocompletion magic
* Adding [https://github.com/cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub) as content root will allow pycharm to enable auto completion on the Live module


## Typing {#typing}

I’m using python2.7's typing system and it helps a lot. the typing module is not available in the Live10 python build so  it is necessary to install it locally and insert the site-packages folder in `sys.path` before anything else in the `__init__.py`


## Logging {#logging}


### Log formatting {#powershell-formatting}

I wrote a little PowerShell script (in my [Protocol0-backend repo](https://github.com/lebrunthibault/Protocol-0-backend) that filters, colors and formats Ableton log file with only my script info (and errors). Works also with my logging level in the script. It helps a good deal.


### Data model dump {#data-model-dump}

I also have a "dump" method that dumps the most interesting part of my model data to the log file (to inspect the script state) and is mapped to one button of my controller.


## Testing {#testing}


### Jupyter notebooks {#jupyter-notebooks}

I wrote a dummy Live stub that allows me to load the script in tests and jupyter notebooks. A real Live stub could be written but I don't think it's worth a shot as it would need to be quite complex to emulate real situations. Still, jupyter is great for small python tests.


### Pytest {#pytest}

As for the jupyter notebooks it is possible to test parts of the script by using the dummy Live Stub. I've also created a few mocks for the track class etc.. Like this we can test functions and classes that don’t interact too deeply with the Live API. Limited but useful.

Wider tests could be achieved by mocking the LOM in more detail. Seems overkill as stated above.
