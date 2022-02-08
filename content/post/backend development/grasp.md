---
title: grasp
draft: true
---



# [GRASP](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design))



## Information expert

- Assign responsibility to the class that has the information needed to fulfill it.

>  Low Coupling, High Cohesion

## Creator

 In general, Assign class `B` the responsibility to create object `A` if one, or preferably more, of the following apply

- Instances of `B` contain or compositely aggregate instances of `A`
- Instances of `B` record instances of `A`
- Instances of `B` closely use instances of `A`
- Instances of `B` have the initializing information for instances of `A` and pass it on creation

> Low Coupling, [Factory pattern](https://en.wikipedia.org/wiki/Factory_pattern)

### Controller

