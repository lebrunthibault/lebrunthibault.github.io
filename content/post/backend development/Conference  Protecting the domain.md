# Protecting the domain by [Victor Rentea](https://victorrentea.ro/)

talk on [youtube](https://www.youtube.com/watch?v=cK19rE2V9UY)

Most important principles :

- Single Responsibility
- Dependency inversion
- DRY

### Testing tools

- Archunit java
- equivalent in php : https://github.com/qossmic/deptrac
- https://github.com/j6s/phparch
- https://github.com/mihaeu/dephpend
- https://github.com/carlosas/phpat

### Domain vs

- DDD : domain driven development
- encapsulates a specific part of the business code (entities, services ..)
- higher level code than infrastructure

### Infrastructure

- backend code
- lower level code
- implementations

## Protect the domain

- Keep the domain safe from any external influence.  Defend the domain ! Agnostic.

- Defend it from someone else when you call lower level code
- domain logic should not depend on infrastructure
- Keep core logic independent of UI
- independent of DB, no vendor lock ins, no stored procedures, no too complicated sql
- independent of external APIs
- is an orm intrusive ? not necessarily
- logic should be built on objects you have full control on 

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/agnostic_domain.PNG?raw=true)

![](https://github.com/lebrunthibault/lebrunthibault.github.io/blob/master/static/img/domain_vs_infrastructure.PNG?raw=true)

### DTOs are enemies

they are

- bloated
- flat
- different perspective

should be replaced by ids, value objects and events 

### Testing

- Tests should test the domain

### Domain communication and calls 

Options

- RPC
- Queue
- FTP
- DB

To communicate between those 2 

- Create an interface
- Create an adapter in the domain
- Client code depends on the domain

### Multiple domains

Possible to have multiple domains (e.g. product and user)

**Modularizing the monolith**

Protecting from the database ? is database the enemy ? not necessarily

Read [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Do we need application + domain + architecture ? 

No we can use application which is also architecture (pragmatic onion architecture aka hexagonal aka ports and adapters aka clean architecture)

# Monolith vs micro services

- micro services is slow to build
- monolith is fast but should be modular

monolith should be broken down after some time

Breaking it down

- organize your code by entities ! like order.service and not service.order
- instead of linking entities use literal id and get the entity from the other side
- or use a value object
- cut the link from 2 domains
- communication using a common domain events (or event folder per domain) but any events can be accessed by any domain
- never using directly entities or services
- test by using arch unit and having less and less violations
- use Value Object (VO) instead of DTOs
- Sometimes you can create a Order object in Customer domain, "duplicating" the class name but it's good because it doesn't serve the same goal

## Bounded context

Read [https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf](https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf) or [here](https://www.infoq.com/minibooks/domain-driven-design-quickly/)

When 2 contexts have different expectations you should create a bounded context and so create multiple class Chickens for example and disperse the fields in each entity.



## Anti corruption layer

- Make sure nothing from outside goes inside

- In frontend : MVVM viper architecture : read

## Event driven ?

- events or direct service calls ?

- if no return expected -> events potentially over queue
- event = asynchronous message queue, propaget change
- fetch data over GET (sync RPC) 
- DDD uses a lot domain events

## Tests

- Test DSL : for end to end

 