# FAST API



## Type declarations

 **FastAPI** uses the same declarations to:

- **Define requirements**: from request path parameters, query parameters, headers, bodies, dependencies, etc.

- **Convert data**: from the request to the required type.

- Validate data

  : coming from each request:

  - Generating **automatic errors** returned to the client when the data is invalid.

- Document

   

  the API using OpenAPI:

  - which is then used by the automatic interactive documentation user interfaces.

## ROuting

- *path operation function*
- async def but for sqlalchemy it should be def
- Starlette (and **FastAPI**) are based on [AnyIO](https://anyio.readthedocs.io/en/stable/), which makes it compatible with both Python's standard library [asyncio](https://docs.python.org/3/library/asyncio-task.html) and [Trio](https://trio.readthedocs.io/en/stable/).



## SQL ALchemy

- we should define both sqlalchemy models (extening `Base = declarative_base()`)
- for each model we should add a pydantic model for request / response validation



## [Dependency injection](https://fastapi.tiangolo.com/tutorial/dependencies/)