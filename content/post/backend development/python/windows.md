# Windows tricks

- to add to path : create a <file>.pth in site packages for the chosen python version

  

## Python default version

- if using `python` setting up with PATH and system PATH
- if using `py`: use [windows python launcher](https://docs.python.org/fr/3/using/windows.html#launcher) 
  - setup : PY_PYTHON and PY_PYTHON{major} path variables (in user and system)

## [Module search](https://docs.python.org/fr/3/using/windows.html#finding-modules)

> Python stocke généralement sa bibliothèque (et donc votre dossier `site-packages`) dans le répertoire d'installation. Donc, si vous aviez installé Python dans `C:\Python\`, la bibliothèque par défaut résiderait dans `C:\Python\Lib\` et les modules tiers devraient être stockés dans `C:\Python\Lib\site-packages\`.

- sys.path can be overwritten totally or 

## Install wheels / windows stuff

- Install wheels with https://www.lfd.uci.edu/~gohlke/pythonlibs/
- install via pip install <wheel_file>
- or push to github and pipenv install <raw_url>

## Pipenv

- slow
- cannot install wheel rtmidi_python-0.2.2-cp37-cp37m-win_amd64.whl ..?



## Poetry

- Buggy on windows, cannot do poetry add (EnvironmentError cannot find the python interpreter)