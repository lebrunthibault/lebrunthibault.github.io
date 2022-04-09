# Imports

- see [this article](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355)

- when doing import python checks for 
  - builtin packages
  - sys.path
  - PYTHONPATH

## To import from sibling package

- modify pythonpath env variable
  - on the machine
  - or at runtime when launching the command 
- or modify sys.path at run time e.g. `sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))`