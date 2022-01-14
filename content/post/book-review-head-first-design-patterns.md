---
title: "Head first design patterns"
draft: true
---

# 1. Intro to design patterns

Example of ducks (quacking, flying)

- Example 1 : abstract duck class with display(), quack(), fly(): tight coupling to the superclass, behavior not modifiable at run time
- Example 2 : Using Flyable and Quackable interfaces: code duplication in all subclasses. No code reuse

Advice: 

> Identify the aspects of your application that vary and separate them from what stays the same. 
>
>  take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don’t.

- Example 3 : isolate (encapsulate) behaviors in specific class implementing an interface.

<img src="C:\Users\thiba\Downloads\Capture.PNG" alt="Capture" style="zoom:50%;" />

#### “Program to an interface” really means “Program to a supertype.”

> An abstract supertype (could be an abstract class OR interface). The important part is that we don't know the concrete type. That's what program to an interface really means.

**What we get**:

With this design, other types of objects can reuse our fly and quack behaviors because these behaviors are no longer hidden away in our Duck classes! And we can add new behaviors without modifying any of our existing behavior classes or touching any of the Duck classes that use flying behaviors.

Also : we can add setters to modify behaviors at run time (e.g. start with default implementation and modify it in a factory method)

*comment: using association coupled with interface moves the complexity and change to another axis making it more manageable*

**Vocabulary: ** set of behavior == family of algorithm

#### Design principles:

- Identify the aspects of your application that vary and separate them from what stays the same.
- Program to an interface, not an implementation.
- Favor composition over inheritance.

**Composition: ** Not only does it let you encapsulate a family of algorithms into their own set of classes, but it also lets you change behavior at runtime

> We spend more time in maintaining than developing. We should favor maintainability and extensibility over reuse. That is composition over inheritance.

--> We used the **strategy pattern** : The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.



# 3. The decorator pattern

One main advantage is run time modification of behavior of an object.

But it also simplifies the businness code by extracting responsibility from either objects or client code.

one of the flagship patterns of the **open-closed principle** and the **composition (and delegation) over inheritance principle**

- Decorators should have the same supertype as objects they wrap
- They can add behavior before or after the wrapped object call
- The patterns uses inheritance to achieve the type matching, but not to get behavior
- The pattern starts getting stronger when used in conjunction with Factory or Builder to centralize the composition.



# 4. The factory pattern

> Using the new is coding against an implementation and not an interface

**problem**: a classical approach 



# 9. The Iterator and Composite Patterns

### Composite

> In a tree mixed structure with leaf nodes and containers, be able to interface them to handle any case with the same interface 

# Other patterns

### Bridge

Useful when the code can be organized around two class hierarchies:

- abstraction : ui code that will call methods of an implementation. **ex: different remote controls**
- implementation : backend code that executes business logic. **ex: different tvs**

The relation between the 2 is called the bridge

> Useful in graphics and windowing systems that need to run over multiple platforms.
