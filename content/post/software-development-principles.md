---
title: "Software development techniques"
description: "My software development techniques notes"
keywords:
  - Software development
  - Backend development
  - Design patterns

---


> I'm focusing on the languages I've used most : Python and PHP.
>
> I've structured this document as going from lower level development techniques to higher level concepts like design patterns.

# Typing {#typing}

> Made a distinction between 
>
> - <u>literal types</u>: types as seen by a type checker, 
>- <u>logical types</u>: types as how they carry logic and state
> - <u>structural types</u>: interfaces, how components are structured at the higher level of the codebase

## Literal types: type-hints

> Using extensively language types / type-hinting possibilities makes dynamically typed languages feel more a statically typed ones and as such automatically detect a whole range of bugs that would have otherwise arisen at runtime. Compilation is replaced by type checkers static analysis.
>
> <br/>
>
> Maybe as importantly, it makes the code much easier to grasp at first sight and feels like loosening the coupling between components at the type level (we don't need to understand what a method logically returns only what type it returns)

- The editor should be configured to error about wrong parameter types.
- Setup static analysis tools (like mypy) with strict settings. They should be integrated in the IDE, run as pre-commit and in the test / deploy pipeline.

## Logical types: [Data Transfer Objects](https://martinfowler.com/eaaCatalog/dataTransferObject.html)

> DTOs handling can be painful and should generally not be used to encapsulate function parameters. 

- As soon as the type hint system does not go deep enough (php) or that we need to encapsulate state we could use Data Transfer Objects . Make these DTO minimal and focused with no domain logic attached.
- Can be useful to encapsulate serialization in c
- Use language constructs like python's decorator `@dataclass`. 
- Never manipulate arrays that contain mixed types as keys or values. Use DTO / custom classes instead + enums.
- Never use literal string as dictionary indexes if you later need to subscript it directly. This violates DRY, does not play well with IDEs and makes refactoring painful.

## Structural types : interfaces & mixins

- "Code against interfaces". At a high level the program should look like interfaces interacting with each other thus enforcing the typing experience at this level also.
- More in-depth explanation [below](#design-patterns) 

# [DRY](http://wiki.c2.com/?DontRepeatYourself) {#dry}

> Maybe the single most important (and simplest) rule is to reduce (code / information / logic) duplication in the codebase at the bar minimum. It has architectural as well as technical implications. It is easier to spot and correct than to get right from the start.
>
> Here again I'll go from lower level (technical) techniques to higher level thinking.

## Literals

> Literal values are the simplest dry violation to spot, especially string ones. They should almost never happen

Literal values (especially strings) usually belong to configuration / data and should be banned from code files containing logic, e.g. services.

### Exceptions to this rule

- Documentation
- Logs
- String arguments for external library calls (use enums or class constants if possible)
- Hardcoded filenames 
- Coding conventions (e.g. the env file is called .env)

### Where are configuration literals allowed

- Environment (.env) for environment dependent variables and sensitive data 
- Configuration files (json, yaml ..) for global configuration variable as to centralize them and change them easily
- Enumerations
  - They are great and should be used extensively whenever multiple literals can be grouped together.
  - Enums can be grouped at the same place in the codebase making it easier to see configuration values at a glance. 
  - They can also be stored to store more complex data than an object and in this case getters should be added to the enum class.
  - They can be used with database columns.
- Class constants :
  - They can be useful especially when prototyping but should not be used when literals can be stored in enums or configuration files.
  - Private constants only accessed by the class can be useful.
  - Downsides :
    - Public class constants break encapsulation and expose internals of a class
    - Using them with inheritance can be confusing
    - Don't play well with refactoring components in sub components.
    - Don't necessarily play well with interfaces 
    - Configuration data is spread over many files
    - It's better to keep configuration away from logic

## Logic and knowledge

- duplication is present when different part of a system knows the internal of other parts. It's called implicit knowledge and is closely related to [Decoupling](#decoupling)

# Decoupling

> Coupling is the enemy of change because it transitively links together things that must change in parallel.



## Main 00 concepts

- Identify the aspects of your application that vary and separate them from what stays the same.
- Program to an interface, not an implementation.
- Favor composition over inheritance : composition is relationship defined at runtime, inheritance represents static relationships.
- Strive for loosely coupled designs between objects that interact.



## Loose coupling

- Loose coupling is coupling on an interface instead of implementation.
- All the rest can change without bring breaking changes

## Encapsulation

- Tell, don't ask : objects internals should not be available and known to the client code
- See also Law of Demeter
- The severity of the encapsulation is a pragmatic decision 

## Inheritance

The canonical way to use inheritance is when we have different kind of classes related to a parent class with only minimal changes necessary, and usually not core logic changes. Most other kind of usages can usually be replaced by a better pattern. 

### The problems with inheritance

- Coupling between child and parent class : any change in the parent will affect all child classes. 
- using inheritance when using only part of the parent class interface is bad because of the law of demeter. 
- Semantically the parent class can loose its (semantical) meaning especially when the child class partially uses the parent class. 
- Not so easy to swap logic in the parent class if the class internals are used by the child classes.
- Code gets confusing as soon as multiple levels are involved, even without considering multiple inheritance

### Solutions

- Interfaces
- Delegation
- Mixins

## How can we abstract multiple similar classes ?

- Create an interface
- Interface default implementation can be :
  - In an abstract class 
  - In a mixin
- Using the interface + mixin is the most modular as any client class can declare implementing different interfaces --> best
- We can still have client classes extending an abstract class for common stuff to all classes. This abstract class does not necessarily implement an interface (except if we want to get more abstraction when using it in factories / mocks / dependency injection ..)

##### Special case two level inheritance vs single level + interface / mixin

> When subclassing a class already inheriting from an abstract class the simple way is to directly inherit from this parent class and add methods to it
>
> The flexible way is to make this parent class an interface (if only its subclasses are gonna be instantiated) and create a mixin. This approach has two advantages :
>
> - it's a bit clearer as we can type hint on the interface. Also multiple inheritance levels are not so readable (two clicks away from the abstract class vs one)
> - it's open to modification by simply implementing another interface + adding a mixin
>
> I think it's useful even if the child classes are never gonna implement another interface. 



## Building interfaces

- Law of Demeter : a class should not expose sub objects only a clean and minimal interface. See [Wikipedia](https://fr.wikipedia.org/wiki/Loi_de_D%C3%A9m%C3%A9ter) 
- Consequence &rarr; encapsulation. An object should be responsible for managing its own logic.  

## State

- Logic and state should not be mixed
- State should be encapsulated in Data objects handling only minimal logic 

## Other principles

- Uniform access: hide the implementation details (see [Encapsulation](#encapsulation)]). Python's `@property`

# Design Patterns {#design-patterns}

> https://refactoring.guru/design-patterns
>
> When should we use patterns ? At any time of the development process. But usually when refactoring. Say
>
> - first try : simple implementation tight to specific classes
> - second try: still the same
> - third try : refactoring using design patterns



# Creational Patterns



## [Static Creation method](https://refactoring.guru/design-patterns/factory-comparison)

- Not a real pattern but just the classical static creation method
- Simpler to spot in code, single responsibility, and useful when the constructor cannot accept arguments (e.g. using fixtures) 
- Can leverage singleton

## [Factory method](https://refactoring.guru/design-patterns/factory-method)

> Used when we don't know the exact type and dependencies of the object, as well as to simplify object creation.

- Let the object instantiation be done by  a Creator class.
- `def create() -> ProductInterface` (let's use create instead of make)
- created objects must implement an interface
- Creator classes can be subclassed to return different implementations of the product interface
-  Allows extension by creating new product creator and classes
- Follows single responsibility (one place to create) and open / closed (extensible via inheritance)



## Finite State Machines

> or workflows

- Finite possible states with a current state
- Each state defines events (or transitions) that change the current state and can trigger actions
- Simple to implement
- Centralizes the state transformation away from the core logic
- Use an enum for states



## Event systems

> Event systems have all the same goal of decoupling the passage of information between a producer / emitter / subject / observable and a consumer / listener / subscriber / observer.
>
> They have very diverse implementations and differ in the way the information is called, passed, dispatched and transmitted to the consumer(s). Decoupling impact can vary as well.
>
> Semantically, the producer and consumer can be passive or active in the way they emit / subscribe or are notified.



# [Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)



## [Template method](https://refactoring.guru/design-patterns/template-method)

> defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure
>
> Implemented in offers synchronization at Basile.

- Mandatory steps are abstract methods in base class
- Default steps are normal methods in base class (with implementation)
- hooks are empty methods in base class
- Useful but not so clear code. Hard to find the balance with full configurability and too small steps. Can break lsp by removing base class behavior.

### [Observer](https://refactoring.guru/fr/design-patterns/observer)


{{< figure src="/img/observer.PNG" title="observer class diagram" >}}


- Behavioral design pattern, the Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically. The observers are *dependent* (coupled) on the subject
- Many **observers** **subscribe** to one **subject**. They are **notified** of its changes.
- The observers usually have a pointer to the subject (e.g. for unsubscribing).
- Usually better to use observer **pull** than subject **push** (passing parameters in the update method) as it's less flexible.
- Follows open / closed and modifiable at runtime. Example of **loose coupling**.
- A good evolution is to use callables implementing the update signature instead of classes.
- Simple and strong but introduces coupling when the observers need to register directly on the observable. Makes sense when the coupling already exists and for small problematics.
{{% code file="/static/code/observer/main.py" language="python" %}}
- Close to the mediator pattern (which removes the coupling between oberserver and observable by introducing a third mediator object in between). Correspond to a central event bus.



### Mediator

- An evolution of the observer pattern removing the coupling between observable and observer
- The mediator object is an interface injectable in all subjects  with a single notification method
- Subjects can pass a context to the notification method but should try to not increase coupling by passing themselves in the context
- Concrete mediators can maintain state and include some logic about managing subjects
- Overlaps with the event bus pattern but some say that the mediator has a more complex role in controlling the objects interactions



### Event bus

> Implemented at basile

- Event systems can be heavy, sometimes a simple event bus that acts as global state is simpler to handle
- Objects can emit event directly on the bus and subscribers can subscribe to events.



### Pub / Sub

- Evolution of the observer :  allows subscribers to express interest in different types of messages and further separates publishers from subscribers. It is often used in middleware systems.The observer is a **subscriber** and the subject is a **publisher** and does not know about its subscribers. Deals well with asynchronous code. Message passing is decoupled from the sender code.
- Scales well.
- Message queuing is a special case of pub/sub[^1] with usually only one subscriber per message type, and asynchronous.
- More complex to grasp at first sight as the publish / subscribe are done in different places.

  


## Reactive programming[^2]

- Another way to handle asynchronous (or sync) events and queries is to reason with streams
- Reduces coupling and greatly reduces state
- Reduces boilerplate code to handle loops and logic on iterables
- Push based (more natural when reacting to events)

## Client - Service communication via schema

There is one problem that arise when multiple components want to talk together in a system. It is especially visible when exposing software functionality over an API : _The client needs to know how to contact the service_. That can include : a protocol, paths or method names, parameter types etc.

This means some information about the structure of the service is duplicated. In an http API that could be simply the http verb and the url. This problem is present also inside a single local codebase when a client piece of software calls a supplier but have subtler implications. 

The problems that arise include the following :

- Information and logic (parameters validation / marshalling) duplication
- The typing information is lost when e.g. the 2 components communicate over plain text or bytes. This weakens the system as a whole.
- The refactoring becomes less straightforward and bugs can creep in due to the 2 above reasons.

A way to centralise the service interface definition is to have it available as text e.g. using json schemas, either doing code-first or schema-first development. These removes information duplication. Starting from a json schema we can simply generate sdks for any client. And use for example decorators to expose the service public interface. We get to :

- Completely hide the communication part of the code, be able to switch protocols, and remove any reference to the fact that we are not using local code.
- Have a typing experience approaching the one inside the rest of the codebase.

Code generation has the additional benefit of reducing the number of moving parts in the code even if it can of course be modified. Increases system decoupling and reduce mental overhead



# [SOLID](https://en.wikipedia.org/wiki/SOLID)

- The [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle): "There should never be more than one reason for a [class](https://en.wikipedia.org/wiki/Class_(computer_programming)) to change."[[5\]](https://en.wikipedia.org/wiki/SOLID#cite_note-5) In other words, every class should have only one responsibility.[[6\]](https://en.wikipedia.org/wiki/SOLID#cite_note-cleancode-6)
- The [Open–closed principle](https://en.wikipedia.org/wiki/Open–closed_principle): "Software entities ... should be open for extension, but closed for modification."[[7\]](https://en.wikipedia.org/wiki/SOLID#cite_note-7)
  Open for extension would mean association and interfaces (e.g. using dependency injection). Also present in e.g. factory patterns that create more implementations without modifying client code. 
- The [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle): "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."[[8\]](https://en.wikipedia.org/wiki/SOLID#cite_note-:0-8) See also [design by contract](https://en.wikipedia.org/wiki/Design_by_contract).[[8\]](https://en.wikipedia.org/wiki/SOLID#cite_note-:0-8). LSP violation can be detected by the usage of instance of as it expects different behavior from objects with the same interface. More specific version of open/closed.
- The [Interface segregation principle](https://en.wikipedia.org/wiki/Interface_segregation_principle): "Many client-specific interfaces are better than one general-purpose interface."[[9\]](https://en.wikipedia.org/wiki/SOLID#cite_note-9)[[4\]](https://en.wikipedia.org/wiki/SOLID#cite_note-martin-design-principles-4). Also meaning inheritance should be restricted and replaced by specific interface / traits. Note: as a result interfaces should ideally not extends other interfaces.
- The [Dependency inversion principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle): "Depend upon abstractions, [not] concretions."[[10\]](https://en.wikipedia.org/wiki/SOLID#cite_note-10)[[4\]](https://en.wikipedia.org/wiki/SOLID#cite_note-martin-design-principles-4)

# ETC

## Error handling

- Use assertions for unexpected conditions : at the top of the methods and catch / log / report assertion bugs 
- Use exceptions for normal error conditions : use inheritance to create an exceptions tree.
- Prefer throwing exceptions instead of returning null

<hr>
**Bibliography**

- https://refactoring.guru/design-patterns

- [The Pragmatic Programmer, 20th Anniversary Edition](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [Head First Design Patterns, 2nd Edition](https://www.oreilly.com/library/view/head-first-design/9781492077992/)

<hr>

[^1]: [Comparing Publish-Subscribe Messaging and Message Queuing](https://dzone.com/articles/comparing-publish-subscribe-messaging-and-message)

[^2]: [http://reactivex.io/](http://reactivex.io/)

