---
Title: "Software development techniques"
date: 2021-07-17
draft: false
summary: "My software development techniques memo"

---

> This is a opinionated and structured list of thoughts about development and what techniques I feel leads to strong code. It has a focus on what I would call "static code", that is how a codebase answering to a given problem should look like in the end. Not how you get there (development methods, prototyping ..) nor how to test / deploy / maintain code. It's a work in progress.
>
> <br/>
>
> Even though many concepts are well known, I'm writing them down the way I understand them.
>
> <br/>
>
> I've structured this document as going from lower level development techniques to higher level concepts like design patterns.

# Typing {#typing}

> This section is more focused on the typing experience you get from dynamically typed languages like Python / PHP.
>
> <br/>
>
> Made a distinction between 
>
> - <u>literal types</u>: types as seen by a type checker, 
> - <u>logical types</u>: types as how they carry logic and state
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

> Maybe the single most important (and simplest) rule is to not repeat / duplicate any information or logic in the codebase. It has architectural as well as technical implications. It is easier to spot and correct than to get right from the start.
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

# Design Patterns {#design-patterns}



> This section could be covered in a whole book so I'm gonna be brief for each point.


## Inheritance



#### The problems with inheritance

- Coupling between child and parent class
- namespace pollution
- Not easy to swap logic in the parent class

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

## Useful patterns for decoupling
- Decorator
- Observable

## API Design by contract

At the module level (e.g. client / server in a web project, APIs ..), some coupling is bound to happen. It happens with literals / configuration as well as logic. For specific cases like a web API using conventions like REST can reduce it. 

But as the 2 components trying to communicate with each other don't necessarily belong to the same codebase (or language) coupling can also happen with configuration data like route names and not be included in the typing system. The solution is to share the routing configuration outside of both parts in configuration files and use code generation to create sdks for both. Then the 2 parts do not need to know anything about the way to call the other (protocol etc ..) or a hardcoded path / url / string literal etc. The communication becomes part of the type system thanks to the code generation and the generated code can handle the parameter marshalling and validation. It will also instantiate and return the right objects. Using JSON Schema or Open API.

