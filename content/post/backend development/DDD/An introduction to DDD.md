# [An introduction to Domain-Driven Design](https://medium.com/inato/an-introduction-to-domain-driven-design-386754392465)



> Domain-Driven Design is an approach to software development based on **making your software deeply reflect a real-world system** or process

- “Domain” is what is commonly referred to as “business logic”
- Good match for complex projects with experienced teams



## The basics of Domain-Driven Design

- Separating the concerns into layers
- Modeling the Domain
- Managing the life-cycle of Domain objects



## I. Isolating the domain: the layered architecture



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220324121846610.png" alt="image-20220324121846610" style="zoom:33%;" />



- **User Interface (or Presentation Layer)** : Responsible for showing information to the user and interpreting the user’s commands
- **Application Layer**: 
  - Defines the jobs (use cases) the software is supposed to do and coordinates the domain objects to work out problems
  - This layer is kept thin. It does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down
  - It does not have state reflecting the business situation, but it can have state that reflects the progress of a task for the user or the program
- **Domain Layer (or Model Layer)** : State that reflects the business situation is controlled and used here, even though the technical details of storing it are delegated to the infrastructure
- **Infrastructure Layer**
  - Provides generic technical capabilities that support the higher layers: message sending for the application, persistence for the domain, drawing widgets for the UI, and so on
  - The infrastructure layer may also support the pattern of interactions between the four layers through an architectural framework



## 🌐 II. Domain modeling
- The basic constraint is that the model must both help the implementation of features and represent real-life knowledge
- Ubiquitous language based on model
- Used in speech, writing, diagrams



### Expressing the model: Building Blocks

There are 3 tools to express the model in Domain-Driven Design, which can be grouped in Modules:

- Value Objects
- Entities
- Services

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220324122810875.png" alt="image-20220324122810875" style="zoom:33%;" />



#### Value Objects

- immutable
- Ensure that the attributes that make up a Value Object form a conceptual whole.



#### Entities

- An Entity is an object defined primarily by its identity, rather than specific attributes.
- The identity of an Entity runs through time, and possibly different representations. Entities are also called “reference objects”



#### Services

- In some cases, the clearest and most pragmatic design includes operations that do not conceptually belong to any object
- Rather than force the issue, we can follow the natural contours of the problem space and include Services explicitly in the model.



#### Modules

- The Modules in the domain layer should emerge as a meaningful part of the model, telling the story of the domain on a larger scale
- low couping / high cohesion
- Give the Modules names that become part of the Ubiquitous Language. Modules and their names should reflect insight into the domain
- favor conceptual clarity over technical convenience




## III. Managing the life cycle of domain objects

> The goal is to prevent the model from getting swamped by the complexity of managing the life cycle. To do this, we separate the management of the life cycle (i.e. persisting objects) from the business logic



### Aggregates

- Aggregates are a cluster of Entities and Value Objects that make sense domain-wise and are retrieved and persisted together
- Aggregates add structure to the model by setting boundaries and providing a clear ownership for the objects they contain
- Choose one Entity to be the root of each Aggregate, and control all access to the objects inside the boundary through the root



### Repositories

- Repository interfaces are **declared in the Domain Layer**, but the repositories themselves are **implemented in the Infrastructure Layer**.
