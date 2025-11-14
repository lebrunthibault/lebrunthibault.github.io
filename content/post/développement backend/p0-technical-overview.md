---
prod: true
title: " Protocol0 technical overview"
description: "Protocol0 Ableton Surface Script technical overview and discussion"
keywords:
  - Electronic music
  - Ableton 
  - Python
  - REST API
  - Open API
date: "2022-01-01"
---

> This is technical documentation for my [Protocol0 Ableton control surface script](https://github.com/lebrunthibault/Protocol-0-Surface-Script). Context and goals on the [GitHub readme](https://github.com/lebrunthibault/Protocol-0-Surface-Script).

This doc is here to shed some light on the script’s object model, 
a few techniques I’ve set up, and the tools I’m using for development. 
It goes from global discussion on remote scripting concepts / problems 
to tiny details about the script but is not a full technical documentation.
Please read the GitHub readme first.

<u>NB</u> : This script is a selected_track/clip/scene control kind of script.
Actions dispatched after moving knobs usually apply to what is selected in the set.

One of the first things I've done in this script it create my own object model
so as to be really confortable. Even though most remote scripts probably use stock Live track objects
I’ve decided to start with an explanation of the most complex stuff of my object model : tracks. 
What are the different track objects, and how do I generate them at script initialization and when the LOM changes.
If this doesn't interest you please feel free to skip.


# Object Model {#object-model}

I’ve wrapped most of the Live objects. This allows me to do complex stuff, and it makes typing stronger.
I’m using instead my own classes (tracks, clip_slots, clips, devices, parameters.. ).
The most complex part is the handling of tracks (not surprisingly).


## Track Classes {#track-classes}

TLDR :

* A `Live.Track.Track` is wrapped in a `SimpleTrack`
* A `SimpleTrack` that is also a group track is mapped to an `AbstractGroupTrack` allowing seamless manipulation of different type of group tracks.
* All track objects inherits from `AbstractTrack` enforcing a common interface. 
* Indeed, the track layout uses the **Composite design pattern**

Mini Glossary :

* When I speak about `Live.Track.Track` I speak about the LOM object representing a track
* When I speak about `SimpleTrack` or `AbstractGroupTrack`  I’m talking about the classes I defined.
* When I speak about a group track, I just mean a group track in a set (that is foldable and has sub tracks).


### Contextual Explanation

> This was tricky to set up, so I went in depth with this explanation

I’ve created the `SimpleTrack` class originally to make handling tracks easier than with the stock `Live.Track.Track` objects
(because I can add my listeners, events, methods etc) 
and also to get a stronger typing experience. 
Conceptually they are simple and a one to one mapping to a track. 
In reality, I pimped them quite a bit.

What I really wanted when I started the script was to be able to manipulate group tracks 
as if they were a non group track (e.g. arming / soloing / recording etc …).
This is because I wanted to record midi and audio in a group track at the same time,
the group track representing actually one instrument (e.g. my prophet rev2).

So I created the `AbstractGroupTrack` which is another way of representing a group track 
and wraps a `SimpleTrack` (because all tracks are still `SimpleTrack`s).
But because all my tracks are already wrapped by a `SimpleTrack`, 
sub tracks of an `AbstractGroupTrack` are either `SimpleTrack` or `AbstractGroupTrack`
(the Composite pattern !). 
And `AbstractGroupTrack.base_track` is this `SimpleTrack` while 
`SimpleTrack.abstract_group_track` is the opposite relationship. 
This base_track property somehow breaks the composite pattern, so I could maybe remove it one day.

What is conceptual here is that I’m creating a double mapping layer 
(iterating twice on the track list on set startup). 
The first layer is just `SimpleTrack` creation and is straightforward.

The second layer is the `AbstractGroupTrack` creation and is not as straightforward.
I’m effectively mapping all group tracks of the set into subclasses of `AbstractGroupTrack`.
But I’m still keeping the `SimpleTrack` mapping, 
it is necessary for several reasons, notably because the `SimpleTrack` handles access to the underlying LOM objects,
but also because non-foldable tracks are always simply `SimpleTrack`s

The only thing complicated here is that each group track is both a `SimpleTrack` and an `AbstractGroupTrack`.
Both objects can access the other and that’s part of the glue between the 2 layers.

One touchy thing with this setup is for example if we have nested group tracks then we will effectively have
the two layer setup with `SimpleTrack` group track objects having `SimpleTrack` sub tracks and
`AbstractGroupTrack` having either `AbstractGroupTrack` or `SimpleTrack` sub tracks.

So it means that when accessing an `AbstractGroupTrack` sub tracks we have either classes
(so actually : `List[AbstractTrack]`).
But when accessing the same Live track from its `SimpleTrack` wrapped object (when we do `track.base_track`) 
its own sub tracks are : `List[SimpleTrack]`. I'm always accessing sub tracks with the former technique.

It’s a bit convoluted but for me, it means `AbstractTrack`s are the interface to the controller and 
what the interface sees.
They handle logic but leave implementation details to the lower `SimpleTrack`s layer.
The lower layer handles all the tiny lom logic and listeners and emit their own events when necessary.

Details :

* `SimpleTrack`: one to one mapping with `Live.Track.Track`. Composes the sub tracks of
* `AbstractGroupTrack` (abstract) : One to one on a Live group track (mapped to a `SimpleTrack` ofc) 
  and managing its own sub_tracks.

    Sub tracks of an `AbstractGroupTrack` can access their `SimpleTrack` group_track by `self.group_track` (as any grouped track) and abstract_group_track (`AbstractGroupTrack`) by `self.abstract_group_track`.
    Subclassed by
  
    * `SimpleGroupTrack` : A group track with no specific behavior.
    * `ExternalSynthTrack`. Allows recording an external synth easily: abstraction track wrapping :
        * A midi `SimpleMidiTrack`
        * An audio `SimpleAudioTrack`
        * An audio `SimpleAudioTailTrack` : to record clip tails
        * One or many `SimpleDummyTrack`s : because clip automation doesn't exist for group tracks. 
* `AbstractTrack `: top of the inheritance hierarchy for any track object (and an abstract class).
  This class groups all common attributes and methods that are indeed the interface of any track object. Including :
  
    * `self.base_track` is always the `SimpleTrack` itself, or the group_track in the case of an `AbstractGroupTrack`
    * `self._track` is the underlying `Live.Track.Track` object (and == `self.base_track._track`)
    * `self.group_track` is the `SimpleTrack` mapping of `self._track.group_track`
    * `self.abstract_group_track` is the `AbstractGroupTrack` parent if it exists


## Global track objects and lists {#global-track-objects-and-lists}


### TrackService private track list {#trackservice-private-track-list}

Starting with a `Live.Track.Track` object, 2 layers of abstraction are necessary to map the Live track object
to our own tracAbstractGroupTrack object:

* _live_track_id_to_simple_track : maps a `Live.Track.Track` id to a `SimpleTrack` object
* The `AbstractGroupTrack` are reached through the `SimpleTrack.abstract_group_track`s

With this single list we can reach the right level of abstraction from e.g. `Live.Song.Song.selected_track`


### Track Lists in SongFacade {#track-lists-in-songfacade}

* `SongFacade.simple_tracks()` : a List of `SimpleTrack` (that is `len(song.simple_tracks) == len(tracks)` (in a Live set except master and return tracks)
* `SongFacade.abstract_tracks()` : the top track layer as they most specific form (that is `SimpleTrack` for lone tracks 
  and `AbstractGroupTrack`s for the group tracks).

Regarding my explanation above, the first list is the lower level, 
and the second a part (because only top tracks) of the higher track mapping layer.


### Track Objects in SongFacade {#track-objects-in-songfacade}

* `SongFacade.selected_track()` : the selected `SimpleTrack` object
* `SongFacade.current_track()` : the most iconic getter of the script. 
  It equals `SongFacade.selected_track().abstract_group_track or SongFacade.selected_track()`.
  And indeed always outputs the appropriate abstraction level from the currently selected_track.
  This property allows transparent track manipulation from the controller



## Track, Clip_slot and Clip generation {#track-clip_slot-and-clip-generation}

### Maintaining state through LOM changes {#maintaining-state-through-lom-changes}

The underlying lom objects do not change (even though the index in e.g. `<Track.Track object at 0x000000009AFAD6C8>)` changes ..).
Moreover, the `_live_ptr` property on all objects will stay the same.

As objects don’t change it is possible to reuse existing objects so that’s what I’m doing
when I have a track change or scene change.
Reusing all my tracks objects and taking care of rebuilding my clip slots (e.g. on scene add)
while reusing existing ones. Like this my state is preserved while the set is open.


# Asynchronous tasks and scheduling {#asynchronous-tasks-and-scheduling}

When the code cannot be executed synchronously 
(some LOM changes are asynchronous, dispatching keystrokes and clicks is also asynchronous etc ..)
we need to defer methods to be run later.
There are 2 ways to handle this : either by listening on LOM properties (if possible, preferred way) or by
delaying callbacks using a (static) timer.

Here are the 2 ways of scheduling asynchronous tasks in the code :

* The clean one is to listen to changes on the LOM by setting up listeners.
  * It should be used wherever it is possible (See explanations [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing)). Obviously this technique works only when the changes can be observed by listening to observable properties.
* The other way is to wait for a constant duration instead of having a reactive workflow.
  This usually happens in the following cases :
    * We cannot set up listeners on objects (some properties are not listenable)
    * Maybe the change will not be reflected in the LOM (e.g. showing a VST doesn't trigger a LOM event).
    * It just seems easier to define a duration in ms than to set up some complicated listener pattern
  

This second way works by leveraging a timer loop given by the Live API.
It seems to be the only way possible as using `threading.timer` does not work and is detailed in the 
timer scheduling following section.

## Events

Using events is mandatory for any asynchronous stuff and usually useful for sync stuff as well. I'm using them quite often.

 I'm using them in two ways :

- Low level LOM events are handled via the Live event system :
  - Use them by subclassing `SlotManager`and using the `subject_slot` decorator
  - This approach is here as the low level event interface to the LOM and it works perfectly
  - But Live events have several issues
    - They are more notifications than events, there is no payload
    - They use monkey patching which is dirty and cannot be checked by mypy
    - The code seems very complicated for what it does
    - As a consequence its not so easy to integrate into it. Thats why I've dropped a past integration and now use my own event system.
- High level Domain events are handled by myself
  - I've setup a simple event bus
  - Every time I feel the need to decouple stuff or emit events I create a simple object event and dispatch it
  - Any component can listen to any event and optionally check its payload (it's global state really but fine for this not so big codebase).
  - These events are integrated to the Sequence pattern (see below) allowing simple composition of events and actions
  - I really like events more and more and I've used them quite a lot to decouple objects together, in a way not so far from js frameworks like vue.
- NB : For closer scope low level events I'm also using the Observer pattern. 

## The Sequence class {#the-sequence-class}

> This is my solution for doing asynchronous stuff in Live.
> 
> It exploits the Live listener system, the Live Timer as well as my own events
> 
> Everything is wrapped in a simple class that will execute all the code it is given timely
> by reacting to different events.
> 
> It ressembles the _Framework Task class, but I've added some more features on it. 
> It also ressembles a poor implementation of asyncio.
> 
> It works well, but the `Sequence.add` only accepts functions, so it means using a lot of partial and lambda 

* A `Sequence` usually represents a number of statements (usually a whole method) and a `SequenceStep` one statement (usually a method call)
* A `SequenceStep` is often a method call that returns a `Sequence`.
  That is `Sequence`s can be nested allowing deep asynchronous method calls.
* A `Sequence` should never be passed to the called code 
  but instead the called code should return its own sequence to be appended (and executed) to the calling one (see the code)
* A `Sequence` instantiation should always finish by calling `Sequence.done()` which starts the sequence.
  * Why should the sequence always be started explicitly by the inner code ? 
    Well it's because it allows the Sequence pattern to be hidden from the calling code. A method using the Sequence pattern can be called synchronously, and we are insured the Sequence will be called.

**Attention**: The called code is going to be called synchronously, any data lookup (e.g. on Live API)
is going to be computed at sequence instantiation time and not at sequence runtime.

If you don't want this behavior to happen, wrap your lookup calls in a method as a single step.
But the fast way to solve this is to do lookups in lambda functions.

### Asynchronous behavior declaration 

The code can declare asynchronous behavior in different ways:


* via  `seq.wait(<ticks>)` which leverages `Live.Base.Timer` tick
  for tasks where we have a rough idea of the delay we want (see [below](#using-timers-using-timers))
* via `seq.wait_beats(<beats)` (or `wait_bars`) that leverages the `current_song_time` Live event (see `BeatScheduler`)
* via the `seq.wait_for_event(<event>)` that will continue sequence execution when one of my own events is fired




#### Example usage

```python
class TrackCrudComponent(object):
    def duplicate_track(self, index):
        # type: (int) -> Sequence
        seq = Sequence()
        self._duplicate_track(index)
        seq.wait_for_event(TracksMappedEvent)
        return seq.done()
```

* A sequence step should always wait for its completion 
  and not expect the next step to handle any timeout or checks. 
  Like this any step can always be assured that it executes after the previous one has succeeded


## Using timers {#using-timers}

They are (to my knowledge) 2 ways of scheduling asynchronous tasks via timers using the Live API.
Both leverage a timer that runs every n millisecond so that a task (a callable) can not be called faster
than this interval


### Via `ControlSurface.schedule_message` {#via-controlsurface-schedule_message}

* The tick interval is about 100ms +- 20ms (roughly)
* called via `ControlSurface.schedule_message(delay_in_ticks: int, callable: Callable)`
* This seems to be the historical way of scheduling tasks using timers 
  and the easiest way also as the tasks and timing management is handled by the framework
* I'm not using it, it's too slow


### Via `Live.Base.Timer` {#via-live-base-timer}

* The tick interval is much shorter (around 17ms +- 3ms on my machine)
* This way the handling of the task queue needs to be done by the script (not so complicated)
* This technique is used by the push2 code and also by clyphx

As the 2nd method is the fastest that’s what I used.
The numbers associated to wait parameters always refer to this tick interval.




## Changes cannot be triggered by notification error {#changes-cannot-be-triggered-by-notification-error}

This infamous error appears when we want to apply modifications to the LOM in the same tick
we received a notification (that is a listener was triggered somewhere).
Not all changes to the LOM trigger this error, only certain property changes.

It is quite boring and there might be a clean solution to handling this.
I didn't find it and so there are a lot of places where I defer changes by using `Scheduler.defer` or `Sequence.defer` or `@defer`.
This just delays the callable execution to the next tick. It is inconvenient for 2 reasons :

* It makes the following method code asynchronous, and we need to transform it using lambda and partial
* Second it is not so clear why there are all these defer because deferring can be done for other reasons as well

There are other ways to handle this
(like defer everything done after a listener is called, or decorate methods raising this error).
None of them is ideal, and I stuck with my current approach.

# Interface and controls {#interface-and-controls}

The interface is exposed in the `application/controlSurface` folder.
It is targeted at my FaderFox ec4 which is composed of 16 knobs.
Knobs (or encoders) can send notes via press or CC via scroll.


### Classes {#classes}

* extending `ActionGroupMixin` : corresponds to a midi configuration (or group) for the 16 knobs (the ec4 has many groups).
  A channel is assigned to it and all knobs of the group should trigger CC/Notes on that channel
* `MultiEncoder` : corresponds to a knob on the EC4 and is assigned a midi identifier (for cc or Note).

As such, any controller with configurable note / cc can be used with this interface.
But the controller should be configured to match the script Midi values and channels (or modify the script instead)

The `MultiEncoder` class handles different “moves” :

* presses
* long presses
* scroll

Any of these moves will trigger “actions” (that is : execute a callable)


# Development {#development}

> headstart for remote scripting

## Documentation
Here is all the doc I have found and used for building the script (plus a lot of articles and googling about python ofc)
- The [max for live documentation](https://docs.cycling74.com/max5/refpages/m4l-ref/m4l_live_object_model.html):
  It doesn't show the full Live API but it has a nice diagram and is quite readable
- The [Structure void documentation](https://structure-void.com/PythonLiveAPI_documentation/):
  It's simply a dump of the Live API. Not so readable but thorough
- The [Structure void remote scripts decompiled](https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts)
  That's what you need to have on your computer to understand the _Framework and ableton/v2 code
  
  NB : you can also simply decompile your remote scripts folder yourself.
- The [Clyphx Pro user manual](https://isotonikstudios.com/wp-content/uploads/ClyphX-Pro-User-Manual-5.pdf)
  That is interesting if you've decompiled the Clyphx source code. I've learnt a lot of things on remote scripting by checking out the code.

## Editor {#editor}

Pycharm of course.


#### Autocompletion {#autocompletion}

Is done by adding some folders as content roots.

* Adding decompiled version of framework or Ableton v2 is really necessary as it allows Pycharm
  to make its autocompletion magic
* Adding [https://github.com/cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub) 
  as content root will allow pycharm to enable auto-completion on the Live module


## Typing {#typing}

I’m using python2.7's typing module, and it helps a lot.
the typing module is not available in the Live10 python build,
so it is necessary to install it locally and insert the site-packages folder in `sys.path` 
before anything else in the top `__init__.py`


## Logging {#logging}

### Log formatting {#powershell-formatting}

I wrote a little python script (in my [Protocol0-backend repo](https://github.com/lebrunthibault/Protocol-0-backend))
that filters, colors and formats Ableton log file with only my script info (and errors).
It helps a good deal.

### Data model dump {#data-model-dump}

I also have a `LogService` that can dump the most interesting part of my model data to the log file 
(to inspect the script state) and is mapped to one button of my controller.


## Testing {#testing}

I wrote a dummy Live stub that allows me to execute tests (pytest) and jupyter notebooks.
It's not at all thorough, but it allows me to completely load the script and even play with track objects.

### Jupyter notebooks {#jupyter-notebooks}

I sometimes test script features using jupyter. It's great for anything I don't really need Live for.

### Pytest unit tests {#pytest}

As for the jupyter notebooks it is possible to test parts of the script by using the dummy Live Stub.
Like this we can test functions and classes that don’t interact too deeply with the Live API. 
I can also test stuff not related to the Live API like the Sequence code.
Limited but useful.

### Integration tests

I have an empty method in my `ActionGroupTest` that I use for testing features against Ableton.
