---
title: "Head first design patterns"
draft: true
---

> and excerpts from https://refactoring.guru/

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
>
> in design patterns, the phrase “implement an interface” does NOT always mean “write a class that implements a Java interface, by using the ‘implements' keyword in the class declaration.” In the general use of the phrase, a concrete class implementing a method from a supertype (which could be a abstract class OR interface) is still considered to be “implementing the interface” of that supertype

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



# 2. The observer pattern

> Publishers + Subscribers = Observer Pattern

Observer never poll subject : `Don’t call me, I’ll call you!`

- The Observer Pattern defines a one-to-many relationship between a set of objects. 
- When the state of one object changes, all of its dependents are notified.
- Tight coupling between subject and observer classes
- Synchronous

### Is publish / subscribe an observer pattern ?

> - No, although they are related. The Publish-Subscribe pattern is a more complex pattern that allows subscribers to express interest in different types of messages and further separates publishers from subscribers. It is often used in middleware systems. 
> - The publisher-subscriber pattern can be considered as an improved (asynchronous and loosely-coupled) version of the observer pattern
> - It's many to many, asynchronous messaging system.
> - They introduce the concept of "topic" between publishers and subscribers
> - A pub/sub system is usually carried over the the network, whereas observer is local
> - Loose coupling of publishers and subscribers via the insertion of a message broker / bus. Broker usually implemented using a message queue to provide asynchronous behavior.
> - [Observer Pattern vs. Pub-Sub Pattern](https://towardsai.net/p/systems/observer-pattern-vs-pub-sub-pattern)
> - **Observer** pattern needs to be implemented in a single application address space. On the other hand, the **Publisher/Subscriber** pattern is more of a cross-application pattern

Thing to think about

- Passing the subject to the observer can make it unregister when necessary
- Passing data can be better **pull** than **push** to allow for evolving observers later on. And so that changing the enriching the data doesn't change existing observers (in the case of multiple arguments)
- Order of notifications to observers is not always garanteed.



# 3. The decorator pattern

One main advantage is **run time modification** of behavior of an object vs static behavior.

But it also simplifies the businness code by extracting responsibility from either objects or client code.

one of the flagship patterns of the **open-closed principle** and the **composition (and delegation) over inheritance principle**



### Open-closed principle
- Classes should be open for extension, but closed for modification
- Be careful when choosing the areas of code that need to be extended; applying the Open-Closed Principle EVERYWHERE is wasteful and unnecessary, and can lead to complex, hard-to-understand code
- The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.



### What we know about decorators

- Decorators have the same supertype as the objects they decorate. 
- You can use one or more decorators to wrap an object. 
- Given that the decorator has the same supertype as the object it decorates, we can pass around a decorated object in place of the original (wrapped) object. 
- **The decorator adds its own behavior before and/or after delegating to the object it decorates to do the rest of the job**. 
- Objects can be decorated at any time, so we can decorate objects dynamically at runtime with as many decorators as we like



#### Composition but still inheritance

- The patterns uses inheritance to achieve the type matching, but not to get behavior



#### Comparison with other patterns

- The pattern starts getting stronger when used in conjunction with Factory or Builder to centralize the composition.

- Contrary to the Chain of Responsibility pattern, decorators aren’t allowed to break the flow of the request

- Contrary to the Adapter pattern decorators have the same interface as the objects they decorate.

- Decorator ressembles composite but has a single child and adds behavior.

- Decorator lets you change the skin of an object, while Strategy lets you change the guts

  

#### Potential problems

- Adds a lot of small classes, can lead to an unclear design
- **typing problems**: you can usually insert decorators transparently and the client never has to know it’s dealing with a decorator
- introducing decorators can increase the complexity of the code needed to instantiate the component (then use **Factory** or **Builder**)
- It’s hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack





# 4. The factory pattern

> Using the new is coding against an implementation and not an interface. New is “closed for modification.”

## The Simple Factory

> The Simple Factory isn’t actually a Design Pattern; it’s more of a programming idiom

**Problem** : After the pizza type we add the pizza region to the app (that's two parameters for creating pizza).

**Solution 1**  : Create a pizza factory per region

**Problem**: If we process the pizza object after creation (in `orderPizza(string $type)`, we want the process to be in the factory but then we want to always use the same steps and not leave it to the factory implementation  !

## The Factory method

- We create an abstract factory class with method `orderPizza(string $type)` and abstract method `createPizza(string $type)` and change is insulated. 
- It's static behavior.
- This decouples the client code in the superclass (steps) from the object creation code in the subclass
- The Pizza subclasses can override steps (bake(), cut(), box() ..)
- With this behavior we need to create pizza classes for each combination of the 2 parameters (type and region)
- It create parallel hierarchies (abstract factory => abstract object and factory => object subclasses)
- The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
- The factory method (and abstract factory class) can be concrete to provide default values, in the absence of concrete factory subclasses

#### The factory method parameter(s)

- A factory method pattern using a parameter (here `string $type`) is called a **parameterized factory method**. But the pattern is still valid without parameters.
- NB : a string parameter is not type safe, better use constants or enums

#### Usage and advantages

Respects 

- "encapsulate what varies"
- "Single responsibility principle"
- "Open / closed principle"
- "Dependency Inversion Principle" : Depend upon abstractions. Do not depend upon concrete classes.
- Factory method is generally used when you have some generic processing in a class, but want to vary which kind of fruit you actually use
- that is usually implement code in the abstract creator that makes use of the concrete types the subclasses create.



#### Dependency inversion principle & guidelines

- Close to "Program to an interface, not an implementation" but goes further : suggests that our high-level components should not depend on our low-level components; rather, they should both depend on abstractions (here Pizza)

- Low level components (concrete pizza) depend on pizza
- High level components (pizza store) also depend on pizza (instantiated via subclasses)
- No variable should hold a reference to a concrete class
- No class should derive from a concrete class (but should derive from an abstraction !)
- No method should override an implemented method of any of its base classes.
- These are guidelines and not rules. Sometimes it's easier to violate them. Especially when the concrete class is not likely to change.

best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes (like here with pizza stores)

[Factory Method](https://refactoring.guru/design-patterns/factory-method) is a specialization of [Template Method](https://refactoring.guru/design-patterns/template-method). At the same time, a *Factory Method* may serve as a step in a large *Template Method*.

## The abstract factory

Let's imagine we also want to create ingredients with another family of objects (regions). We don't want specific shops to alter ingredients.

So we can inject a PizzaIngredientFactory in the concrete pizza class.

- The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- family of products = multiple product hierarchy

## Difference between factory method and abstract factory

- [Difference between simple factory / factory method / abstract factory, simple example](https://stackoverflow.com/questions/13029261/design-patterns-factory-vs-factory-method-vs-abstract-factory)

- **often the methods of an Abstract Factory are implemented as factory methods** -> Like Factory method but with multiple factory methods in a same class (here creating multiple ingredients)
- more technical : factory method uses (only) inheritance to create objects via subclassing whereas abstract factory uses composition (and inheritance because it uses factory method) by passing / instantiating the factory to the outer factory code. 
- In short
  - the factory method is used to create one object but usually some processing is done in the abstract factory once the object is created
  - the abstract factory is used to create a family of related objects but will not process them in the abstract factory class.



# 5. The Singleton Pattern

- There are many objects we only need one of: thread pools, caches, dialog boxes, objects that handle preferences and registry settings, objects used for logging, and objects that act as device drivers to devices like printers and graphics cards
- In many ways, the Singleton Pattern is a convention for ensuring one and only one object is instantiated for a given class
- Like a global variable but without the downside
- Lazy loading contrary to a global variable

> The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it

### Be careful about threads

- Trivial fix : `public static synchronized Singleton getInstance()`
- But synchronization is expensive and is not necessary when the object is singleton is already instantiated

**Solution**

- Do nothing else if `getInstance()` is not critical to the application
- Move to an eagerly created instance rather than a lazily created one: create the singleton in a static initialized (thread safe)
- Use “double-checked locking” to reduce the use of synchronization in getInstance()

**Also**

- It could be possible instead to use a class with only static variables / methods. But that can lead to subtle bugs, notably in java
- Be careful when using multiple class loaders and singleton
- reflection and serialization / deserialization can also present problems with Singletons
- **Singleton breaks the loose class coupling**: Modifying the singleton will have potential side effects in every class owning it. Common criticism of the pattern. 
- **Breaks the single responsibility principle** (somehow): by handing its own code + the single instantiation. Still it's a limited problem. Possible to abstract the instantiation code elsewhere.

**Should we subclass Singleton**

- Hard because the constructor is private and because a single variable holds the instance
- Possible by turning the constructor protected or public and use a registry of sorts in the base class
- But usually easier to duplicate the singleton instantiation code
- Having too many singletons is a code smell : singletons are meant to be used sparingly

**Don't use global variables, use singleton**

- global variable provides global access but does not ensure only one instance of the class exists
- global variable cannot provide eager instantiation
- pollute the global namespace

#### [Fixing possible class loading, reflection, serialization / deserialization issues](https://dzone.com/articles/java-singletons-using-enum)

- (de)Serialization will create a new object even if the constructor is private (java)
- The solution is that we have to implement the [readResolve](https://docs.oracle.com/javase/7/docs/platform/serialization/spec/input.html#5903) method, which is called when preparing the deserialized object before returning it to the caller.
- Reflection can set the private constructor to public and create another singleton. No way to protect from that

### Use an enum ! best way (in java)

```java
public enum Singleton {
    INSTANCE;
}
```



# 6. The Command Pattern

> In this chapter, we take encapsulation to a whole new level: we’re going to encapsulate method invocation. Being able to log and undo easily.

- The Command Pattern allows you to decouple the requester of an action from the object that actually performs the action.
- introduce command objects into the design
- The remote doesn’t have any idea what the work is, it just has a command object that knows how to talk to the right object to get the work done

# 9. The Iterator and Composite Patterns

### Composite

> In a tree mixed structure with leaf nodes and containers, be able to interface them to handle any case with the same interface 



# 10. The state of things

> Useful to structure multiple possible actions on an object having state
>
> Instead of checking the state of the object we isolate the actions in a class per state and kindof let the object do the work.

### State machine

- A state machine is composed of states and transitions between those states
- Only certain transitions are allowed 

### The pattern



# Other patterns

### Bridge

Useful when the code can be organized around two class hierarchies:

- abstraction : ui code that will call methods of an implementation. **ex: different remote controls**
- implementation : backend code that executes business logic. **ex: different tvs**

The relation between the 2 is called the bridge

> Useful in graphics and windowing systems that need to run over multiple platforms.
