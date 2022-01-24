See https://www.mirkosertic.de/blog/2013/04/domain-driven-design-example/

> A Domain is a “sphere of knowledge”, for instance the business the company runs. A Domain is also called a “problem space”, so the problem for which we have to design a solution

See also : **[Pourquoi avoir choisi d’utiliser l’architecture CQRS ?](https://medium.com/tiller-systems/pourquoi-avoir-choisi-dutiliser-l-architecture-cqrs-e04c082f8b5f#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImNhMDA2MjBjNWFhN2JlOGNkMDNhNmYzYzY4NDA2ZTQ1ZTkzYjNjYWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NDMwNDUzOTYsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExNDUwMTk3OTM1ODU4NzM4Nzg1MCIsImVtYWlsIjoidGhpYmF1bHRwaWFub0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IlRoaWJhdWx0IExlYnJ1biIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDVqUnFKeGpqbE1Cc3BXMjI0QWhWQ05ISGRWUHJDV3pvdGpHcGI3Zz1zOTYtYyIsImdpdmVuX25hbWUiOiJUaGliYXVsdCIsImZhbWlseV9uYW1lIjoiTGVicnVuIiwiaWF0IjoxNjQzMDQ1Njk2LCJleHAiOjE2NDMwNDkyOTYsImp0aSI6IjllMjExYWNjNzQyNjBjZmU1ZDE2YTI2ZDVmZTY4YTg4NjhmMmMzMGQifQ.lAyHsJLBl8FsFSpA2bsX8T3oz1xvWXGOj1RSO9KfxlcDrBAzPYbiHXP8e5KeOuan42l0u-c_nt-mN_xz1qsu0rqZ8UWSe-mHe4hO_2K2WPXDuvJ3pcSIkaUieiecmRWRV-PRuITTKtz6PYfDfRJC-_Pu9cQCefw4xGCaEya67RANBWvUcaRwkXXNege38wtWoDUOq2rtELop-D-pKZZNCQsBn3crX2BfEbU6vlGF2dXaxkfzy1tAvCMROA4yPnErH7oyDwXwZoOiSdY92euaHQ9FbRU3LZeMEHBpJBD7XSTr3FNrYCZtTpkR3DlxBG9vCw3uy-WzvaoIIdh27UtIGw)**

# [Overview and building blocks](https://www.mirkosertic.de/blog/2012/07/domain-driven-design-overview-and-building-blocks/)

If you want to know more about the principles behind DDD, you can also consult the [GRASP Patterns](http://en.wikipedia.org/wiki/GRASP_(object-oriented_design)) or the [SOLID Patterns](http://en.wikipedia.org/wiki/SOLID_(object-oriented_design))

## Core definitions

- Domain: A sphere of knowledge (ontology), influence, or activity. The subject area to which the user applies a program is the domain of the software.
- Model: A system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain.
- Ubiquitous Language: A language structured around the domain model and used by all team members to connect all the activities of the team with the software.
- Context: The setting in which a word or statement appears that determines its meaning.

## Prerequisites for the successful application of DDD

- Your domain is not trivial
- The project team has experience and interest in Object Oriented Programming/Design
- You have access to domain experts
- You have an iterative process

## Building blocks strategic patterns

- Domain, and Subdomains: As mentioned above, a Domain is a sphere of knowledge. A Domain can be split into Subdomains if it is too large. The Domain is usually known as the problem space.

- Bounded Context: A Bounded context should be aligned with a Domain or a Subdomain. There is one Ubiquitous Language applied within a Bounded Context. A Bounded Context is usually the solution space, where we design our software or business solution.

- Context Map: A Context Map displays the alignment of Domains, Subdomains and their Bounded Contexts. A Context Map also shows dependencies between Bounded Contexts. Such dependencies can be upstream or downstream. Dependencies show where integration patterns should or must be applied

## Layers

- The client sends a command to the Application Service
- The Application Service translates the command to a Domain Model use case invocation
- It is always a good choice to keep transaction control out of the domain model (technical, not business)

### Domain Layer

- The Domain Layer contains the real business logic, but does not contain any infrastructure specific code. 
- The infrastructure specific implementation is provided by the Infrastructure Layer. 
- The Domain Model should be designed as described by the [CQS](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation)(Command-Query-Separation) principle. 
- CQS : There can be query methods which do just return data without affecting state, and there are command methods, which affect state but do not return anything

### Application Layer

- The Application Layer takes commands from the User Interface Layer and translates these commands to use case invocations on the domain layer. 
- The Application Layer also provides transaction control for business operations. 
- The application layer is responsible to translate Aggregate data into the client specific presentation model by a Mediator or Data Transformer pattern

# Context integration

> Integration between multiple domains

**Domain Service**: implements business logic which cannot be implemented by an Entity, Aggregate or ValueObject, because it does not belong there. For instance if the business logic invocation includes operation across multiple Domain Objects or in this case integration with another Bounded Context

### Asynchronous 

- **Messaging**: the reason we use messaging: system decoupling
- The infrastructure layer should call the application layer after a message is received
- it is a good practice to design Events as an idempotent operation (always the same result without side effects)
