# Python interfaces

See [Real Python](https://realpython.com/python-interface/#python-interface-overview)

## Informal interfaces

- define a base class with 'abstract" methods (e.g. throwing NotImplementedError)
- Subclass by implementations
- Pb : `issubclass(<subclass>, <baseclass>)` is always true even when the subclass doesn't fully implement the interface
- `<subclass>.__mro__` shows the interface even when its not implemented
- NB : when raising NotImplementedError, pycharm warns in the subclass but mypy doesn't

## Using Metaclasses

> Check [this great article](https://levelup.gitconnected.com/metaphysics-2036b38fa711)

- Implementing 2 dunder methods : `__instancecheck__()` and `__subclasscheck__()`

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401152803914.png" alt="image-20220401152803914" style="zoom:67%;" />

- By using a metaclass, you don’t need to explicitly define the subclasses. Instead, the subclass must **define the required methods**. If it doesn’t, then `issubclass(EmlParserNew, UpdatedInformalParserInterface)` will return `False`
- As you can see, `UpdatedInformalParserInterface` is a superclass of `PdfParserNew`, but it doesn’t appear in the MRO. This unusual behavior is caused by the fact that `UpdatedInformalParserInterface` is a **virtual base class** of `PdfParserNew`.

## Virtual base classes

- When a class builds from a metaclass it will be a virtual base class of any class implementing the metaclass

- A class building from a metaclass can be called an interface

- We have

  - `isinstance(Interface, Metaclass) == True` if interface builds from the metaclass

  - `issubclass(ConcreteClass, Interface) == True` if ConcreteClass implements Interface
  - `isinstance(ConcreteClass(), Interface) == True`

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401175101399.png" alt="image-20220401175101399" style="zoom:67%;" />



## Metaclasses usage

- [See stack](https://stackoverflow.com/questions/392160/what-are-some-concrete-use-cases-for-metaclasses#:~:text=Having%20considered%20the%20most%20common,or%20function%20can%20unbake%20them.)
- Registering each subclass in a data structure
- Allow changing the evaluation of class body
- Allow creating overloaded methods

## Formal Interfaces

### Using `abc.ABCMeta`

- like creating a custom metaclass but more standard

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401180949945.png" alt="image-20220401180949945" style="zoom:67%;" />



### Using `abc` to Register a Virtual Subclass

- Once you’ve imported the `abc` module, you can directly **register a virtual subclass** by using the `.register()` metamethod
- NB : allows creating metaclass of literal types for example
- Once you’ve registered `Double`, you can use it as class [decorator](https://realpython.com/courses/python-decorators-101/) to set the decorated class as a virtual subclass. NB : can be dangerous
- `__subclasshook__` takes precedence over register

### Using Abstract Method Declaration



# [Mypy Protocols](https://mypy.readthedocs.io/en/stable/protocols.html)

- Mypy supports two ways of deciding whether two classes are compatible as types: nominal subtyping and structural subtyping
- Nominal subtyping = normal inheritance, compatible with instance of
- Structural subtyping : 
  - Class `D` is a structural subtype of class `C` if the former has all attributes and methods of the latter, and with compatible types
  - Structural subtyping can be seen as a static equivalent of duck typing

## Existing protocols

- Iteration protocols: Iterable[T] and Iterator[T]
- Collection protocols: Sized, Container[T], Collection[T]
- etc.. (One-off protocols, Async Protocols, Context manager protocols ..)

## User defined protocols

![image-20220401155546245](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220401155546245.png)

- Note that inheriting from an existing protocol does not automatically turn the subclass into a protocol – it just creates a regular (non-protocol) class or ABC that implements the given protocol (or protocols). The `Protocol` base class must always be explicitly present if you are defining a protocol



# Interface libraries

- `zope.interface` [[zope-interfaces\]](https://peps.python.org/pep-0544/#zope-interfaces) was one of the first widely used approaches to structural subtyping in Python
- Design by contract, supports invariants

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220408172725336.png?token=AEHIPTIG5GFXQPQRXC3Y5KDCKBKKK" alt="image-20220408172725336" style="zoom:67%;" />
