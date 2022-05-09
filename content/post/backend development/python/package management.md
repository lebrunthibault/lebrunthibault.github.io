# Setup.py

- See [stack](https://stackoverflow.com/questions/1471994/what-is-setup-py), the [hitchhiker’s guide to python](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html) and [this description of seutp.py](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/) and [why it’s best to use pyproject.toml](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

- `setup.py` is a python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

- This allows you to easily install Python packages. Often it's enough to write:

  ```py
  $ pip install . 
  ```

  `pip` will use `setup.py` to install your module. Avoid calling `setup.py` directly.

- The [setup.py](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html#setup-py-description) file is at the heart of a Python project. It describes all of the metadata about your project. There a quite a few fields you can add to a project to give it a rich set of metadata describing the project. However, there are only three required fields: name, version, and packages

- setup.py also allows to **install a package locally** without the need to change `PYTHON_PATH` or `sys.path`

