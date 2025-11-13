

# Doc

- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

# Commands

- pipenv run alembic --version
- pipenv run alembic init : creates the migration envirronment (meaning alembic/ package)
- `alembic revision -m "create account table"` : pour créer une migration
- `alembic upgrade head` (ou <revid> +1, +2 ..)
- alembic downgrade <rev_id> (ou -1, -2) (ou base pour retourner au début)
- `alembic current` : view the current revision:



Creating a new revision :

Another thing to notice is the `down_revision` variable. This is how Alembic knows the correct order in which to apply migrations. When we create the next revision, the new file’s `down_revision` identifier would point to this one



# Files

- env.py : configure the sql alchemy connection. *The `env.py` script is part of the generated environment so that the way migrations run is entirely customizable*
- `script.py.mako` - This is a [Mako](http://www.makotemplates.org/) template file which is used to generate new migration scripts. Whatever is here is used to generate new files within `versions/`. This is scriptable so that the structure of each migration file can be
- `versions/` - This directory holds the individual version scripts. Users of other migration tools may notice that the files here don’t use ascending integers, and instead use a partial GUID approach. In Alembic, the ordering of version scripts is relative to directives within the scripts themselves, and it is theoretically possible to “splice” version files in between others, allowing migration sequences from different branches to be merged, albeit carefully by hand.
- `alembic.ini`



# Alembic.ini

- file_template: [See stack](https://stackoverflow.com/questions/56306156/flask-migrate-make-migrations-in-alphabetical-order) If you really want to change naming convention you can do it by adding `file_template` field to your `alembic.in`

  e.g.: `file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(rev)s_%%(slug)s`



# Cookbook

- [Create and up to date database](https://alembic.sqlalchemy.org/en/latest/cookbook.html#building-uptodate)

