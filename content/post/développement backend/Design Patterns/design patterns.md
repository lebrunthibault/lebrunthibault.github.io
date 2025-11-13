---
prod: true
draft: false
title: "Design Patterns Portfolio"
description: "Notes bout design patterns"
keywords:
  - Software development
  - Backend development
  - Design patterns
date: "2022-01-01"
---

# Design patterns currently used in projects I've worked on



### [Factory Method](https://refactoring.guru/design-patterns/factory-method)

- Used in Protocol0 backend to generate notification / prompt / select windows

### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

- Used textbook in Protocol0 to generate a track recorder
- The abstract factory generates for a track and record type :
  - A track recorder
  - A scene index for the recording
  - A bar length for the recording

### [Singleton](https://refactoring.guru/design-patterns/singleton)

- Used in basile ats client generation tests
- The test ats client returned is always the same to be able to push fake http responses into the tests (pattern not used anymore)

### [Facade](https://refactoring.guru/design-patterns/facade)

- Used in protocol0 SongFacade to expose readonly access to song objects
- Also in Scheduler to expose simplified facade to scheduling methods from 2 scheduler classes

### [Composite](https://refactoring.guru/design-patterns/composite)

- Used to abstract composite tracks in protocol0 e.g. in arming tracks or soloing them.
- Implemented using classical inheritance with AbstractTrack
- Leaves are SimpleTracks, containers are AbstractGroupTracks
- We could remove the AbstractTrack.base_track as it breaks the encapsulation principle.

### [Decorator](https://refactoring.guru/design-patterns/decorator)

> Used in its simple form but could be improved to implements the real pattern semantics.

- Used in protocol0, to augment behavior of notification classes.
- Used somewhat in basile to catch exceptions. Respects the pattern semantics but replaces the interface step by just using callables.
- Could improve the generation of missing ATS responses in basile. The ATSServiceFactory could return a ATSServiceResponseGeneratorDecorator implementing the interface without handling these kind of cases explicitly.
- Could also work for the ErrorHandlerService instead of catching the exceptions in the client code.
- Could also be used for offer synchronization by applying decorators at service instantiation time for company custom code instead of using inheritance. Might be overkill though.  

### [Template method](https://refactoring.guru/design-patterns/template-method)

- Used in basile ats synchonize offers
- Used in protocol0 recording system ()

### [Observer](https://refactoring.guru/design-patterns/observer)

- Used in protocol0 system notification system
- The inner notification window notifies values when buttons are clicked
- A decorator applied at instantiation (in the notification factory) observes the inner window and sends values to the script over midi.

### [Pub / sub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

> in a simple, synchronous way

- Used in Basile status synchronization
- The status code emits events on a event bus
- The event bus dispatches to observers subscribed to specific events

# Design patterns partially used

### [Builder](https://refactoring.guru/design-patterns/builder)

- Used in basile admin crud. ressemble because we don't use a bloated constructor.
- Not using a specific builder class but by passing directly an instantiated object
- Could be improved by creating an AdminCrudConfigBuilderInterface subclassed by AdminCrudConfigBuilder and AdminFormConfigBuilder. Not really the builder pattern because we would pass a specific builder class and not interface but close.

### [Prototype](https://refactoring.guru/design-patterns/prototype)

- Used in basile to clone newsletters
- Not respecting the prototype pattern semantics but using __clone magic method

### [State](https://refactoring.guru/design-patterns/state)

- Used in Protocol0 Sequence code
- A Sequence can be in different states (unstarted, started, paused, cancelled, errored)
- Transitions are defined accordingly
- Implemented using the transitions package
- NB : states are not defined in specific classes which doesn't respect the pattern

# Design patterns that could improve existing projects

### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

- In basile ATSServiceFactory
- Instead of using a single class per ATS we could instead create one feature class per abstract ATS feature
- The current ats class could be replaced by a factory returning a feature class instance respecting the single responsibility principle.
- That would be beneficial for the status synchronization as we could have a single synchronizeStatusesInteface (with method synchronizeStatuses) instead of using a match in ATSSynchronizeStatusesService.
- Downside : would need a lot more classes and would complicate the subclassing of the ats code by a specific company's ats implementations.

### [Command](https://refactoring.guru/design-patterns/command)

- Replace the encoder action code with commands
- create a command class per feature
- logging by command (using command class name)
- add an undo button doing multiple undo.
- undo can be used for undoing recordings as well
- define macro commands using commands arm track, show plugins .. 

In basile

- NB : in basile we use messages as commands but it’s message handlers that connect to a specific receiver and not client code
- We could use commands to wire up some frontend and backoffice features but how do we serialize the command in the front ? 



### [Adapter](https://refactoring.guru/design-patterns/adapter)

- Maybe on ATS system to abstract the different protocols used (if one day we use more that are not rest ..?) 
- For ATS V1



