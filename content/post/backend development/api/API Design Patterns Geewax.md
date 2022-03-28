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
  - “make the common case awesome and the advanced case possible
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



# Part 2. Design principles

