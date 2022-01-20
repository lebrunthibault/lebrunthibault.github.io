# Protecting the domain by [Victor Rentea](https://victorrentea.ro/)

talk on [youtube](https://www.youtube.com/watch?v=cK19rE2V9UY)

Important principles :

- Dependency inversion
- DRY
- Single Responsibility

Archunit : equivalent in php : https://github.com/qossmic/deptrac or https://github.com/j6s/phparch or https://github.com/mihaeu/dephpend or https://github.com/carlosas/phpat

## Domain

- DDD : domain driven development

- Client code
- higher level code

Infrastructure

- backend code
- lower level code
- implementations

### Protect the domain

- Keep the domain safe from any external influence.  Defend the domain ! Agnostic.

- Defend it from someone else when you call lower level code
- domain logic should not depend on infrastructure
- Keep core logic independent of UI
- independent of DB, no vendor lockins, no stored procedures, no too complicated sql
- indepent of external apis
- is an orm intrusive ? not necessarily
- logic should be built on objects you have full control on 

### DTOs are enemis

they are

- bloated
- flat
- different perspective

### Testing

- Tests should test the domain

### Domain calling infrastructure 

Options

- RPC
- Queue
- FTP
- DB

To communicate between those 2 

- Create an interface
- Create an adapter in the domain
- Client code depends on the domain
- Infrastructure 

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
- instead of linking entities use literral id and get the entity from the other side
- or use a detail object 
- cut the link from 2 domains
- communication using a common domain events. or split events but any events can be accessed by any domain
- but never using directly entities or services
- test by using archunit and having less and less violations
- use Value Object (VO) instead of DTOs
- Sometimes you can create a Order object in Customer domain, "duplicating" the class name but it's good

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

 