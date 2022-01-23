---
title: uml
draft: true
---



# Association vs Aggregation vs Composition

If two classes in a model need to communicate with each other, there must be a link between them, and that can be represented by an association (connector).

Association can be represented by a line between these classes **with an arrow indicating the navigation direction**. In case an arrow is on both sides, the association is known as a bidirectional association.

**Association** = link between two classes. Can be unidirectional or bidirectional. Can be one to many or one to one

**Aggregation** and **Composition** are subsets of association meaning they are **specific cases of association**. In both aggregation and composition object of one class "owns" object of another class. But there is a subtle difference:

- **Aggregation** implies a relationship where the child can exist independently of the parent. Example: Class (parent) and Student (child). Delete the Class and the Students still exist.
- **Composition** implies a relationship where the child cannot exist independent of the parent. Example: House (parent) and Room (child). Rooms don't exist separate to a House.
