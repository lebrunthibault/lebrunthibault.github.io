---
title: "Design Patterns"
description: "Notes bout design patterns"
keywords:
  - Software development
  - Backend development
  - Design patterns
---

# Design patterns currently used in projects

### [Abstract Factory Method](https://refactoring.guru/design-patterns/factory-method)

- Used in Protocol0 backend to generate notification / prompt windows

### [Singleton](https://refactoring.guru/design-patterns/singleton)

- Used in basile ats client generation tests
- The test ats client returned is always the same to be able to push fake http responses into the tests (pattern not used anymore)

### [Composite](https://refactoring.guru/design-patterns/composite)

- Used to abstract composite tracks in protocol0 e.g. in arming tracks or soloing them.
- Implemented using classical inheritance with AbstractTrack
- Leaves are SimpleTracks, containers are AbstractGroupTracks
- We could remove the AbstractTrack.base_track as it breaks the encapsulation principle.

### [Decorator](https://refactoring.guru/design-patterns/decorator)

> Used in its simple form but could be improved to implements the real pattern semantics.

- Used in protocol0, to augment behavior of notification classes.
- Used somewhat in basile to catch exceptions. Respects the pattern semantics but replaces the interface step by just using callables.
- Could improve the generation of missing ATS responses in basile. The ATSServiceFactory could return a ATSServiceResponseGeneratorDecorator implementing the interface without handling these kind of cases explicitely.
- Could also work for the ErrorHandlerService instead of catching the exceptions in the client code.
- Could also be used for offer synchronization by applying decorators at service instantiation time for company custom code instead of using inheritance. Might be overkill though.  

# Design patterns partially used

### [Builder](https://refactoring.guru/design-patterns/builder)

- Used in basile admin crud. ressemble because we don't use a bloated constructor.
- Not using a specific builder class but by passing directly an instantiated object
- Could be improved by creating an AdminCrudConfigBuilderInterface subclassed by AdminCrudConfigBuilder and AdminFormConfigBuilder. Not really the builder pattern because we would pass a specific builder class and not interface but close.

### [Prototype](https://refactoring.guru/design-patterns/prototype)

- Used in basile to clone newsletters
- Not respecting the prototype pattern semantics but using __clone magic method

# Design patterns that could improve existing projects

### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

- In basile ATSServiceFactory
- Instead of using a single class per ATS we could instead create one feature class per abstract ATS feature
- The current ats class could be replaced by a factory returning a feature class instance respecting the single responsibility principle.
- That would be beneficial for the status synchronization as we could have a single synchronizeStatusesInteface (with method synchronizeStatuses) instead of using a match in ATSSynchronizeStatusesService.
- Downside : would need a lot more classes and would complicate the subclassing of the ats code by a specific company's ats implementations.



### [Adapter](https://refactoring.guru/design-patterns/adapter)

- Maybe on ATS system to abstract the different protocols used (if one day we use more that are not rest ..?) 



