# [Pydantic](https://pydantic-docs.helpmanual.io/)

- [Pydantic](https://pydantic-docs.helpmanual.io/) is a Python library to perform data validation.
- pydantic models extend `from pydantic import BaseModel` 
- works well with mypy

## [Models](https://pydantic-docs.helpmanual.io/usage/models/)

- access some functions like dict(), json(), schema() ..
- Recursive models
- Possible to configure a GetterDict to work with different sources (like XML)
- Raise rich validation errors
- Possible to create field validators to validate values
- Possible to create own validation errors
- Helper functions to parse strings, [pickle](https://docs.python.org/3/library/pickle.html) byte stream, files or python dicts directly
- bypass validation with _fields_set (30x faster)
- Generic models 
  - (using Generic[T]) and <Model>[T] 
  - integrates with mypy
  - Can be (partially) inherited by generic model. 
  - repr Class name configurable.
  - Can be used in composition with other generic models
- model can be dynamically created at runtime (with extending base class, validators)
- creation from namedTuple or [TypedDict](https://adamj.eu/tech/2021/05/10/python-type-hints-how-to-use-typeddict/)
- Modify the `__root__` to define the root type passed to the model
- Make them immutable with allow_mutation = False 
- Works with [ABC](https://docs.python.org/3/library/abc.html)
- Fields are ordered
- Fields can be declared as required or accepting None
- Field can have a dynamic default value (e.g. date)
- Private model attributes (if we need some processing, starts with _)
- model can be cast as a specific type (parse_obj_as)
- pydantic executes data conversion on input with subtypes (e.g. float to int)
- fields can define aliases

### Orm models

- with Config.orm = True can be used to translate sqlAlchemy model to pydantic model (Pydantic models can be created from arbitrary class instances to support models that map to ORM objects.)
- supports recursive mapping
- can map to any reserved name

## [Field types](https://pydantic-docs.helpmanual.io/usage/types)

- All the normal types including typing
- Generators (with helpers for not consuming, checking first value)
- pydantic types (url, file path, color, secret, domain ..)
- constrained types (checks input value, min, max ..)
- strict types to prevent coercion (StringStr, StrictInt ..)
- custom data types: (e.g. regex)
- Generic Classes as Types : validation on type (advanced)

## [Validators](https://pydantic-docs.helpmanual.io/usage/validators/)

- to check consistency of multiple fields (e.g. password1 == password2)
- root validator (on all values)

## [Model config](https://pydantic-docs.helpmanual.io/usage/model_config/)

- Behavior of *pydantic* can be controlled via the `Config` class on a model or a *pydantic* dataclass.

## [Schema](https://pydantic-docs.helpmanual.io/usage/schema/)

- *Pydantic* allows auto creation of JSON Schemas from models

## [Dataclass](https://pydantic-docs.helpmanual.io/usage/dataclasses/)

- pydantic model can extend model or use @dataclass (from pydantic.dataclass)

## [Validation decorators](https://pydantic-docs.helpmanual.io/usage/validation_decorator/)

- Apply validation without using boilerplate code using @validate_arguments
- we can use Annotated[Field()] as type hint

## Settings

- enables easy [settings](https://pydantic-docs.helpmanual.io/usage/settings/) management (env file, unit test overrides)
- source configuration and ordering (via customize_sources)

## [Mypy](https://pydantic-docs.helpmanual.io/usage/mypy/)

- out of the box
- specific [pydantic plugin](https://pydantic-docs.helpmanual.io/mypy_plugin/) with more checks

## [Pycharm Plugin](https://pydantic-docs.helpmanual.io/pycharm_plugin/)

