---
Title: "Protocol 0 technical overview"
date: 2020-12-01
draft: true
summary: "Protocol0 technical overview"
---

Context and goals on the [github readme](https://github.com/lebrunthibault/Protocol-0-Surface-Script)

Some global remote scripting tips [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing)

_This doc is here to shed some light on the script’s object model, a few techniques I’ve set up and the tools I’m using for development. It goes from global discussion on remote scripting concepts / problems to tiny details about my remote script but is not a full technical documentation. Mostly wrote this so that it’s clearer to me ^^_

NB : This script is a selected_track/clip/scene_control kindof script and so actions dispatched after moving knobs always apply to what is selected in the set.

NB : a big chunk of the automation part of the script is gonna be dropped because it is too complicated and not so useful (AutomatedTrack, AbstractAutomationTrack, AutomationAudioTrack, AutomationMidiTrack, automation curves etc ..). I’ll just keep simple methods to show / scroll clip envelope parameters like in Clyphx.

On the right is a Table of Contents listing all subjects discussed.


I’ve decided to start with an explanation of the most complex stuff of my object model : tracks. What are the different track objects, and how do I generate them at script initialization and when the lom changes.


# Object Model {#object-model}

I’ve wrapped most of the Live objects I’m using in my own classes (tracks, clip_slots, clips, devices, parameters.. ). The most complex part is the handling of tracks (not surprisingly).


## Track Classes {#track-classes}

TLDR :



* A Live.Track.Track is mapped to a SimpleTrack
* A SimpleTrack that is also a group track is mapped to an AbstractGroupTrack allowing seamless manipulation of different types of group tracks.
* All track objects inherits from AbstractTrack enforcing a common interface

Mini - Glossary :



* When I speak about Live.Track.Track I speak about the LOM object representing a track
* When I speak about SimpleTrack or AbstractGroupTrack  I’m talking about the classes I defined.
* When I speak about a group track, I just mean a group track in a set (that is foldable and has sub_tracks).


#### Contextual explanation

I’ve created the SimpleTrack class originally to make handling tracks easier than with the stock Live.Track.Track objects (because I can add my listeners, events, methods etc) and also to get a stronger typing experience. Conceptually they are simple and a one to one mapping to a track.

But what I really wanted when I started the script was to be able to manipulate group tracks as if they were a non group track (e.g. arming / soloing / recording etc …). This is because I wanted to record midi and audio in a group track at the same track, the group track being actually one instrument.

So I created the AbstractGroupTrack which is a mapping from a group track. But because all my tracks are already mapped to a SimpleTrack they are indeed mapped from a SimpleTrack. and AbstractGroupTrack.base_track is this SimpleTrack while SimpleTrack.abstract_group_track is the opposite relationship.

What is conceptual here is that I’m creating a double mapping layer (iterating twice on the track list on set startup). The first layer is just SimpleTrack creation and is straightforward.

The second layer is the AbstractGroupTrack creation and is not as straightforward. I’m effectively mapping all group tracks of the set into subclasses of AbstractGroupTrack. But I’m still keeping the SimpleTrack mapping, it is necessary for several reasons, notably that the SimpleTrack handles access to the underlying lom objects.

The only thing complicated here is that each group track is both a SimpleTrack and an AbstractGroupTrack . Both objects can access the other and that’s part of the glue between the 2 layers.

One touchy thing with this setup is for example if we have nested group tracks then we will effectively have the two layer setup with SimpleTrack group track objects having SimpleTrack sub tracks and AbstractGroupTrack having either AbstractGroupTrack or SimpleTrack sub tracks.

So it means that when accessing an AbstractGroupTrack sub tracks we have either classes (so actually : List[AbstractTrack]). But when accessing the same Live track from its SimpleTrack object the sub_tracks are : List[SimpleTrack ].

It’s a bit convoluted but for me it means AbstractTracks are the interface to the controller and what the interface sees. They handle logic but leave implementation details to the lower SimpleTracks layer. The lower layer handles all the tiny lom logic and listeners and emit their own events when necessary.

Details :



* SimpleTrack: one to one mapping with Live.Track.Track. Subclassed by
* AbstractGroupTrack (abstract) : One to one on a Live group track (SimpleTrack) and handling actions on sub_tracks. Taking into account sub_tracks can be thought of as a one to many mapping with SimpleTrack.

    Sub tracks of an AbstractGroupTrack can access their SimpleTrack group_track by self.group_track (as any grouped track) and abstract_group_track (AbstractGroupTrack) by self.abstract_group_track


    Subclassed by

    * SimpleGroupTrack : A group track with no specific behavior.
    * ExternalSynthTrack. Allows recording an external synth easily: abstraction track wrapping :
        * A midi SimpleTrack
        * An audio SimpleTrack
* AbstractTrack : top of the inheritance hierarchy for any track object (and an abstract class). This class groups all common attributes and methods that are indeed the interface of any track object. Including :
    * self.base_track is always the track itself or the group_track in the case of an AbstractGroupTrack
    * self._track is the underlying Live.Track.Track object (and == self.base_track._track)
    * self.group_track is the SimpleTrack mapping of self._track.group_track
    * self.abstract_group_track is the AbstractGroupTrack parent if it exists


## Global track objects and lists {#global-track-objects-and-lists}


### SongManager private track lists {#songmanager-private-track-lists}

Starting with a Live.Track.Track object, 2 layers of abstraction are necessary to map the Live track object to our own track object:



* _live_track_to_simple_track : maps a Live.Track.Track to a SimpleTrack object
* _simple_track_to_abstract_group_track : maps a SimpleTrack to its AbstractGroupTrack (either from the group_track or any of its sub_tracks)

With these 2 lists we can reach the right level of abstraction from e.g. Live.Song.Song.selected_track


### Track Lists in Song {#track-lists-in-song}



* song.simple_tracks : a List of SimpleTrack (that is len(song.simple_tracks) == len(tracks in a Live set except master and return tracks)
* song.abstract_tracks : the top track layer as they most specific form (that is SimpleTrack for lone tracks and AbstractGroupTracks for the group tracks). It also equals the sum of :
    * song.abstract_group_tracks
    * song.simple_tracks MINUS simple_tracks that belong to an AbstractGroupTrack

Regarding my explanation above, the first list is the lower level and the second a part (because only top tracks) the higher level of the 2 layers track mapping. Actually the controller sees both layers because some controls are specific to SimpleTrack objects.


### Track Objects in Song {#track-objects-in-song}



* song.selected_track : the selected SimpleTrack object (that is self._live_track_to_simple_track[Live.Track.Track]
* song.current_track : the most iconic property of the script. It equals : self._simple_track_to_abstract_group_track[song.selected_track] or song.selected_track. And indeed always outputs the appropriate abstraction level from the currently selected_track.

    This property allows transparent track manipulation from the controller



## Track, Clip_slot and Clip generation {#track-clip_slot-and-clip-generation}


### Maintaining state through lom changes {#maintaining-state-through-lom-changes}

The underlying lom objects do not change (even though the index in e.g. &lt;Track.Track object at 0x000000009AFAD6C8>) changes ..). Moreover the _live_ptr property on all objects will stay the same. It took me a long time to realise this simple fact god knows why.

As objects don’t change it is possible to reuse existing objects so that’s what I’m doing when I have a track change or scene change. Reusing all my tracks objects and taking care of re building my clip slots (e.g. on scene add) while reusing existing ones. Like this my state is preserved while the set is open.


### What happens on startup and after tracks or scenes change {#what-happens-on-startup-and-after-tracks-or-scenes-change}

NB: on tracks or scene change I’m reusing objects as stated above

NB: everything is done on tick 0 (synchronous, nothing is deferred)



1. All tracks are mapped to Simple Tracks.
    1. ClipSlot are generated
    2. Clips are generated
2. Instrument activation states are mapped back from the stale simple track list. Then stale tracks are disconnected.
3. Abstract group tracks are generated by looking up track names and sub_tracks disposition (ExternalSynthTrack and AutomatedTrack)
    3. AutomatedTrack.__init__ generates AutomationTracksCouple and links audio and midi dummy tracks
        1. Specific simpleTracks are generated : AutomatedAudioTrack and AutomatedMidiTrack
        2. This includes generation of ClipSlot and Clip specific subclasses
        3. “Basic” SimpleTracks are replaced in the Song and SongManager lists
    4. ExternalSynthTrack.__init__ links audio and midi tracks
4. During instantiation of Abstract group tracks, tracks are linked and generate linking for
    5. Clip Slots via ClipSlotSynchronizer
    6. Clips via ClipSynchronizer (handle by the ClipSlotSynchronizer)
5. abstract_tracks and current_track properties are computed


# Specific objects behavior {#specific-objects-behavior}


## Clip {#clip}



* on creation (by interface or API) : the Clip _configure_new method is called
    * Some properties of the clip are set (e.g. defining default clips depending on the track type)
    * For midi clips : base notes are set and the note clip view is fold to speed things up while producing (Simpler clips have a c3 note and automation clips have min middle and max notes set)


# Asynchronous tasks and scheduling {#asynchronous-tasks-and-scheduling}

**Tl;dr** : _When the code cannot be executed synchronously (some LOM changes are asynchronous, dispatching keystrokes and clicks is also asynchronous etc ..) we need to defer callbacks to be run later. There are 2 ways to handle this : either by listening on LOM properties (when possible) or by delaying callbacks using a timer._

Here are the 2 ways of scheduling asynchronous tasks in the code :



* The clean one is to listen to changes on the LOM by setting up listeners. It should be used wherever it is possible (See expanantions [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing)). Obviously this technique works only when the changes can be observed by listening to observable properties.
* The other way is to wait for a constant duration instead of having a reactive workflow. This usually happens in the following cases :
    * We cannot set up listeners on objects (some properties are not listenable) or even the changes will not be reflected in the LOM (e.g. showing a vst doesn’t trigger changes in the LOM).
    * The scheduling does not imply LOM changes (e.g. overcoming the “changes cannot be triggered by notifications”)
    * It just seems easier to define a duration in ms than to setup some complicated listener pattern

    This second way works by leveraging a timer loop given by the Live API. It seems to be the only way possible as using threading.timer does not work and is detailed in the timer scheduling following section.



## Using listeners {#using-listeners}



* Using listeners directly [in this doc](https://docs.google.com/document/d/1-r0w2E3IJiEtCIoQ9j-vnXadDUHAbiswE_HJ5iOh0Yk/edit?usp=sharing). This means attaching callbacks to listeners in some way and implies setting at least one callback variable. This method is **not** used in the script.
* Using the Sequence class (see doc in code).

**Tl;dr **: The sequence class uses both scheduling workflows (listener and timer). For the listener workflow it makes it easier to work with listeners by handling the callback registration on the listeners themselves and also makes the syntax cleaner when splitting a functionality in different asynchronous steps(reducing boilerplate code). This is possible when using the p0_subject_slot decorator instead of the subject_slot framework decorator. I like this class a lot ^^. Part of this is probably already obsolete as of Live 11 because now we might use asyncio.


### The Sequence class {#the-sequence-class}

Replacement of the _Framework Task as it does not seem to allow variable timeouts like triggers from listeners.



* A Sequence usually represents a number of statements (usually a whole method) and a SequenceStep one statement
* A Sequence step is very often a function call that could return a Sequence.
That is Sequences can be nested allowing deep asynchronous function calls.
* A Sequence should never be passed to the called code but instead the called code should return it's own sequence to be appended (and executed) to the calling one.

**Attention**: The called code is gonna be called synchronously, any data lookup (e.g. on Live API) is gonna be computed at sequence instantiation time and not at sequence runtime !

If you don't want this behavior to happen, wrap your lookup calls in a step

Ideally, an asynchronous method should wrap all it's statements in a sequence and do lookups in lambda functions

The code can declare asynchronous behavior in 2 ways:


* via wait which leverages Live 100ms tick for tasks where we have a rough idea of the delay and guess without too much hassle
* via the on_complete argument that defers the completion of the step until a condition is satisfied

This condition can be either :
* a simple callable returning a bool : in this case an exponential polling is setup with a timeout
* a CallbackDescriptor decorated function (a function decorated by _@p0_subject_slot or @has_callback_queue_) : the step executes when the function is called next be it by Live listener system or by direct call

This is the best part because it allows us to react to the execution of Live listeners or even our own listeners. Thus being a shortcut to define yet another listener on an already listened to subject.
To be clearer it is equivalent to defining a method listening on a subject (a listener) that would call back the sequence when executed.

##### Tips {#tips}

* A sequence step should always define its completion step and not expect the next step to handle any timeout or checks
* Example : A step song.create_midi_track should define its completion check to be the next call to the _added_track_listener.
* Like this any step can always be assured that it executes after the previous one has succeeded or failed (thus ending the sequence).
* After instantiating a sequence by e.g. seq = Sequence(..) you should always call seq.done() to start the sequence execution. If not the sequence is not going to be called and an exception will be thrown at the next tick.


##### Conditional execution {#conditional-execution}

Conditional execution of steps is available via do_if and do_if_not which can be any argument to Sequence.add
* The condition is executed *before* the main callable and can bypass the step depending on the result
* return_if and return_if_not are similar but will end the enclosing sequence early instead.
*  These 2 callables are going to be executed *before* the main callable which can therefore not be called
* This is rarely needed but if needed it's better to put return_if or return_if_not in an empty step (without a callable) to make things clearer


## Using timers {#using-timers}

_They are (to my knowledge) 2 ways of scheduling asynchronous tasks via timers using the Live API. Both leverage a timer that runs every n millisecond so that a task (a callable) can not be called faster than this interval_


### Via ControlSurface.schedule_message {#via-controlsurface-schedule_message}



* The tick interval is about 100ms +- 20ms (roughly)
* called via ControlSurface.schedule_message(delay_in_ticks: int, callable: callable)
* This seem to be the historical way of scheduling tasks using timers and the easiest way also as the tasks and timing management is handled by the framework


### Via Live.Base.Timer {#via-live-base-timer}



* The tick interval is much shorter (around 17ms +- 3ms on my system)
* This way the handling of the task queue needs to be done by the script (not so complicated)
* This technique is used by the push2 code and also by a famous remote script

As the 2nd method is the fastest that’s what I used for “constant time” scheduling. The numbers associated to wait named parameters always refer to this tick interval.


# Changes cannot be triggered by notification error {#changes-cannot-be-triggered-by-notification-error}

This infamous error appears when we want to apply modifications to the LOM in the same tick as we received a notification (that is a listener was triggered somewhere). Not all changes to the lom trigger this error, only certain property changes.

It is quite boring and there might be a clean solution to handling this. I didn’t find it and so there are a lot of places where I defer changes by using stuff like the @defer decorator on listeners or self.parent.defer methods. This just delays the callable execution to the next tick. It is inconvenient for 2 reasons :



* First it means wrapping assignments in syntax of the type partial(settattr, …)) which is not clear and not as well supported by pycharm as normal assignments or method calls.
* Second it is not so clear why there are all these defers because deferring can be done for other reasons as well


## Potential solution {#potential-solution}

The solution is to defer all actions done after a listener. Adding a defer in the @p0_subject_slot would be a start. I didn’t do this because I used to work with the 100 ms tick and didn’t want to slow down all the code for this trivial issue, as the deferring could potentially add up to more than one tick and noticeably slow down the interface for complex tasks. Now I’m using the faster Base.Timer tick so it might be a better choice indeed.

**Old Solution** : I used to use a decorator on properties setter that would catch this error and defer the call to the next tick. It worked perfectly but I stopped using it because I didn’t like the fact that I didn’t know if the property was changed or not. Didn’t cause any problems but I thought it could (or had) potentially introduce subtle bugs. And no one likes subtle bugs ^^

**Current Solution **:

it is not such a big issue because it doesn’t happen often and is very easy to fix.

So for now I’m just deferring stuff. Also I’m always deferring callback execution when they are attached to a listener. I’m usually setting @defer decorator on a method that would trigger this error. I prefer putting it on the topmost calling method instead of e.g. setter.


# Interface and controls {#interface-and-controls}

The interface is exposed in the components/actionGroups folder. It is targeted at my FaderFox ec4 which is composed of 16 knobs. knobs (or encoders) can send notes via press or CC via scroll.


### Classes {#classes}



* AbstractActionGroup : corresponds to a midi configuration (or group) for the 16 knobs (the ec4 has many groups). A channel is assigned to it and all knobs of the group should trigger CC/Notes on that channel
* MultiEncoder : corresponds to a knob on the EC4 and is assigned a midi identifier (for cc or Note).

As such, any controller with configurable note / cc can be used with this interface. But the controller should be configured to match the script Midi ids and channels.

The MultiEncoder class handles difference “moves” :



* presses
* long presses
* scroll
* modifiers (see below)

Any of this theses moves will trigger “actions” (that is execute a callable)


### Modifiers {#modifiers}

As my beloved EC4 has a little screen but only 16 knobs I thought of a way to optimise knobs by not only mapping one knob to a one button but by using modifiers. A button can be modified by one modifier only atm.

So a MultiEncoder belong to 1 of 2 categories :



* modifiers : we cannot attach actions to them and they just listen to presses.
* encoders : actions can be attached to any of the encoder possible “moves” or to a move with a modifier pressed (they are just like Ctrl, and multiply the number of actions that can be registered on the 16 knobs)


#### Encoder as selected object and modifier as verb {#encoder-as-selected-object-and-modifier-as-verb}

This setup is interesting because semantically I mostly think of modifiers as verbs and encoders as objects (objects always mean “selected” object of course, this is a selected_track kind of script).

Let’s just imagine modifiers being HTTP verbs and encoders being HTTP resources in a REST API :) (some encoders do not represent objects but just trigger actions though, we can think of them as RPC calls).

Here are the “object” encoders I defined:



* Track
* Track Category (the script allows us to tag tracks with a category)
* Scene
* Clip
* Song

Here are the “verb” modifiers I defined:



* Play
* Solo
* Fold
* Duplicate

Example :

The modifier Play can be applied to all of the encoders listed and will play / stop the corresponding object (and of course it applies to the selected object, e.g. the selected track).

Like this it’s clearer and easier to remember how to execute a generic action !

And the FaderFox EC4 reay shines with it’s little screen ^^


# Development {#development}


## Editor {#editor}

Pycharm of course.


#### Autocompletion {#autocompletion}

Is done by adding some folders as content roots.



* Adding decompiled version of framework or ableton v2 is really necessary as it allows pycharm to make it’s autocompletion magic
* Adding [https://github.com/cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub) as content root will allow pycharm to enable auto completion on the Live module


## Typing {#typing}

I’m using python2.7's typing system and it helps a lot. the typing module is not available in the Live10 python build so  it is necessary to install it locally and insert the site-packages folder in sys.path before anything else.


## Logging {#logging}


### Powershell formatting {#powershell-formatting}

I wrote a little powershell script that filters, colors and formats Ableton log file with only my script info (and errors). Works also with my logging level in the script. It helps a good deal.


### Data model dump {#data-model-dump}

I also have a "dump" method that dumps the most interesting part of my model data to the log file (to inspect the script state) and is mapped to one button of my controller.

-


## Testing {#testing}


### Jupyter notebooks {#jupyter-notebooks}

I wrote a dummy Live stub that allows me to load part of my code in tests and jupyter notebooks. A real Live stub could be written but I don't think it's worth a shot as it would need to be quite complex to emulate real situations. Still, jupyter is great for small python tests.


### Pytest {#pytest}

As for the jupyter notebooks It is possible to test parts of the script by using the dummy Live Stub. We can test functions and classes that don’t interact too deeply with the Live API. Limited but useful.

Wider tests can be achieved by mocking the LOM in more detail. Seems overkill as stated above.
