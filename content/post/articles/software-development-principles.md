---
title: " Software development principles"
description: "My software development principles notes"
prod: true
draft: true
keywords:
  - Software development
  - Backend development
  - Design patterns
---


> I'm focusing on the languages I've used most : Python and PHP.
>
> I've structured this document as going from lower level development techniques to higher level concepts like design patterns.



# Type layers

> The definition of a type depends on the point of view of the observer. At a basic level, types can be seen as elements exposing a specific API to other types.This allows type checker to do their work. At a higher level though, types express business concepts, something a type checker will not understand but a developer will.
>
> As a consequence I chose not to describe what a type is but rather what a type layer.
>
> A type layer consists of types, how they are seen and what meaning they express, alone or in conjunction with other types
>
> I think we can split type layers in 3 categories : 
>
> - <u>type checker level types</u>: types as seen by a type checker and the IDE
> - <u>object level types</u>: types as how they encapsulate logic and state (entities, value objects, events, commands).
> - <u>module level types</u>: types as how they structure / architecture the module (interfaces)
>
> The two latter way of seeing types makes it possible to express business intent.



## Type checker layer

> In dynamically typed languages, compilation is replaced by type checking static analysis. We’ll have the best of both worlds : strongly typed feel and liberty of dynamism.

- This is the “dummy” level of types, how the type checker / editor sees them and how it (or the developer) can check the API of any variable.
- The editor as well as the type checker should be configured with strict settings.
- Tools  should be integrated in the IDE, run as pre-commit and in the test / deploy pipeline.
- Exploiting the full range of type generation will enforce a first layer of comprehension for the type checker / compiler and for the developers. (Optional / Enums / Lists / Unions /  Custom Types / Generics / Classes)



## Object level layer: Entities, Value objects, DTOs, events
- As soon as the type hint system does not go deep enough (php) or that we need to encapsulate logic or state we will start to define types that represent business logic or intent
- These types usually represent a class and express the logic relationship between objects
- They can carry identity (Entities) or only encapsulate some program logic (Value Objects)
- They can also carry intent of how the program operate during time (events)
- Naming : by using  the business model concepts / ubiquitous language, these types will become expressive and carry intent and meaning
- Point of view additions from the type checker types
  - A type now also means state and behavior
  - It expresses a real business concept
  - Relationships to other types start expressing meaning, not just API compatibility



## Module level layer : interfaces & mixins

- The most abstract type layer in that it doesn’t require the type to correspond to a specific class

-  Respects the "Code against interfaces". At a high level the program should look like interfaces interacting with each other

- The fact that interfaces can be implemented by multiple classes and express only public APIs make them appropriate for structuring the logic outline

  making them a great fit for structuring the logic at the module level.

- As interfaces define a type layer of its own, they could normally be tested independently

- Some of the typing consistency with the former layer can be checked with principles like Liskov Substitution.  

- More in-depth explanation [below](#design-patterns-design-patterns)



## Know when a type construct is strong

- It should be compatible with the IDE (autocompletion, warnings)
- It should be caught by the type checker
- It should emit runtime warnings
- it should be standard : well known, easily understandable by anyone (no black magic, and better not "complicated" language constructs like Python metaclasses etc ..)
- It should be elegant, focused and easily configurable
- It should prevent from going over the type system by using casts / runtime type checks etc ..

# [DRY](http://wiki.c2.com/?DontRepeatYourself) {#dry}

> Maybe the single most important rule is to reduce (code / information / logic) duplication in the codebase at the bar minimum.
> It has architectural as well as technical implications.
>
> Code Duplication brings a lot of troubles notably :
>
> - The drift between 2 code parts that should be united (bringing bugs, sometimes subtle)
> - A drop in the architectural quality of the codebase
> - A loss of meaning overall, because duplicate fragments usually mean a business concept is not expressed clearly
>
> It must be pointed out that by duplication we usually mean intent duplication, and that’s what should be tracked down.
>
> Sometimes this rule must be bent when other principles are at play, especially when the duplicated code cannot be factored in a way that's in accordance with business intent. 
>
> Here again I'll go from lower level (tactical) techniques to higher level thinking.



## Literals

> Literal values are the simplest dry violation to spot, especially string ones. They should almost never happen
> They can usually be replaced by enums and constants.

### Exceptions to this rule

- Documentation
- Logs
- String arguments for external library calls (use enums or class constants if possible)
- Coding conventions (e.g., the env file is called .env)

### In service code In service code Where are configuration literals allowed

- Environment (.env) for environment dependent variables and sensitive data 
- Configuration files (json, yaml ..) for global configuration variable as to centralize them and change them easily
- Enumerations: They are great and should be used extensively whenever multiple literals can be grouped together.
- Class constants :
  - Private constants only accessed by the class can be useful.
  - Downsides :
    - Public class constants break encapsulation and expose internals of a class
    - Using them with inheritance can be confusing
    - Don't necessarily play well with interfaces
- Config objects : they are very useful as soon as we pay attention to not break module cohesion by tearing away config values belonging to a module / class.

## Logic, knowledge and intent

- pure knowledge duplication is terrible and should be avoided at all costs.
- Duplication is subtly present when different part of a system know about the internal of other parts.
  It's called implicit knowledge and is closely related to [Decoupling](#decoupling).
- Ideally modules and classes should be self contained and not little to nothing about other system parts or the system as a whole.
- Design patterns and composition help greatly reduce coupling between components.
- At the codebase level, setting up a layered architecture like Domain Driven Design will efficiently reduce components coupling at the global level.



# Decoupling

> Coupling is the enemy of change because it transitively links together things that must change in parallel.

## Main 00 concepts

- Identify the aspects of your application that vary and separate them from what stays the same.
- Program to an interface, not an implementation.
- Favor composition over inheritance : composition is relationship defined at runtime, inheritance represents static relationships.
- Strive for loosely coupled designs between objects that interact.

## Loose coupling

- Loose coupling is coupling on an interface instead of implementation.
- All the rest can change without bringing breaking changes

## Encapsulation

- Tell, don't ask : objects internals should not be available and known to the client code
- See also Law of Demeter
- The severity of the encapsulation is a pragmatic decision 



## Inheritance

The canonical way to use inheritance is when we have different kind of classes related 
to a parent class with only minimal changes necessary, and usually not core logic changes.

Inheritance can in this case supply some logic to a range of class while also marking them as child of an abstract class allowing polymorphism.

NB : polymorphism is also possible by implementing interfaces and it is the best way to do it.

Most other kind of usages (especially inheriting behaviour) can usually be replaced by a better pattern.

### The problems with inheritance

- Coupling between child and parent class : any change in the parent will affect all child classes as soon as they start using their parent class internals.
- Semantically the parent class can lose its (semantic) meaning especially when the child class partially uses the parent class. 
- Inheritance is much harder to test (over composition)
- Code gets confusing as soon as multiple levels are involved, even without considering multiple inheritance

### Solutions

- Interfaces / Mixins / Traits
- Composition / Delegation
- Design Patterns

## How can we abstract multiple similar classes ?

- Create an interface and its default implementation in a mixin

- Using the interface + mixin is the most modular as any client class can declare implementing different interfaces

- We can still have client classes extending an abstract class for common stuff to all classes. 
  This abstract class should probably not implement an interface (except in specific patterns like Factory Method / Abstract Factory)
  
- Using this technique we are open to modification by simply implementing another interface + adding an optional mixin

  

## Encapsulation and state

- Law of Demeter : a class should not expose sub objects only a clean and minimal interface. See [Wikipedia](https://fr.wikipedia.org/wiki/Loi_de_D%C3%A9m%C3%A9ter) 
- An object should be responsible for managing its own logic, expose only the necessary getters
- Object containing state should manage it themselves and expose few to no setters
- Value objects should be immutable



## [Liskov substitution principle](https://stitcher.io/blog/liskov-and-type-safety)

> Inheritance is not like "re-using parts of the parent type, and overriding other parts in the sub-type", 
> rather it is extending the behaviour defined by its parent. This is what the LSP guards against.

Rules :

- There must be contravariance of the method arguments in the subtype. This is valid for exceptions thrown as well.
- There must be covariance of the return types in the subtype.
- NB : usually checking the type of an object at runtime is a code smell as it breaks the LSP and exposes lower level code internals.

### Invariance in PHP

PHP allows polymorphism and follows the LSP by forbidding subclass methods to :

- use subtypes in parameters types
- use parent types in return type

It also follows the LSP since version 7.4 by allowing :

- Covariance: allows a child's method to return a more specific type than the return type of its parent's method
- Contravariance: allows a parameter type to be less specific in a child method, than that of its parent




# Design Patterns {#design-patterns}

> https://refactoring.guru/design-patterns
>
> When should we use patterns ? At any time of the development process. But usually when refactoring. Say
>
> - first try : simple implementation tied to specific classes
> - second try: maybe still the same
> - third try : refactoring using design patterns

# Creational Patterns

## [Static Creation method](https://refactoring.guru/design-patterns/factory-comparison)

- Not a real pattern but just the classical static creation method
- Simpler to spot in code, single responsibility, and useful when the constructor cannot accept arguments 
  (e.g. using fixtures) 
- Can leverage singleton

## [Factory method](https://refactoring.guru/design-patterns/factory-method)

> Used when we don't know the exact type and dependencies of the object, as well as to simplify object creation.

- Let the object instantiation be done by  a Creator class.
- created objects must implement an interface
- Creator classes can be subclassed to return different implementations of the product interface
- Allows extension by creating new product creator and classes
- Follows single responsibility (one place to create) and open / closed (extensible via inheritance)

> NB : the factory method is great at dissociating conditionals for one or specific variable / enum.
>
> It's not always easy to work with multiple variables / enum classes changing and be DRY.
>
> Using decorators inside a factory class can solve this and is a strong pattern.


# [Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)

## [Template method](https://refactoring.guru/design-patterns/template-method)

> defines the skeleton of an algorithm in the superclass but lets subclasses override 
> specific steps of the algorithm without changing its structure

- Mandatory steps are abstract methods in base class
- Default steps are normal methods in base class (with implementation)
- hooks are empty methods in base class
- Useful but not so clear code. Hard to find the balance with full configurability and too small steps. 
- Can break LDP by removing base class behavior.

## [Observer](https://refactoring.guru/fr/design-patterns/observer)

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/observer.PNG?raw=true)

- This pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically. 
- The observers are *dependent* (coupled) on the subject
- Many **observers** **subscribe** to one **subject**. They are **notified** of its changes.
- The observers usually have a pointer to the subject (e.g. for unsubscribing).
- Follows the Hollywood Principle : don't call us we'll call you (move from pull to push)
- Follows open / closed and modifiable at runtime. Example of **loose coupling**.
- Simple and strong but introduces coupling when the observers need to register directly on the observable. 
- Makes sense when the coupling already exists and for small problematics.
- Otherwise, something like Mediator, Pub/Sub or event bus can remove this coupling.
{{% code file="/static/code/observer/main.py" language="python" %}}

## Event systems

> Event systems have all the same goal of decoupling the passage of information between a producer / emitter / subject / observable and a consumer / listener / subscriber / observer.
>
> They have very diverse implementations and differ in the way the information is called, passed, dispatched and transmitted to the consumer(s). Decoupling impact can vary as well.
>
> Semantically, the producer and consumer can be passive or active in the way they emit / subscribe or are notified.

### Mediator

- An evolution of the observer pattern removing the coupling between observable and observer
- The mediator object is an interface injectable in all subjects with a single notification method
- Subjects can pass a context to the notification method but should try to not increase coupling by passing themselves in the context
- Concrete mediators can maintain state and include some logic about managing subjects
- Overlaps with the event bus, but the mediator has a more complex role in controlling the objects interactions


### Event bus

- Event systems can be heavy, sometimes a simple event bus that acts as global state is simpler to handle
- Objects can emit event directly on the bus and subscribers can subscribe to events.
- This has very low coupling at the price of a loss of visibility about subject / observer interactions.
- The event trail can be logged / monitored / error handled and replayed.

### Pub / Sub

- Evolution of the observer :  allows subscribers to express interest in different types of messages and further separates publishers from subscribers. 
  It is often used in middleware systems.The observer is a **subscriber**, and the subject is a **publisher** and does not know about its subscribers. 
  Deals well with asynchronous code. Message passing is decoupled from the sender code.
- Scales well.
- Message queuing is a special case of pub/sub with usually only one subscriber per message type, and asynchronous.
- More complex to grasp at first sight as the publish / subscribe are done in different places.


## Reactive programming

- Another way to handle asynchronous (or sync) events and queries is to reason with streams
- Reduces coupling and greatly reduces state
- Reduces boilerplate code to handle loops and logic on iterables
- Push based (more natural when reacting to events)

## Client - Service communication via schema

There is one problem that arise when multiple components want to talk together in a system. 
It is especially visible when exposing software functionality over an API : 
The client needs to know how to contact the service.
That can include : a protocol, paths or method names, parameter types etc.

This means some information about the structure of the service is duplicated. 
In a http API that could be simply the http verb and the url. 

The problems that arise include the following :

- Information and logic (parameters validation / marshalling) duplication
- The typing information is lost when e.g. the 2 components communicate over plain text or bytes. 
  This weakens the system as a whole.
- The refactoring becomes less straightforward and bugs can creep in due to the 2 above reasons.

A way to centralise the service interface definition is to have it available as text e.g. using json schemas, 
either doing code-first or schema-first development. These remove information duplication. 
Starting from a json schema we can simply generate sdks for any client. 
We get to :

- Completely hide the communication part of the code, be able to switch protocols, and remove any reference to the fact that we are not using local code.
- Have a typing experience approaching the one inside the rest of the codebase.

Code generation has the additional benefit of reducing the number of moving parts in the code even if it can of course be modified.
Increases system decoupling and reduce mental overhead

# [SOLID](https://en.wikipedia.org/wiki/SOLID)

### [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle): 

- "There should never be more than one reason for a [class](https://en.wikipedia.org/wiki/Class_(computer_programming)) to change."[[5\]](https://en.wikipedia.org/wiki/SOLID#cite_note-5) In other words, every class should have only one responsibility.[[6\]](https://en.wikipedia.org/wiki/SOLID#cite_note-cleancode-6)
- Factory method, Abstract Factory
### [Open–closed principle](https://en.wikipedia.org/wiki/Open–closed_principle)
- "Software entities ... should be open for extension, but closed for modification."[[7\]](https://en.wikipedia.org/wiki/SOLID#cite_note-7)
  Open for extension would mean composition and interfaces (e.g. using dependency injection). 
- Observer, Decorator, Factory method, Abstract Factory

### [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle)
- "Functions that use pointers or references to base classes must be able to use objects of derived classes 
  without knowing it."[[8\]](https://en.wikipedia.org/wiki/SOLID#cite_note-:0-8) See also [design by contract](https://en.wikipedia.org/wiki/Design_by_contract).[[8\]](https://en.wikipedia.org/wiki/SOLID#cite_note-:0-8). LSP violation can be detected by the usage of instance of as it expects different behavior from objects with the same interface. More specific version of open/closed.
- Linked with polymorphism

### [Interface segregation principle](https://en.wikipedia.org/wiki/Interface_segregation_principle)
- "Many client-specific interfaces are better than one general-purpose interface."[[9\]](https://en.wikipedia.org/wiki/SOLID#cite_note-9)[[4\]](https://en.wikipedia.org/wiki/SOLID#cite_note-martin-design-principles-4). Also meaning inheritance should be restricted and replaced by specific interface / traits. 
  Note: as a result interfaces should ideally not extend other interfaces.

### [Dependency inversion principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
- "Depend upon abstractions, [not] concretions."[[10\]](https://en.wikipedia.org/wiki/SOLID#cite_note-10)[[4\]](https://en.wikipedia.org/wiki/SOLID#cite_note-martin-design-principles-4)
- Factory method, Abstract Factory

# Misc

## Error handling

- Use assertions for unexpected conditions : at the top of the methods and catch / log / report assertion bugs 
- Use exceptions for normal error conditions : use inheritance to create an exceptions tree.
- Prefer throwing exceptions instead of returning null on error

<hr>
**Bibliography**

- https://refactoring.guru/design-patterns
- [The Pragmatic Programmer, 20th Anniversary Edition](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [Head First Design Patterns, 2nd Edition](https://www.oreilly.com/library/view/head-first-design/9781492077992/)
- [Domain Driven Desing in PHP](https://www.amazon.fr/Domain-Driven-Design-PHP-Carlos-Buenosvinos/dp/1787284948)
<hr>

[^1]: [Comparing Publish-Subscribe Messaging and Message Queuing](https://dzone.com/articles/comparing-publish-subscribe-messaging-and-message)

[^2]: [http://reactivex.io/](http://reactivex.io/)

