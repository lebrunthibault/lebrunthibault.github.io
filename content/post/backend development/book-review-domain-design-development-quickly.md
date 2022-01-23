---
title: "Domain Driven Development Quickly"
draft: true
---

Book [here](https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf)

# Intro

>  Software needs to incorporate the core concepts and elements of the domain, and to precisely realize the relationships between them. Software has to model the domain
>
>  a domain model is not a particular diagram; it is the idea that the diagram is intended to convey
>
>  *we need to communicate the model*

### Code design

- code design is working on the details vs software design working on big picture
- Here code design patterns come handy, and they should be applied when necessary

### Existing Software design approaches

- Classical software design, **waterfall** : The business experts put up a set of requirements which are communicated to the business analysts. The analysts create a model based on those requirements, and pass the results to the developers
- **Extreme Programming (XP)**: 
  - goes against waterfall. 
  - Try solving difficulties of trying to come up with all the requirements upfront, particularly in light of requirements change. 
  - Uses a lot refactoring instead of upfront design.
  - Good but needs developers with solid design principles or the code will become hard to understand after several refactorings
  - Can lead to the fear of a good design by opposition
- Domain Drive Design
  - a bit of both
  - combines design and development practice, and shows how design and development can work together to create a better solution

## Building domain knowledge

- You need to learn as much as possible about the domain from the experts. And by putting the right questions, and processing the information in the right way, you and the experts will start to sketch a view of the domain, a domain model
- The building of the domain allows to put the maximum domain knowledge in the model, **very** important.
- The software specialists want to extract knowledge from the domain experts
- The analytical mind of the software designer helps unearth some of the key concepts of the model, because domain experts see things a way that is not always applicable to software
- the model is the place where those two areas of expertise meet (domain expertise and software expertise)



# The ubiquitous language, the need for a common language

- A project faces serious problems when team members don’t share a common language for discussing the domain. Domain experts use their jargon while technical team members have their own language tuned for discussing the domain in terms of design
- the most incisive expressions of the domain often emerge in a transient form that is never captured in the code or even in writing

> A core principle of domain-driven design is to use a language based on the model

### Impose the domain language

- Use the model as the backbone of a language
- Request that the team use the language consistently in all communications, and also in the code
- The Ubiquitous Language connects all the parts of the design, and creates the premise for the design team to function well
- The Ubiquitous Language connects all the parts of the design, and creates the premise for the design team to function well
- Iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model
- he model and the language are strongly interconnected with one another. A change in the language should become a change to the model

## Creating the Ubiquitous Language 

- By having domain interviews with the domain experts
- We have seen how the language is shared by the entire team, and also how it helps building knowledge and create the model.

### Expressing the language

- UML : great for a few classes but gets complicated when we add too much classes / knowledge
- UML cannot convey two important aspects of a model: the meaning of the concepts it represents and what the objects are supposed to do
- One advisable way of communicating the model is to make some small diagrams each containing a subset of the model
- Then we can add text to the diagram. The text will explain behavior and constraints which the diagram cannot
- Those documents can be even hand-drawn, because that transmits the feeling that they are temporary, and might be changed in the near future
- Avoid long documents that get outdated faster
- Sometimes code can be used (or test code) but the code even working doesn't always express the right thing.

# Model driven design

> Starting from a model not easily adaptable, good developers might pull together a product which works, but will it stand the trials of time? Will it be easily extendable? Will it be easily maintainable?

- It is important to choose a model which can be easily and accurately put into code
- *analysis model* : result of business domain analysis, resulting in a model which has no consideration for the software used for implementation. Such a model is used to understand the domain. After translation in code the code will start to move away from the model.
- A better approach is to closely relate domain modeling and design
- Those who write the code should know the model very well, and should feel responsible for its integrity
- Every person working on the project should contribute to all parts (dev to the model, business analysts to the code)
- OOP is good for model driven design because classes and objects can contain behavior and relationships



### Presentation of the most important model driven design patterns

> Map of the different patterns

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/model_driven_design.PNG?raw=true)



## Layered architecture



![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/layered_architecture.PNG?raw=true)

> When we create a software application, a large part of the application is not directly related to the domain, but it is part of the infrastructure or serves the software itself.

- Partition a complex program into LAYERS. Develop a design within each LAYER that is cohesive and that depends only on the layers below
- Concentrate all the code related to the domain model in one layer and isolate it from the user interface, application, and infrastructure code

A common architectural solution for domain-driven designs contain four conceptual layers:

- **User interface** (presentation layer) : Responsible for presenting information to the user and interpreting user commands
- **Application Layer** : This is a thin layer which coordinates the application activity. It does not contain business logic. It does not hold the state of the business objects, but it can hold the state of an application task progress
- **Domain layer **: This layer contains information about the domain. This is the heart of the business software. The state of business objects is held here. Persistence of the business objects and possibly their state is delegated to the infrastructure layer
- **Infrastructure Layer** : This layer acts as a supporting library for all the other layers. It provides communication between layers, implements persistence for business objects, contains supporting libraries for the user interface layer, etc.

> UI talks to application with talks to the domain and infrastructure (e.g. fetches domain object from infra, calls domain object methods and use infra to persist the objects)



## Entities

> There is a category of objects which seem to have an identity, which remains the same throughout the states of the software.

- implementing entities in software means creating identity
- When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model
- Be alert to requirements that call for matching objects by attributes. Define an operation that is guaranteed to produce a unique result for each object
- The model must define what it means to be the same thing
- It is also important to determine if an object needs to be an entity or not

## Value objects

##### Difference with DTO

> - A value object is a simple object whose equality isn't based on identity. 
> - A [data transfer object](https://martinfowler.com/eaaCatalog/dataTransferObject.html) is an object used to transfer data between software application subsystems, usually between business layers and UI. 
> - It is focused just on plain data, so it doesn't have any behaviour. 
> - Used to batch up multiple remote procedure calls in one call. 
> - Another advantage is to encapsulate the serialization mechanism

- It takes a lot of careful thinking to decide what makes an identity
- There are also performance implications in making all objects entities
- There are cases when we need to contain some attributes of a domain element. We are not interested in which object it is, but what attributes it has. 
- **An object that is used to describe certain aspects of a domain, and which does not have identity, is named Value Object**
- It is highly recommended that value objects be immutable (implement only getters)
- Being immutable, and having no identity, Value Objects can be shared
- Value Objects can contain other Value Objects, and they can even contain references to Entities

## Services

> Services act as interfaces which provide operations

**3 Caracteristics of a service**

- The operation performed by the Service refers to a domain concept which does not naturally belong to an Entity or Value Object. 
- The operation performed refers to other objects in the domain
- The operation is stateless

### Domain segregation

- It is easy to get confused between services which belong to the domain layer, and those belonging to the infrastructure. There are application services, domain services and infrastructure services
- While working on the model and during the design phase, we need to make sure that the domain level remains isolated from the other levels
- Deciding the layer a Service belongs to is difficul (application or domain ?)

## Modules

- for a large application it is necessary to organize the model into modules
- It is widely accepted that software code should have a high level of cohesion and a low level of coupling
- group highly related classes into modules to provide maximum cohesion possible
- **communicational cohesion**: when the module operates on the same data
- **functional cohesion**: all parts of the module work together to perform a well-defined task. Considered the best type of cohesion 
- Using modules in design is a way to increase cohesion, maintainability and decrease coupling
- **Modules should have well defined interfaces which are accessed by other modules**
- Choose Modules that tell the story of the system and contain a cohesive set of concepts
- Refine the model until it partitions according to high-level domain concepts and the corresponding code is decoupled as well
- **Give the Modules names that become part of the Ubiquitous Language**



## Aggregates

> Factories and Repositories are two design patterns which help us deal with object creation and storage
>
> Aggregate is a domain pattern used to define object ownership and boundaries

- Most of the time it pays of to eliminate or simplify relations from the model
- One to many is more complicated than one to one and many to many is the most complicated to deal with especially when it's bidirectional
- Firstly, associations which are not essential for the model should be removed
- Secondly, multiplicity can be reduced by adding a constraint : if many objects satisfy a relationship, it is possible that only one will do it if the right constraint is imposed on the relationship (NB : meaning many to one to one to one ..?)
- many times bidirectional associations can be transformed in unidirectional ones : (e.g. an engine doesn't need to have a car)
- database transactions are used to enforce data integrity
- It is also necessary to be able to enforce the invariants (rules which have to be maintained whenever data changes. meaning stuff that we cannot check at the database level ?)

### Solution : aggregates

- An Aggregate is a group of associated objects which are considered as one unit with regard to data changes
- The Aggregate is demarcated by a boundary which separates the objects inside from those outside
- Each Aggregate has one root. The root is an Entity, and it is the only object accessible from outside
- NB in basile : 
  - an AbstractApplication Aggreagate with absApp as root and ApplicationFormValue, Candidate, Status, Alerts ..?
  - BonusAmount Aggreagte (with BonusAmountFilter) 
  - Company: CompanyImage, CompanyLog
  - Offer : OfferAdress, OfferPreference
- The root object will enforce the invariants
- It is possible for the root to pass transient references of internal objects to external ones, with the condition that the external objects do not hold the reference after the operation is finished
- One simple way to do that is to pass copies of the Value Objects to external objects. Aggreagate integrity will be protected
- If objects of an Aggregate are stored in a database, only the root should be obtainable through queries. The other objects should be obtained through traversal associations
- Objects inside an Aggregate should be allowed to hold references to roots of other Aggregates
- The root Entity has global identity, and is responsible for maintaining the invariants. Internal Entities have local identity
- Cluster the Entities and Value Objects into Aggregates and define boundaries around each

## Factories

- Entities and Aggregates can often be large and complex
- Factories are used to encapsulate the knowledge necessary for object creation, and they are especially useful to create Aggregates
- When the root is created, it is necessary that all objects subject to invariants are created too (VO should have there valid state and an exception is thrown if anything goes astray)
- shift the responsibility for creating instances of complex objects and Aggregates to a separate object, which may itself have no responsibility in the domain model but is still part of the domain design

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/ddd_factory.PNG?raw=true)

- It is necessary that when such a component is created to automatically belong to a container. The client calls the createComponent(Type t) method of the container
- The concrete class of the component is determined based on its type
- **When creating a Factory, we are forced to violate an object’s encapsulation**
- Factories are tightly related to the objects they are created. That can be a weakness, but it can also be a strength

Don't use factory method when

- The construction is not complicated. 
- The creation of an object does not involve the creation of others, and all the attributes needed are passed via the constructor. 
- The client is interested in the implementation, perhaps wants to choose the Strategy used. 
- The class is the type. There is no hierarchy involved, so no need to choose between a list of concrete implementations.



## Repositories

- Using V0 and Aggregates can increase coupling between objects
- purpose of which is to encapsulate all the logic needed to obtain object references
- the Repository acts as a storage place for globally accessible objects
- The overall effect is that the domain model is decoupled from the need of storing objects or their references, and accessing the underlying persistence infrastructure
- create an object that can provide the illusion of an in-memory collection of all objects of that type
- Provide repositories only for Aggregate roots that actually need direct access
- the repository interface will be pure domain model
- Factory and Repository. They are both patterns of the model-driven design



# Refactoring towards deeper insight

- tools to make refactoring easier
- Technical refactoring, the one based on patterns, can be organized and structured. Refactoring toward deeper insight cannot be done in the same way
- A good model is the result of deep thinking, insight, experience, and flair
- Traditionally, refactoring is described in terms of code transformations with technical motivations. Refactoring can also be motivated by an insight into the domain and a corresponding refinement of the model or its expression in code

## Bring key concepts into the light

- There are times when lots of small changes add very little value to the design, and there are times when few changes make a lot of difference. It’s a **Breakthrough**

### Breakthrough

- A Breakthrough often involves a change in thinking, in the way we see the model.
- may imply a large amount of refactoring
- To reach a Breakthrough, we need to make the implicit concepts explicit
- They are **implicit concepts**, used to explain other concepts which are already in the model
- If they are domain concepts, they should be present in the model and the design
- Another obvious way of digging out model concepts is to use domain literature

There are other concepts which are very useful when made explicit

- **Constraint** : isolate the constraints (invariants) in specific methods
- **Process**: use Services.  If there are different ways to carry out the process, then we can encapsulate the algorithm in an object and use a **Strategy**
- **Specification**: 
  - used to test an object to see if it satisfies a certain criteria.
  - useful when a constraint grows too big
  - it should stay in the domain layer

# Preserving Model Integrity 

## Bounded Context 

- Each model has a context. When we deal with a single model, the context is implicit. We do not need to define it
- A model should be small enough to be assigned to one team
- The main idea is to define the scope of a model, to draw up the boundaries of its context, then do the most possible to keep the model unified
- A Bounded Context is not a Module. A Bounded Context provides the logical frame inside of which the model evolves. Modules are used to organize the elements of a model, so Bounded Context encompasses the Module
- There is a price to pay for having multiple models
- We won’t be able to transfer any objects between different models, and we cannot invoke behavior freely as if there was no boundary
- It is much simpler for the e-shop application to send Value Objects containing purchase information to the warehouse using asynchronous messaging

## Continuous Integration 

- When a number of people are working in the same Bounded Context, there is a strong tendency for the model to fragment and lose a valuable level of integration and coherency
- For a single small team, daily merges are recommended
- Another necessary requirement is to perform automated tests
- Continuous Integration applies to a Bounded Context, it is not used to deal with relationships between neighboring Contexts

## Context Map

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/observer.PNG?raw=true)

- An enterprise application has multiple models, and each model has its own Bounded Context
- A Context Map is a document which outlines the different Bounded Contexts and the relationships between them
- Each Bounded Context should have a name which should be part of the Ubiquitous Language and corresponds to a module

## Shared Kernel 

