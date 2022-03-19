# Types



## Generics

### Upper bounds

- See [stack](https://stackoverflow.com/questions/59933946/difference-between-typevart-a-b-and-typevart-bound-uniona-b)

- TypeVar('T', A, B) means upper bounded by A or by B (e.g. with List it means array of A or array of B) or any subtype
- TypeVar('T', Union[A, B]) means upper bound by Union (so List can be List[Union[A, B]]) or any subtype combination