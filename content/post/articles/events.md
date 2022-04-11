# Introduction

Working with events is probably the most popular and efficient way of decoupling a system.

Events have the ability to overcome a number of problems that arise when the software complexity grows with few drawbacks.

Introducing events immediately lowers dependencies and bring the following advantages to the table :

- Objects (subjects) know less about their dependents (observers), and don't event need to know about their existence or if they are initialized
- Events will bring down transitive coupling allowing pieces of code to be developed independently
- Events make testing much more reliable and fast to setup because we now don't need to build a complex graph to test a single part
- Events will ease circular references problems
- Events will also improve the logging / audit trail
- Events bring meaning and intent to the code making it easier to grasp

They have a few drawbacks though :

- Events stream and propagation can make the global understanding harder, especially when there is a lot of them involved
- It's harder to skim through a code using events than normal function invocations
- Events can be harder to debug, especially when they are dispatched application wide

There are many ways to decouple code using events. Here are a few, from lower level to higher level techniques

# Observer pattern

- Low level
- Very efficient and easy to setup
- Observers are linked directly to their subjects which leaves some coupling
- Is usually applicable when the observer already knows about its subjects (one to one or one to many relationships)
- Will replace patterns when the relations of an observer explicitly know the subject (because it is passed in the constructor for example)
- In this case it breaks circular reference and make the subject much leaner and testable
- This pattern can typically be used in an entity / value object relation ship, the value object being the subject



# Event bus pattern

- To dispatch events module or application wide the event bus is a good match
- 