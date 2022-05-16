# [Python packaging and distribution](https://www.youtube.com/watch?v=wCGsLqHOT2I)

- how to package and distribute python code ?
- 2 libraries exist 
  - distutils (part of python): old and not used directly anymore
  - setuptools (the "new" - 2004) high level tool using distutils. De facto standard
- They both have the same API and the same command interface

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220513163558641.png?token=AEHIPTI5I5MRK4AV3MCGRQLCP2ETA" alt="image-20220513163558641" style="zoom:50%;" />



## Setup tools

- de facto standard
- single function setup
- setup tools is not part of python. check if it is available: `python -c 'import setuptools'`
- command to package the project : `python setup.py sdist`. 
- Creates a dist folder containing a tar file containing :
  - all the python files
  - Using **MANIFEST.in** we can add non python files to the dist package
- Distribute with twine on pypy

## How to have a package available without pushing it to pypy ?

- `python setup.py develop`
- creates a symbolic link to your site packages

# PIP

- [`pip` is a higher-level interface](https://stackoverflow.com/questions/8550062/how-do-setuptools-distribute-and-pip-relate-to-one-another#:~:text=pip%20is%20a%20higher%2Dlevel,controversial%20features%2C%20like%20zipped%20eggs.) on top of setuptools or Distribute. It uses them to perform many of its functions but avoids some of their more controversial features, like zipped eggs
- `pip` also provides features not available in `setuptools`, like an uninstall command and the ability to define fixed sets of requirements and reliably reproduce a set of packages
- pip use wheels as a format for binary distribution