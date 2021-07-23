---
Title: "Software development techniques"
date: 2021-07-17
draft: true
summary: "My software development techniques memo"

---

> This is a structured list of thoughts about development and an evolving reference of my techniques.
>
> I've structured this document as going from lower level development techniques to higher level concepts like design patterns.



The main concepts to strong code

- [Typing](#typing) 
- [DRY](#dry)
- [Decoupling & Design Patterns](#design-patterns)

# Typing {#typing}

> This section is more focused on the typing experience you get from dynamically typed languages like Python / PHP.

## Literal types: type-hints

> Use extensively language types / type-hinting possibilities. Makes dynamically typed languages feel more a statically typed ones and as such automatically detect a whole range of bugs that would have otherwise arisen at runtime.
>
> Maybe as importantly, it makes the code much easier to grasp at first sight and loosen the coupling between components at the type level.

- The editor should be configured to error about wrong parameter types.
- Setup static analysis tools (like mypy) with strict settings. They should be integrated in the IDE, run as pre-commit and in the pipeline.

## Logical types: Data Transfer Objects

- Use Data Transfer Objects as soon as the type hint system does not go deep enough. Make these DTO minimal and focused.
- Never manipulate arrays that contain mixed types as keys or values. Use DTO / custom classes instead.
- Never use literal string as dictionary indexes if you later need to subscript it directly. This violates DRY, does not play well with IDEs and makes refactoring painful.

## Structural types : interfaces & mixins

- "Code against interfaces". At a high level the program should look like interfaces interacting with each other thus enforcing the typing experience at this level also.
- See also [below](#design-patterns)



# DRY {#dry}

> Maybe the single most important (and simplest) rule is to not repeat / duplicate any information or logic in the codebase. It has architectural as well as technical implications. It is easier to spot and correct than to get right from the start.
>
> Here again I'll go from lower level (technical) techniques to higher level thinking.

## Literals

> Literal values are the simplest dry violation to spot, especially string ones. They should almost never happen

- Where are they allowed
- Not allowed
- environment variables
- Enums

### Enums

# Design Patterns {#design-patterns}

### Inheritance



##### The problems with inheritance

- 

- Problems

### Solutions
- Interfaces
- Delegation
- Mixins

### Useful patterns for decoupling
- Decorator
- Observable

### TDD
