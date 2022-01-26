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
