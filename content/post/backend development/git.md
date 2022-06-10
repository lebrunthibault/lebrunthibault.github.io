# Submodules

- Voir [doc git](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- See [this](https://shunsvineyard.info/2019/12/23/using-git-submodule-and-develop-mode-to-manage-python-projects/)



### Problèmes rencontrés 

- **Ne jamais mettre le dossier du submodule dans le gitignore**



### Installation

- `git submodule add https://github.com/chaconinc/DbConnector`

### [Modification du repo upstream](https://stackoverflow.com/questions/11637175/swap-git-submodule-with-own-fork)

- Update l’url dans **.gitmodules**
- `git submodule sync`

### [Suppresion](https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule)

### Mise a jour

- `git submodule update` to sync the submodule from upstream
- Mettre a jour : 
  - cd <sub_module>
  - git pull



### Mise à jour du back

- git pull
- git submodule update --init --recursive



### Développement sur le submodule

- chaque submodule doit etre push avant de push sur le repo principal
- Utiliser : `git config push.recurseSubmodules check` (block) pour enforce ca ou `git config push.recurseSubmodules on-demand`
- ou git submodule foreach git push
- rajouter un pre commti check




# [Subtree](https://www.atlassian.com/git/tutorials/git-subtree)

- alternative to git submodule
- transparent for deploy and other devs
- slightly harder to contribute upstream

## Forking

- can contribute back just by doing a regular pull request to the upstream repo
- forked repo should be configured to pull changes from the original upstream repo  **by adding a remote** (see [this](https://www.youtube.com/watch?v=a_FLqX3vGR4)) : `git remote add upstream <upstream_repo>`
- sync :
  - git fetch upstream
  - git merge upstream/main
- on dev sur main sur le fork
- on sync l’upstream dans main



|      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |
|      |      |      |      |      |
|      |      |      |      |      |
|      |      |      |      |      |



# Pypi

- [Create your own python package and publish it to pypi](https://towardsdatascience.com/create-your-own-python-package-and-publish-it-into-pypi-9306a29bc116)
- [tuto officiel](https://packaging.python.org/en/latest/guides/using-testpypi/)
- Generate the source distribution : `python setup.py sdist`
- Push to pypi : `twine upload --repository testpypi dist/* --verbose` 
- package name can be different than import names (like I did with sqladmin). Can happen [in the following cases](https://stackoverflow.com/questions/54886143/why-are-some-python-package-names-different-than-their-import-name) : 
