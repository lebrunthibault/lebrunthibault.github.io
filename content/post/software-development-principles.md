---
Title: "Software development techniques"
date: 2021-07-17
draft: false
summary: "My software development techniques memo"

---

> This is a opinionated and structured list of thoughts about software development and what techniques I feel leads to strong code. 
>
> I'm focusing on the languages I've used most : Python and PHP. That is on Object Oriented, dynamically typed languages.
>
> It has a focus on what I would call "static code", that is how a codebase answering to a given problem should look like at release time. Not how you get there (development methods, prototyping ..) nor how to test / release / maintain code. 
>
> It's a work in progress.
>
> <br/>
>
> Even though many concepts are well known, I'm writing them down the way I understand them.
>
> <br/>
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

## Logical types: Data Transfer Objects

- As soon as the type hint system does not go deep enough or that we need to encapsulate state we should use Data Transfer Objects . Make these DTO minimal and focused.
- Never manipulate arrays that contain mixed types as keys or values. Use DTO / custom classes instead + enums.
- Never use literal string as dictionary indexes if you later need to subscript it directly. This violates DRY, does not play well with IDEs and makes refactoring painful.

## Structural types : interfaces & mixins

- "Code against interfaces". At a high level the program should look like interfaces interacting with each other thus enforcing the typing experience at this level also.
- More in-depth explanation [below](#design-patterns) 



# DRY {#dry}

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
- Enumerations ❤
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



# Decoupling

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

## Building interfaces

- Law of Demeter : a class should not expose sub objects only a clean and minimal interface. See [Wikipedia](https://fr.wikipedia.org/wiki/Loi_de_D%C3%A9m%C3%A9ter) 
- Consequence &rarr; encapsulation. An object should be responsible for managing its own logic.  

## State

- Logic and state should not be mixed
- State should be encapsulated in Data objects handling only minimal logic 

## Other principles

- Uniform access: hide the implementation details (see encapsulation). Python's `@property`

# Design Patterns {#design-patterns}



> This section could be covered in a whole book so I'm gonna be brief for each point.

## Useful patterns for decoupling
- Decorator
- Observable

## Client - Service communication

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
