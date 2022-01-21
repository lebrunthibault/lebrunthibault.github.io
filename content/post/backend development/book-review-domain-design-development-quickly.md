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
