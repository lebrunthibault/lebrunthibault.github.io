# Preface

- In the real world, I learned how perfectly-optimized code is not nearly as valuable as well-designed code

# Part 1. Introduction

## 1. Introduction to APIs

- API vs web API : much more control using local API vs web API (because it's a local copy). Web API can change or shutdown without notice. For creators, the web 
- api offers more control as they can change things for all users and protect their algorithms
- APIs provide a way to speak the language computers need to interact in a safe and stable way
- how can we make sure the APIs we build fit together like Lego bricks? Let’s start by looking at one strategy for this, called resource orientation

### What are resource-oriented APIs?

- “remote procedure call” (RPC) because we’re effectively calling a library function (or procedure) to be executed on another computer that is somewhere potentially far away (or remote)
-  It turns out that RPC-style APIs are great for stateless functionality, but they tend to be a much poorer fit when we introduce stateful API methods
-  resource-oriented APIs rely on the idea of “resources,” which are the key concepts we store and interact with, standardizing the “things” that the API manages
- **Resource-oriented APIs are a way of designing APIs to reduce complexity by relying on a standard set of actions, called methods, across a limited set of things, called resources**
- Second, rather than using arbitrary RPC names for any action we can think of, resource-oriented APIs limit actions to a small standard set 
- Thinking of this a bit differently, resource-oriented APIs are really just a special type of RPC-style APIs where each RPC follows a clear and standardized pattern: ().

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220328140925132.png" alt="image-20220328140925132" style="zoom: 67%;" />

- For some scenarios RPC oriented APIs will be a better fit (**particularly in the case where the API method is stateless**)
- REST APIs use standardization and make learning them easier and their actions clearer

### What makes an API “good”?

- Operational : + non operational (latency, precision ..)
- Expressive : system allows users to express the thing they want to do clearly and simply. All features should be accessible in the API (no workarounds necessary for users)
- Simple :
  - design this API to be as simple as possible, but no simpler 
  - **make the common case awesome and the advanced case possible**
- Predictable (consistent) : 
  - “If it’s exciting, you’re doing it wrong.”
  - Consistent field names
  - purpose of the book :  APIs built using well-known, well-defined, clear, and (hopefully) simple patterns will lead to APIs that are predictable and easy to learn

## 2. Introduction to API design patterns

###  What are API design patterns?

- Building from scratch is difficult but flexible. Using an existing tool is simple but not flexible
-  It turns out that choosing one of the in-between options (customizing existing software or building from a design document) is much less common but could probably be used more often with great results. And this is where design patterns fit in.
- example : logger -> Singleton

### Why are API design patterns important?

- the iterative approach, advocated in particular by the agile development process, is difficult to apply when designing APIs.  To see why, we have to look at two aspects of software systems. First, we have to explore the flexibility (or rigidity) of the various interfaces generally, and then we must understand what **effect the audience of the interface has on our ability to make changes** and iterate on the overall design.
- Flexibility :
  - graphical user-interfaces (GUIs), which are used primarily by humans rather than computers and as a result are much more resilient to change
  -  interfaces where users can easily accommodate changes are **flexible** and those where even small changes (like renaming fields) cause complete failures are **rigid**
- Visibility :
  - Generally, we can put most interfaces into two different categories: those that your users can see and interact with (in software usually called the **frontend**) and those that they can’t (usually called the **backend**).

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220328143844483.png" alt="image-20220328143844483" style="zoom: 67%;" />

### Anatomy of an API design pattern

- Name and synopsis: 
  - unique name in the catalog, clear and not too long + description. quickly identify whether any particular pattern is worth further investigation
- Motivation : 
  - definition of the problem space (use case), with details
  - We also must explore how the system should react in failure scenarios or incorrect data
  - The pattern can propose solutions or leave problem resolution to the implementation
- Overview : 
  - a high-level description of the solution, with details (parameters format ..)
  - for complex problems with multiple solutions (e.g. many to many in API) : the overview will discuss each of the different options and the strategy employed by the recommended pattern
  - trade-offs section at the end of the pattern description
- Implementation :
  -  interface definitions defined as code
  -  The API definitions will focus on the structure of resources and the various specific ways to interact with those resources (including hierarchical relationships
  - default values
  - error values
  - additional discussion if necessary
  - Finally, this section will include an example API definition, with comments
- Trade-offs :
  - Not possible things
  - Things that get complicated

### Case study: Twapi, a Twitter-like API

#### Listing messages

- Pagination pattern

#### Exporting data

> Asynchronous because big. Configurable destination / compression / encryption

- Import / Export pattern. Introduces

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220328150559418.png" alt="image-20220328150559418" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220328150402943.png" alt="image-20220328150402943" style="zoom:67%;" />



### NB : versionning with fastapi

- See [this](https://medium.com/geoblinktech/fastapi-with-api-versioning-for-data-applications-2b178b0f843f)
- [Four rest api versioning strategies](https://www.xmatters.com/blog/blog-four-rest-api-versioning-strategies/)

# Part 2. Design principles

 ## Naming

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604100212150.png?token=AEHIPTNH44Z7MWP3OJTOBM3CTMW6G" alt="image-20220604100212150" style="zoom:80%;" />

-  changing names in an API can be quite challenging
- choose it good from the start

### What makes a name good ?

- expressive : clear and unambigous (prefer slightly longer names)

- simple : when the context is sufficiently clear prefer simple

  <img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604100654411.png?token=AEHIPTKJUTLETCX7A3S4LB3CTMXPU" alt="image-20220604100654411" style="zoom:80%;" />

- Predictable : consistent

###  Language, grammar, and syntax

- language : use english (consistent with other APIs)
- Grammar :
  - Imperative actions : 
    - like in REST
    - don't use indicative
    - e.g. GetValidationErrors is better than isValid
  - Prepositions :
    - "with", "to", "for"
    - Code smell, shows duplication in the name
    - e.g. ListBookWithAuthors, ListBookWithPublishers
  - Pluralization
    - Most often, we’ll choose the names for things in our APIs to be the singular form, such as Book, Publisher, and Author
    - if an API uses RESTful URLs, the collection name of a bunch of resources is almost always plural. Ex : /books/1234
    - plural should be valid english
  - Syntax 
    - Most technical aspect of naming
    - CASE
      - consistency
    - Reserved keywords
      - ex don't use string, to, from ..

### Context

> we should be cognizant of that context and the meaning it might impart (for better or worse) when choosing names

### Data types and units

- specify the type for ambiguous cases

  - eg. sizeBytes : float is better than size: float

- sometimes names become more clear and usable when a unit is included in the name, other times a name can become more clear when using a richer data type

  <img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604104735652.png?token=AEHIPTPNAOXQSYP5RG5IKH3CTM4IM" alt="image-20220604104735652" style="zoom:80%;" />

### Case study: What happens when you choose bad names?

- ex: Google pageSize vs maxPageSize. Like getting 8 donuts when you asked for 10

# 4 Resource scope and hierarchy

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604105411173.png?token=AEHIPTIE4AIIHSWHJEZRBDTCTM5A6" alt="image-20220604105411173" style="zoom:80%;" />

-  resource layout is the entity (resource) relationship model for a particular design of an API
- like in design, type of relation ships: multiple bidirectional, optional ..
- Reference relationships == many to one
- Many to many
- self reference (often in a graph)
- hierarchical relationships (owning an entity)
- entity diagram 

#### 4.2 Choosing the right relationship

- Do you need a relationship at all? Put differently, reference relationships should be purposeful and fundamental to the desired behavior. In other words, these relationships should never be accidental, nice to have, or something you might need later on. Instead, any reference relationship should be something important for the API to accomplish its primary goal: **meaningful**
-  References or in-line data : use reference id (reference, double API calls, expensive if the info is not needed often) or inline object (in-line data, single API call). judgment call
- Hierarchy 
  - biggest effect: deletion cascade
  - depends on the modeling
  - many to one but not one to many

#### Anti patterns

- Resources for everything :
  -  if you don’t need to interact with one of your proposed resources independent of a resource it’s associated with, then you might be fine with it being just a data type -> **cf aggregate root** (don't make accessing inner data possible)
  - inline if applicable

####  Deep hierarchies

- cf inheritance, make a more flexible design / model

#### In-line everything

- cf no sql etc.. inlined data is not easy to update

# Data types and defaults

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604111346190.png?token=AEHIPTIA7SEECIPOZKSAI3LCTM7KQ" alt="image-20220604111346190" style="zoom:80%;" />

NB : datatypes in the signature are not always precise enough (str / bytes, float / second / microsecond ...)

## Introduction to data types

- , when designing APIs, we have to break out of the mode of thinking of a single programming language primarily because a major goal of our API is to let anyone, programming in any language, interact with the service (any source language, using text)
- Using serialization : structured data to serialized bytes
![image-20220604111726133](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604111726133.png?token=AEHIPTO74BYBD6CIFZ6QDW3CTM7YI)
- down size: some type information will be lost in translation
- how we might extend our serialization format (JSON) in cases where it doesn’t stack up with our needs

### Missing vs. null

- 3 cases : explicit null (JSON), empty value ("", 0), value absent (normally caught or cast to null by data validation)

  ![image-20220604112131770](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604112131770.png?token=AEHIPTMZMVIX3S7QPPI3AB3CTNAHS)

### Booleans

- when they become limited and we need to use multiple flags : use a string / enum type
- rather don't use double negatives

### Numbers

- In general, values that only happen to look like numbers but behave more like tokens or symbols should probably be string values instead (e.g. string for ids)
- use bounds (min, max)
- use default values if possible
- pay attention : big numbers serialization

### Strings

- bounds, defaults
- serialization : it’s a good idea for APIs to reject incoming strings that aren’t UTF-8 encoded using Normalization Form C, but an absolute necessity for strings that happen to represent resource identifiers

### Enumerations

- In short, enumerations should generally be avoided when another type (such as a string) can work instead
- This is particularly true when new values are expected to be added, and even more so when there’s some sort of standard out there for the value in question (e.g. mime types)

### Lists

- atomicity : : list fields, despite containing multiple items, are best used when the items are considered an atomic piece of data to be modified and replaced entirely rather than piecemeal. Problems with ordering, race / loop conditions (add)
- Never allow a value in a list to be updated independently, update the list in bulk.
- Also never 2 ways to update a value
- bounds on list size and item size. Or switch to relations instead of inline
- Lists are similar to strings in that in some serialization formats and libraries there is no easy way to distinguish between the zero value (for lists, []) and a null value

### Maps

- In other words, custom data types are simply a way of rearranging fields we know of and want to organize a bit better, while maps are better suited for dynamic key-value pairs with keys that are unknown at the time we define the API
-  This kind of arbitrary structure of key-value pairs (maps) is a great fit for things like dynamic settings or configuration
- bounds : the schema defines its own boundary conditions. For maps bounds can be set

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220604115334846.png?token=AEHIPTPP3GEHBRJWKR6526LCTND7W" alt="image-20220604115334846" style="zoom:80%;" />

