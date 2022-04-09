# Python Import system

TLDR : use sys.path / pythonpath or [specific .pth files](https://stackoverflow.com/questions/15208615/using-pth-files)



Module: A single python script.

Package: A collection of modules.

- import a module in the same directory : import <module>

## What exactly happens when we write an ‘import’ statement?

- The python interpreter tries to look for the *directory* containing the module *we are trying to import* in `sys.path`
- It is a list of directories that Python will search once it is done looking at the cached modules and Python standard library modules
- *The output from* `sys.path` *will always contain the current directory at index 0! The current directory being the one where the script being run resides.*
- An important thing to remember is that whenever an import statement is made, the entire module will be run
- *The code inside the* `*if__name__ == '__main__'*`*statement* ***won’t be run when imported\***
- `from example1 import *` is considered bad practice (bad readability)

## How to import a module from a sibling package ?

1. Using `sys.path.append()` in the script
2. Using PYTHONPATH environement variable : *PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and package*



## *Relative imports (not recommended): specify the path relative to the path of the calling script.*

