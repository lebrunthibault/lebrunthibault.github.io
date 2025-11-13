---
title: "Django contribution"
draft: true
---



**links**

- [django tutorials for beginners 2021 youtube](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

# Basics

## Install

- Use pipenv
- Nesting can be removed
- Use .env with [django-environ](https://github.com/joke2k/django-environ)
- [django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) like in symfony



## Structure

- Project == site: app == service. project many to many app
- apps can live anywhere in the python path





## Routing

- Each app can define routes in a URLconf file
- The routing file is included in the main site routing URLconf
- `include` chops off matched url part and sends to included for further processing
- Patterns don’t search GET and POST parameters, or the domain name
- Route has url, route name, view (HttpRequest handler) + kwargs. Like in Symfony



## Django ORM

- Model classes



## Logging

- [django and python logging](https://djangodeconstructed.com/2018/12/18/django-and-python-logging-in-plain-english/)
- [django-logging-right-way/](https://lincolnloop.com/blog/django-logging-right-way/) : hands on django logging config includes sentry
- Override django default logging : **Best** 



## Testing



#### Debugger

- Straightforward when running python scripts
- Using django server run configuration (see [this video](https://www.youtube.com/watch?v=zFuaU3Sl4-c))



# Difference django / symfony

- django lighter and more options for views
- system of apps

#### Orm

- saving directly on the entitiy
- not great: magical methods in django (e.g. backward one to many, always use default args)
- app should be added to the installed apps
- better handling of choices / enum  in django (integrated to the model field definition)
- relations
  - one to many : [`ForeignKey`](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey) on the owning side
  - many to many : [`ManyToManyField`](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ManyToManyField) 
  - one to one : [`OneToOneField`](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.OneToOneField)



# Contributing

- [Writing code](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/)

> Django 4.0 will be a time-based release. Any features completed and committed to main by the alpha feature freeze deadline noted below will be included

Schedule

| September 20, 2021 | Django 4.0 alpha; feature freeze. (we will fork `stable/4.0.x` from `main`.) |
| ------------------ | ------------------------------------------------------------ |
| October 25         | Django 4.0 beta; non-release blocking bug fix freeze (all bug fixes except blocking ones) |
| November 22        | Django 4.0 RC 1; translation string freeze.                  |
| December 6         | Django 4.0 final                                             |

## Git flow

- Rebase to one commit before and after review (e.g. `git rebase -i HEAD~2`)

- On upstream change:

  ```bash
  git fetch upstream
  git rebase
  ```

  

