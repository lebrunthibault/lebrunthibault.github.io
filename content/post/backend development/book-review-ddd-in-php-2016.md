---
title: "Carlos Buenosvinos - Domain-Driven Design in PHP-Leanpub (2016)"
draft: true

---

[book here](https://drive.google.com/file/d/16pQ8ET7pLOzadr5ayF9PPUidOgCEJQVl/view?usp=sharing)

# Preface

> initially started as "**Hexagonal** architecture with PHP"

- Bounded Contexts can be implemented in different ways and using different approaches. However, two styles are getting more popular, **Hexagonal Architecture** and **CQRS + ES**

- Integrating bounded contexts : REST is our suggestion for synchronous communication and messaging with RabbitMQ for asynchronous



# 1. Getting Started with DDD

> See DDD quickly for concepts
>
> DDD provides a framework for **strategic** and **tactical** design



### Ubiquitous language

- Along with Bounded Contexts the Ubiquitous Language is one of the main strengths of DDD
- For now, consider a Bounded Context is a conceptual boundary around a system. The Ubiquitous Language inside a boundary has a specific contextual meaning. Concepts out of this context can have a different meaning
- Label with names for actions physical and conceptual domain concepts. 
- Create a glossary of terms and definitions. 
- Capture important software concepts with some kind of documentation. 
- Share and evolve the knowledge collected with the rest of the team



### Should I start considering Domain-Driven Design as an option?

- not for data centric + CRUD application
- If your application has less than 30 use-cases, it might be simpler to use a framework like Symfony
  or Laravel to handle your business logic
- If you know your application is gonna grow and is likely to change often, DDD will definitively help in managing the complexity and refactoring your model over time.

### Business value

> Thinking in technical
> problems is not bad, the only problem is that sometimes thinking less technically is better

- Useful and meaningful model of its domain 
- Domain experts contribute to software design 
- Better user experience 
- Clear boundaries 
- Better architecture organization 
- Iterative and continuous modeling on agile fashion 
- Better tools, strategic and tactical



# 2. Architectural Styles



## Layered architecture

- An essential rule of the Layered architecture is that each layer may be tightly coupled with the layers beneath it

<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/layered_architecture.png?raw=true" style="zoom:50%;" />

## Model view controller MVC

>  Model-View-Controller is an architectural pattern and paradigm that divides the application into three main layers: • The Model: Captures and centralizes all the domain model behaviour. This layer manages all the data, logic and business rules independently of the data representation. 

- It can be said that the Model layer is the heart and soul of every MVC application. 
- The Controller: Orchestrates interactions between the other layers. Triggers actions on the model in order to update its state and refreshes the representations associated to the model. Additionally, the Controller can also send messages to the View layer in order to change the specific Model representation. 
- The View: A layer whose main purpose is to expose the differing representations of the Model layer and to give a way to trigger changes on the Model’s state.

#### The Model

>  the Application services are the ones that make things happen and they are the direct clients of a Domain Model. No other type of object should be able to directly talk to the internal layers of the Model layer.
>
> NB : Any service is an application service ..?

#### The View

- Generally speaking, the View layer receives an object, often a Data Transfer Object (DTO)
- Why create a DTO instead of giving an instance of the Model to the View layer? The main reason and the short answer is, again, **Separation of Concerns**. 
- Letting the view inspect and use a Model instance leads to tight coupling between the View layer and the Model layer
- Most of the time, when the Model triggers a state change, it also notifies the related Views so that the UI can get refreshed. In web, usually mean use a js framework.

#### The Controller

- The Controller layer is responsible for organizing and orchestrating the View and the Mode

- It receives messages from the View layer and triggers Model behaviour in order to perform the desired action. Furthermore, it sends messages to the View in order to display Model representations

- Both operations are performed thanks to the Application Layer, responsible for orchestrating, organizing and encapsulating domain behaviour

- In terms of a web application in PHP, the controller = "speak http" (request -> response)

  

## Inverting Dependencies. Hexagonal Architecture

- Following the essential rule of Layered Architecture, there is a risk to end up implementing domain interfaces that need to make use of infrastructural concerns within the domain model layer
- e.g. a repository is part of the model in MVC but should not necessarily be in the domain layer because of SOC



#### The Dependency Inversion Principle (DIP)

> See [this](https://wkrzywiec.medium.com/ports-adapters-architecture-on-example-19cab9e93be7) for Ports and Adapters

- As the Domain Model layer depends on concrete infrastructure implementations, the Dependency Inversion Principle⁷ could be applied by relocating the Infrastructure layer on top of the other three layers
- **High level modules should not depend upon low level modules. Both should depend upon abstractions**
- Hexagonal Architecture (also known as **Ports and Adapters**) : represents the application as an hexagon where each side represents a Port with one or more Adapters
- A Port is a connector with a pluggable Adapter which transforms an **outside** input to something the **inside** application can understand 
- brings up the concept of symmetry
- no longer make sense to talk about a “top” layer nor a “bottom” layer. Instead, Hexagonal Architecture talks mainly in terms of the ‘outside’ and the ‘inside’.
- ***the core logic is at the center***. A realistic number of ports is about 2 to 4, not necessarily 6 (hexa) which has no special meaning

<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/ports_and_adapters.png?raw=true" style="zoom:50%;" />

Port = interface

adapter = implementation (The Adapter is in charge of defining the way in which the blog posts will be retrieved using a specific technology)

DIC = inject adapter from port

-  **Port** it defines all the interactions that a core will have with anything outside. These ports are like contracts (or APIs) and can be divided into two groups **incoming** (primary) and **outgoing** (secondary). 
- The adapters that **tell** our application to do something are called **Primary or Driving Adapters** while the ones that are **told** by our application to do something are called **Secondary or Driven Adapters**.
- **the Ports (Interfaces) belong inside the business logic**, while the adapters belong outside
- First one are responsible of how you can interact with business core (what commands you can use on it) and latter are used by the core to talk to the outside world
- **ports are only definitions of \*what\* we would like to do. They are not saying of \*how\* to achieve them**
- This problem is taken by an **adapter**. These are implementation of the ports
- We can define multiple adapters for a single port, because the business logic should not care how you get/save data from/to database

- From now on, hexagonal architecture will be the foundational architecture used to build and explain CQRS and Event Sourcing



See also  [this article grouping hexagonal architecture and DDD](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)



<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/explicit_architecture.png?raw=true"  />



## Command Query Responsibility Segregation

-  If the problem is having multiple and disparate views, we can exclude them from the Domain Model and start treating them as a purely infrastructural concern
- This option is based on a design principle, named **Command Query Separation CQS**, defined by Bertrand Meyer which gave birth to a new architectural pattern named **Command Query Responsibility Segregatio**n defined by Greg Young

### CQS

- Asking a question should not change its answer
- This design principle states that every method should be either a Command, that performs an action, or a Query, that returns data to the caller, but not both

CQRS seeks an even more aggressive separation of concerns splitting the Model in two:

- The **Write Model**: Also known as the **Command Model**, it performs the writes and takes responsibility for the true domain behavior. It alters entites state by using domain events
- The **Read Model**: It takes responsibility of the reads within the application and treats them as something that should be out of the **Domain Model**

##### Eventual Consistency

- This strict separation triggers another problem, **Eventual Consistency**
- The consistency of the read model now is subject to the commands performed by the write model
-  every time the write model performs a command it will pull up a process that will be responsible to update the read model according to the last updates on the write model.
- e.g. Cache systems are eventually consistent
- This kind of processes, speaking in CQRS terminology, are called **Write Model Projections** or just **Projections** : We project the write model onto the read model
- sync or async
- it can be done thanks to another useful tactical design pattern that will be explained in detail later on in the book, **Domain Events**
- The basis of the write model projections is to gather all the published domain events and update the read model with all the information coming from the events

#### The Write Model

- repo simplified to save() and byId(), freed from all read concerns except one, the byId which is responsible for loading the aggregate by its’ ID so that we can operate on it
- And once this is done, all the query methods are also stripped down from the Post model, leaving it only with command methods (remove all getters !)
- Instead, domain events will be published in order to be able to trigger write model projections by subscribing to them
- NB **Domain events** should totally replace all data access and manipulation
- All actions that trigger a state change are implemented via domain events
- For each domain event published there is an apply method responsible to reflect the state change. NB : that is defined in the aggregateRoot so as to act on private fields.

#### The Read Model

- The read model, also known as the Query Model, is a pure denormalized (NB : normalize = object => array and vice versa) data model lifted from domain concerns
- These database tables / UI views will be updated using write model projections triggered from the domain events published by the write side.
- An important feature of this architectural style is that the read model should be completely disposable since the true state of the application is handled by the write model.
- NB : single source of truth : write model domain events
- read model doens't need to be relationnal (can be elasticsearch for example)
- However, the write model might benefit from the use of an object-relational mapper as they allow you to organize and structure the read model

#### Synchronizing the Write Model with the Read Model

- tricky part
- one-to-one relationship between domain events and projections



## Event Sourcing

- giving you a high-level degree of detail of what is going on within your domain
- if repositories become hard to maintain then it is time to consider the use of CQRS, to split read and write concerns
- Domain Events are one of the key tactical patterns because of their significance within the domain, as they describe past occurrences
- An ever growing number of events is a smell of the business overlooking insight in the Domain.
- By using CQRS we gained a highly sophisticated history of all the relevant occurrences at a level that the whole state of the domain model can be expressed just by reproducing domain events
- store them in an **eventstore**
- **The fundamental idea behind Event Sourcing is to express the state of Aggregates as a linear sequence of events**
- instead of persisting each entity, with event sourcing we can persist **only** events, resulting in .. **a single database table !**

<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/event_sourcing_apply_history.png?raw=true" style="zoom:50%;" />





# 3. Value Objects

- equality is not based on identity
- slow memory footprint : new instance creation is favoured over reference reuse
- they follow value semantics rather than reference semantics
- value objects should be entirely immutable
- provides **encapsulation**
- *[Self-encapsulation](https://martinfowler.com/bliki/SelfEncapsulation.html)* 
  - indicates that all *internal* access to a data field should also go through accessor methods as well
  - need to create private getters
  - support the [UniformAccessPrinciple](https://martinfowler.com/bliki/UniformAccessPrinciple.html). 
  - Usually **not worth the effort** with small classes having dummies setters and getters
  - Good when there is logic in setters or an inheritance structure
  - From Martin Fowler: use **direct access to fields** and refactor to **self encapsulate field** later.
  - But often better to **extract a new class**.



## Characteristics

- you should always favour Value Objects over Entities
- immutable and **Side-Effect-Free** behaviour
- immutable so Value Objects are always in a valid state
- Empty constructors with multiple setters and getters move the creation responsibility to the client, resulting in the Anemic Domain Model⁶, which is considered an anti-pattern
- it is not recommended to hold references to entities in your Value Objects. Entities are mutable, and as such this could lead to undesirable side-effects occurring in the Value Object
- to emulate Java overloading we can use different factory methods (always use self, static can lead to bugs when the VO is inherited)
- to handle mutability use the following construct

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220128121232232.png" alt="image-20220128121232232" style="zoom:67%;" />

- VO provide **Single responsibility** and **DRY**
- NB : We could use Email VO in Basile
- in PHP, it is common place to compare two Value Objects using  ==
- a solution is to implement a conventional equals method in each VO
- in PHP string are immutable: strtolower returns a new string
- Value Objects are not persisted on their own, they are typically persisted within an Aggregate
- [NB](https://dzone.com/articles/practical-php-patterns/practical-php-patterns-3#:~:text=The%20Embedded%20Value%20is%20an,a%20direct%20reference%20to%20it.) : ValueObjects can be integrated in the FlyWeight pattern.



#### NB : Object relational Stuctural patterns (persistence)

- **Active record** : the entity has methods to save, remove .. on itself and inherits a base class. **Eloquent**
- **Data mapper pattern**: the entity persistence is handled by the ORM. **Symfony** 
- **[Dependent mapping pattern](https://www.sourcecodeexamples.net/2018/05/dependent-mapping-pattern.html)** : Has one class perform the database mapping for a child class (e.g. Person -> address). When a dependent object doesn’t need to be accessed on its own.



### **[Embedded Value pattern](https://dzone.com/articles/practical-php-patterns/practical-php-patterns-3#:~:text=The%20Embedded%20Value%20is%20an,a%20direct%20reference%20to%20it.)** 

- particular case of the [Dependent Mapping](http://css.dzone.com/books/practical-php-patterns/practical-php-patterns-2) one, where it is realized with a single table. 
- It is a further departure from the naive mapping one table, one class and one object, one row And the [Active Record](http://css.dzone.com/books/practical-php-patterns/practical-php-patterns-active) pattern
- add complexity to the object-relational mapper but usually interesting in the long run because the complexity is mostly handled by the ORM.
- employed in conjunction with [Value Objects](http://www.c2.com/cgi/wiki?ValueObject), and it is very useful when having a 1:1 relationship from an Entity towards a Value Object
- With an Embedded Value mapping, the VO will reside in the same row of the User that owns it, as an additional column
- Depending on the case, a VO will be fine when we **won't be adding fields** else it should be an entity
- If we want to access the data **independently** then it's an entity

### Why Doctrine ?

>  We recommend using Doctrine in most cases when dealing with Entities and business logic

- Embedded value with [embedabbles](https://www.doctrine-project.org/projects/doctrine-orm/en/2.11/tutorials/embeddables.html)
- Also possible to use surrogate fields mapped directly (doctrine < 2.4)
  - In this case it's better to use Abstract Factory to generate Product or DoctrineProduct (subclass)

### [Serialize LOB (single large object) Pattern](https://www.martinfowler.com/eaaCatalog/serializedLOB.html)

- Object models often contain complicated graphs of small objects
- Using a relations in db works but is awkward and slow (multiple joins)
- Another form of persistence is serialization, where a whole graph of objects is written out as a single large object (LOB) in a table
- this Serialized LOB then becomes a form of memento [Gang of Four]
- The persistence footprint requirements get reduced to a single column
- **We can't query fields with this pattern**
- Serialization can be improved with [JMS Serializer](http://jmsyst.com/libs/serializer)
- [Doctrine Custom Types](https://www.doctrine-project.org/projects/doctrine-orm/en/2.11/cookbook/custom-mapping-types.html) 

### Persisting VO collections

- Using embeddable value when we know the collection size

#### Collection Serialized into a Single Column

-  With Doctrine you can use an Object or Custom Type
- Check the row size

#### Collection backed by a Join Table

- If we need querying capabilities on VO
- Can be one to many or many to many
- Doctrine requires that all database entities to have a unique identity. Because we want to persist Money Value Objects we need to then add an artificial identity so Doctrine can handle its persistence
- Solution 1: put the surrogate identity in the Money class 
  - Problem The identity is infrastructure and not domain
- Solution 2 : put surrogate field in a subclass and use factories.
  - The factory should be passed in application service and any other domain objects

#### PostgreSQL and JSONB

- Now postgres allows querying directly json with [JSONB](https://www.postgresql.org/docs/9.4/functions-json.html)

### Security

- Manipulating VO is safer as you manipulate valid objects
-  If you centralize the [guards](https://en.wikipedia.org/wiki/Guard_(computer_science)) in the constructor and pass into your model a IATA Value Object avoiding SQL Injections or similar attacks get easier
- [Dan Bergh Johnsson : Secure by design](http://dearjunior.blogspot.com/search/label/domain%20driven%20security)



# 4. Entities

Most of the time the identity of an entity is represented as a primitive type: usually a string or an integer. But using a value object to represent it has more advantages:

- Value Objects are immutable, so they cannot be modified
- Value Objects are complex types that can have custom behaviours that otherwise with primitive types cannot have
- makes equality more explicit

## Identity operation

There are usually 4 ways to define the identity of an entity

- A client provides the identity
- the application itself provides an identity
- the persistence mechanism provides the identity
  - Usual and simple but **we won’t have the identity of the entity until we persist it**
  - will couple the identity operation with the underlying persistence store
- another bounded context provides an identity

### Persistence Mechanism Generates Identity 

#### Surrogate identity

The simplest way to handle that situation is by using a [Layer SuperType](https://martinfowler.com/eaaCatalog/layerSupertype.html) where we put the identity field created for the persistence store.

![image-20220131150038305](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220131150038305.png)

#### Active Record vs Data Mapper for Rich Domain Models

An Active Record implementation is fine mostly for CRUD applications, but it’s not the ideal solution for rich domain models

- The Active Record pattern assumes a one-to-one relation between an entity and a database table. So it couples the design of the database to the design of the object system
-  Advanced things like collections or inheritance are tricky to implement
- Most of the implementations force the use, through inheritance, of some sort of constructions to impose several conventions. This can lead to persistence leakage into the domain model by coupling the domain model with the ORM
- Currently **the best ORM for PHP out there is Doctrine**. It’s an implementation of the Data Mapper pattern⁶. Data Mapper decouples the persistence concerns from the domain concerns, leading to persistence-free entities

### Client Provides Identity

 Probably this is the ideal case, because the identity can be modelled quite easy

- Example : an ISBN

### Application Generates Identity

- If the client cannot provide the identity generally the preferred way to handle the identity operation is to let the application generate the identities, usually through a UUID

- Several libraries provide this, e.g. https://github.com/ramsey/uuid

- The preferred place to put the creation of the identity would be inside a Repository

  ![image-20220131151058018](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220131151058018.png)

### Other Bounded Context Generates Identity

- Probably this would be the most complex identity generation strategy, because it enforces to have a local entity to be dependent not only on local bounded context events, but in external bounded contexts events
- When synchronization is needed between the entities of the Bounded Contexts, usually can be achieved with an Event Driven architecture on each of the Bounded Context that need to be notified when the original entity is changed

## Persisting Entities

- Using doctrine
- Using annotation
  - Simple and elegant but
  - domain concerns are mixed with infrastructure concerns
  - s entity is tightly coupled to the mapping information specified by the annotations in the source code
- Using config files :
  - The best way

## Testing entities

- It’s relatively easy to test entities
-  the test should be the invariants that the entity protects

## Validation

- Validation is a highly important process in our domain model
- Should test all attributes are valid and also whole object is valid. It is not an equivalence

###  Attribute Validation

- Some people understand validation as the process whereby a service validates the state of a given object. In this case, the validation conforms to a [design-by-contract](https://en.wikipedia.org/wiki/Design_by_contract) approach - consisting of preconditions, post-conditions and invariants.
-  Here we will be using guards as an easy way of validating the pre-conditions (username string validation)
- Some developers may see this kind of validation as defensive programming
-  but we control only the correctness of our domain state

### Entire Object Validation

- It can be tempting to add this kind of validation to the object itself, but generally this is an antipattern
-  Higher-level validation is likely to change at different times to the object itself. Also it is good practice to separate these responsibilities
- The validation informs the client about any errors that have been found, or collect the results to be reviewed later. Sometimes we do not want to stop the execution at the first sign of trouble
- An abstract and reusable Validator could be something like

![image-20220131151954274](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220131151954274.png)



### Validating Object Compositions

-  Validating object compositions can be complicated, because of this, the preferred way of achieving this is through a Domain Service
- We can use Domain Events to notify other parts of the system that a particular element has been validated



# 5. Services

When there are operations that need to be represented, we can consider them to be services. There are typically three different types of service which you will encounter, these are :

![image-20220131154707521](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220131154707521.png)



## Application services

- Application services are the middleware between the outside world and the domain logic. The purpose of such a mechanism is to transform commands from the outside world into meaningful domain instructions
- As following the same contract for every service is convenient (will see that later), the communication between the delivery mechanism and the domain is carried by data structures called DTOs (Data Transfer Objects) (NB : UserSigninRequest $request)

### Transactions

- In Domain-Driven Design, transactions are handled at the Application Service level. You are not going to find any beginTransaction or similar anywhere in your Domain code
- All the operations performed during the execution of the Application Service are going to be run atomically against your database

