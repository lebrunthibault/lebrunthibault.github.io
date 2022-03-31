# [Interfaces naming conventions](https://verraes.net/2013/09/sensible-interfaces/)

- Never use prefix / suffix for interfaces / abstract classes :
  - interfaces are first class citizen
  - having suffix can confuse what should be type hinted
  - calling code should not differentiate interfaces vs concrete classes
  - "default" implementation should have a long name (e.g. not just Translator)
  - interfaces should have english names (CastToJson better than Jsonable)