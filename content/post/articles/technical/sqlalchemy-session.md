---
prod: true
draft: false
title: Sqlalchemy's session
category: Backend development
description: Overview of the inner workings of an sqlalchemy session
keywords:
  - Software development
  - Backend development
  - Database
  - Sqlalchemy
  - Python
date: "2022-01-01"
---

# Foreword

As a backend developer, having a good grasp of database management is important.

In python the standard orm is sqlalchemy and it introduces a number of technical concept, that can be sometimes obscure and somewhat not so clearly documented.

The central sqlalchemy object we manipulate in userland backend code is the session object.

Let’s introduce what a sqlalchemy session is, and some simple and advanced use cases

I’ll quote the documentation regularly and reformulate some parts.



# Introduction

>  the primary usage interface for persistence operations is the [`Session`](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session).



- A session is a “holding zone” for all the objects which you’ve loaded (e.g. via `session.query()`)or associated (e.g. via `session.add()`) with it during its lifespan
- sessions are lightweight objects that cannot be shared between processes / threads. A process can also create multiple sessions.



# General database connection concepts

See [stack](https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference)

Sqlalchemy uses different objects to handle connection and maps orm objects changes.

**Engine** and **Connection** objects are low level and allows raw sql execution **and are therefore almost never used in a classic orm usage**

> When using the SQLAlchemy ORM, the public API for transaction control is via the [`Session`](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session) object

- **Engine** : low level, It [maintains a pool of connections](http://docs.sqlalchemy.org/en/latest/core/pooling.html). Can be used to execute raw sql

  ```python
  result = engine.execute('SELECT * FROM tablename;')
  ```

- **Connection**: does the work of executing a SQL query. You should do this whenever you want greater control over attributes of the connection, when it gets closed. Useful for handling e.g. a [Transaction](http://docs.sqlalchemy.org/en/rel_1_0/core/connections.html#using-transactions) when using raw sql

- **Session**: higher level objects using connections and transactions under the hood to run their automatically-generated SQL statements.

  `session.execute` forwards the raw sql to its engine / connection

## Internal structure

- The [`Session`](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session) may be constructed on its own or by using the [`sessionmaker`](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.sessionmaker) class. It typically is passed a single [`Engine`](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine) as a source of connectivity up front.
