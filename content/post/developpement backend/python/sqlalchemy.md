

### Tutos

- [Advanced SQLAlchemy Features You Need To Start Using](https://martinheinz.dev/blog/28)



### Libs

- [Sql alchemy mixins](https://github.com/absent1706/sqlalchemy-mixins)

# [Core vs ORM](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_expression_language.htm)

> SQLAlchemy core uses SQL Expression Language that provides a **schema-centric usage** paradigm whereas SQLAlchemy ORM is a **domain-centric mode of usage**.

- Core = Expression langage (select() etc ..)
- Orm = session.query(User) etc..



# Queries

## ORM

- `session.query(User).filter(User.first_name == "toto")`

### Select 

- `select(User).where(User.first_name == “toto”)`
- returns ORM obejcts
- [scalars](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html): use `.scalars()`to get the first row



## Core / Expression language

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_expression_language.htm
- Lower level / closer to sql / rarer / more comprehensive
- Useful in hybrid properties

### Select

- `select(user_table).where(user_table.c.name == 'spongebob')`
- returns Rows



## [Column Properties](https://martinheinz.dev/blog/28)

- Like hybrid attributes but simpler

- Support overloaded python operators + sql expressions

- > column properties won't be populated before you commit the session, which might be unexpected when working with freshly created record



## [Hybrid attributes](https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html)

- Allow both normal property access and sql generation to be used in queries (filters ..)



### Many to Many Hybrid property

- join on secondary table

- See [stack](https://stackoverflow.com/questions/70435050/how-to-set-a-m2m-hybrid-count-property-in-sqlalchemy/70476720#70476720)



### [Association proxy](https://docs.sqlalchemy.org/en/14/orm/extensions/associationproxy.html)

- Proxy a one to many or M2M attribute
- Leaner code
- Can be used in queries



## [Aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html#many-to-many-aggregates)

- Creates a new column and populates it with the result of a property
- Faster performance than hybrid attributes
- Same syntax as an hybrid property
- Supposed to be automatic but I should test it more