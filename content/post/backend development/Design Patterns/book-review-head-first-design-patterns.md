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

- An abstract supertype (could be an abstract class OR interface). The important part is that we don't know the concrete type. That's what program to an interface really means.
- in design patterns, the phrase “implement an interface” does NOT always mean “write a class that implements a Java interface, by using the ‘implements' keyword in the class declaration.” In the general use of the phrase, a concrete class implementing a method from a supertype (which could be a abstract class OR interface) is still considered to be “implementing the interface” of that supertype

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

## The Strategy pattern

> Favor composition over inheritance.
>
> The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

- We used the **strategy pattern** : The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- Strategy works by using composition and delegation
- Strategy allows runtime behavior change
- The strategy pattern really encapsulate a **family of algorithms**

- *Template Method* works at the class level, so it’s static. *Strategy* works on the object level, letting you switch behaviors at runtime.

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
- The factory method is protected

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
  - the abstract factory is used to create a family of related objects but will not necessarily process them in the abstract factory class.



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
- So, here the requester would be the remote
  control and the object that performs the action would be an instance of one of your
  vendor classes.
- introduce command objects into the design.
- The remote doesn’t have any idea what the work is, it just has a command object that knows how to talk to the right object to get the work done



### The order example

- Think of the Order Slip as an object that acts as a request to prepare a meal.
- Unique method orderUp + reference to the cook object
- The Short-Order Cook is the object that really knows how to prepare meals. Totally decoupled from the waitress



## Pattern

![image-20220222135349158](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220222135349158.png)





![image-20220222135838913](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220222135838913.png)



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220222140325537.png" alt="image-20220222140325537" style="zoom:50%;" />



- binding together a set of actions on a specific receiver : set of actions == command class. Specific receiver == class parameter.
- Back at the diner, the Waitress was parameterized with multiple orders (commands) throughout the day. **Waitress is an invoker**
- The command may / should be immutable
- Most commands only handle the details of how a request is passed to the receiver, while the receiver itself does the actual work
  - In general, we strive for “dumb” command objects that just invoke an action on a receiver; however, there are many
    examples of “smart” command objects that implement most, if not all, of the logic needed to carry out a request. Certainly you can do this; just keep in mind you’ll no longer have the same level of decoupling between the invoker and receiver, nor will you be able to parameterize your commands with receivers.
- As with any other object, a command can be serialized, which means converting it to a string that can be easily written to a file or a database. Later, the string can be restored as the initial command object. Thus, you can delay and schedule command execution. But there’s even more! In the same way, you can queue, log or send commands over the network

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220222143043044.png" alt="image-20220222143043044" style="zoom:50%;" />



> For commands with only one abstract method we can use lambda functions (e.g. for on and off)



## Undo

- add undo to the abstract command class
- implement in subclasses, potentially keeping state

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220222143541765.png" alt="image-20220222143541765" style="zoom:50%;" />



## Macro commands



# 7. The Adapter and Facade Patterns

## Adapter

- The client makes a request to the adapter by calling a method on it using the target interface.
- The adapter translates the request into one or more calls on the adaptee using the adaptee interface.
- The client receives the results of the call and never knows there is an adapter doing the translation.

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220223105440918.png" alt="image-20220223105440918" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220223105520370.png" alt="image-20220223105520370" style="zoom:50%;" />



### Types of adapters

- object adapters : see above
- class adapters : using multiple inheritance. The adapter subclasses the target and adaptee class

### Adapter vs decorator

- both use composition to wrap an object
- but the decorator adds **new behavior**
- while the adapter **implements an interface**
- adapter can also wrap multiple objects to implement an interface



## Facade

- A facade not only simplifies an interface, it decouples a client from a subsystem of components.
- Facades and adapters may wrap multiple classes, but a facade’s intent is to simplify, while an adapter’s is to convert the interface to something different.
- Facades don’t “encapsulate” the subsystem classes; they merely provide a simplified interface to their functionality. The subsystem classes still remain available for direct use by clients that need to use more specific interface
- Each subsystem can have multiple facade
- The intent of the Adapter Pattern is to alter an interface so that it matches one a client is expecting. The intent of the Facade Pattern is to provide a simplified interface to a subsystem.

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220223111731344.png" alt="image-20220223111731344" style="zoom:50%;" />

- An adapter wraps an object to change its interface, a decorator wraps an object to add new behaviors and responsibilities, and a facade “wraps” a set of objects to simplify.



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220223114852994.png" alt="image-20220223114852994" style="zoom:50%;" />

> also called Law of Demeter

when you are designing a system, for any object, be careful of the number of classes it interacts with and also how it comes to interact with those classes.



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220223115111940.png" alt="image-20220223115111940" style="zoom: 33%;" />





# 8. The Template Method Pattern

> The Template Method defines the steps of an algorithm and allows subclasses to provide the implementation for one or more steps.

- Allows a base class to control the algorithm, letting subclasses modify parts of it
- class concentrates knowledge about the algorithm and relies on subclasses to provide complete implementations

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220224130432327.png" alt="image-20220224130432327" style="zoom:50%;" />

- template  = method that define an algorithm as a set of steps
- One or more of these steps is defined to be abstract and implemented by a subclass
- important technique for code reuse

### Hooks

- A hook is a method that is declared in the abstract class, but only given an empty or default implementation. This gives subclasses the ability to “hook into” the algorithm at various points, if they wish; a subclass is also free to ignore the hook
- A hook is a method the concrete class can implement but doesn’t have to (no body or simple body)
- abstract method : subclass must implement. Hook not
- a hook can also be used to notify the concrete class of a change



- Number of abstract methods : trade off between number of methods to implement and granularity / flexibility

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220224131209482.png" alt="image-20220224131209482" style="zoom:50%;" />

- The Hollywood Principle gives us a way to prevent “dependency rot.” Dependency rot happens when you have high-level components depending on low-level components etc ..
- With the Hollywood Principle, we allow low-level components to hook themselves into a system, but the high-level components determine when they are needed, and how

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220224131354907.png" alt="image-20220224131354907" style="zoom: 33%;" />

- Subclass never call parent explicitly
- Parent control part of their API that can be hooked / implemented
- Related patterns Hollywood principle : factory method (specialization of template method with one method, can also be part of a template method), observer
- Strategy resemble template method but works at the object level using composition / runtime. Template method works at the class level using inheritance. It is static
  - Also strategy encapsulate the whole algorithm whereas template method concrete class implement only parts of it. And don’t touch the structure
  - Template method better when few changes are expected. If implementations are quite different, strategy will be fine because we don’t need as much reuse.
- Hollywood principle vs Dependency injection
  - They both limit the dependencies between classes, and decoupling
  - the Dependency Inversion Principle makes a much stronger and general statement about how to avoid dependencies in design

Real world examples :

- subclassing list
- creating frameworks



# 9. The Iterator and Composite Patterns



## Iterator

- if implemented, allows to traverse different types of collections / aggregates with the same interface 

![image-20220331120424901](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331120424901.png)

- we have no method corresponding to first(). That’s because in Java we tend to just get a new iterator whenever we need to start the traversal ove

- Just add a createIterator method to the collection returning an instance of the Iterator interface
- ![image-20220331120740244](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331120740244.png)

- Some collections class already implement a .iterator() method (e.g. Java ArrayList)
- NB once the iterator pattern is implemented we can create a common interface for the container class (Like HasIteratorInterface, or Menu in the book example having :  `Iterator<MenuItem> pancakeIterator = pancakeHouseMenu.createIterator();`)
- Here Menu and MenuItem are interfaces

![image-20220331122615508](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331122615508.png)

- It also places the task of traversal on the iterator object, not on the aggregate, which simplifies the aggregate interface and implementation, and places the responsibility where it should be

![image-20220331122745737](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331122745737.png)

- Iterator ressembles factory method in that it delegates to a subclass (ConcreteAggregate) the creation of the iterator concreate class

### The single responsibility principle

- Should we have the iterator code in the collection class ? No, they are 2 different responsibilities and areas of change

![image-20220331123040027](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331123040027.png)

![image-20220331123155850](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220331123155850.png)



### Iterator types

- Internal iterator : just pass an operation to the iterator. The iterator handles the iterating code by itself (it's not the client that does it). (simple but less flexible. NB : array_walk ..?)
- In general, you should make no assumptions about ordering unless the Collection documentation indicates otherwise

### Iterable

- If a class implements Iterable, we know that the class implements an iterator() method
- e.g. in python : “Under the hood”, an iterable is any Python object with an `__iter__()` method or with a `__getitem__()` method that implements `Sequence` semantics
- Iterable can have additional methods to loop the collection (java foreach) and be compatible with looping constructs (java enhanced for loop)







## Composite

![image-20220401142102147](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401142102147.png)

- treat “individual objects and compositions uniformly.”
- The Composite Pattern allows us to build structures of objects in the form of trees that contain both compositions of objects and individual objects as nodes
- Using a composite structure, we can apply the same operations over both composites and individual objects. In other words, in most cases we can **ignore** the differences between compositions of objects and individual objects.

![image-20220401144715086](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401144715086.png)

- because leaves and nodes have different roles we can’t always define a default implementation for each method that makes sense. Sometimes the best you can do is throw a runtime exception.

### Tradeoff

- The composite somehow break single responsibility by handling both iteration over child nodes and actions on the nodes
- It's also not type safe because some actions cannot be implemented in node or leaves
- It's a design tradeoff, because we favor **transparency**
- We can take the tradeoff the other way and favor type safety by creating 2 interfaces. That's the type safe composite pattern and it forces the client to check the type of the object (with instanceof). Stronger but not as elegant

A few things more :

- Leaves can have a reference to their parents for deletion.
- We can make leaves ordered by implementing logic when creating or deleting them
- Caching : cache the results of an operation done often 

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

