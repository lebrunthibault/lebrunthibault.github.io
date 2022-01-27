---
title: "Carlos Buenosvinos - Domain-Driven Design in PHP-Leanpub (2016)"
draft: true
---

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

- As the Domain Model layer depends on concrete infrastructure implementations, the Dependency Inversion Principle⁷ could be applied by relocating the Infrastructure layer on top of the other three layers
- **High level modules should not depend upon low level modules. Both should depend upon abstractions**
- Hexagonal Architecture (also known as **Ports and Adapters**) : represents the application as an hexagon where each side represents a Port with one or more Adapters
- A Port is a connector with a pluggable Adapter which transforms an **outside** input to something the **inside** application can understand 
- brings up the concept of symmetry
- no longer make sense to talk about a “top” layer nor a “bottom” layer. Instead, Hexagonal Architecture talks mainly in terms of the ‘outside’ and the ‘inside’.
- *the core logic is at the center*. A realistic number of ports is about 2 to 4, not necessarily 6 (hexa) which has no special meaning

<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/ports-and-adapters.png?raw=true" style="zoom:50%;" />

Port = interface

adapter = implementation (The Adapter is in charge of defining the way in which the blog posts will be retrieved using a specific technology)

DIC = inject adapter from port

- From now on, hexagonal architecture will be the foundational architecture used to build and explain CQRS and Event Sourcing



## Command Query Responsibility Segregation

-  If the problem is having multiple and disparate views, we can exclude them from the Domain Model and start treating them as a purely infrastructural concern
- This option is based on a design principle, named **Command Query Separation CQS**, defined by Bertrand Meyer which gave birth to a new architectural pattern named **Command Query Responsibility Segregatio**n defined by Greg Young

### CQS

- Asking a question should not change its answer
- This design principle states that every method should be either a Command, that performs an action, or a Query, that returns data to the caller, but not both

CQRS seeks an even more aggressive separation of concerns splitting the Model in two:

- The **Write Model**: Also known as the **Command Model**, it performs the writes and takes responsibility for the true domain behavior
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
- Domain Events are one of the key tactical patterns because of their significance within the domain, as they describe past occurrences
- An ever growing number of events is a smell of the business overlooking insight in the Domain.
- By using CQRS we gained a highly sophisticated history of all the relevant occurrences at a level that the whole state of the domain model can be expressed just by reproducing domain events
- store them in an **eventstore**
- **The fundamental idea behind Event Sourcing is to express the state of Aggregates as a linear sequence of events**
- instead of persisting each entity, with event sourcing we can persist **only** events, resulting in .. **a single database table !**

<img src="https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/event_sourcing_apply_history.png?raw=true" style="zoom:50%;" />

