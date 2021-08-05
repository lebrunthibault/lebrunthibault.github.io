---
Title: "Asyncio notes"
draft: true
---

# Asyncio

> single thread cooperative multitasking

## [Awaitable](https://docs.python.org/3/library/asyncio-task.html#awaitables)

### [Coroutine]()

```python
async def: pass
```

> A coroutine execution returns a coroutine object. Simply calling a coroutine will not schedule it to be executed
>
> Coroutine can be awaited and it makes the execution synchronous from the caller perspective

Can be run with :

- `await`
- `asyncio.run()`
- `asyncio.create_task()` to run coroutines concurrently as asyncio tasks

### Task

> Tasks are used to schedule coroutines *concurrently*

```python
async def coroutine():
    return 42

async def main():
    # Schedule nested() to run soon concurrently with "main()".
    task = asyncio.create_task(coroutine())
    # or task = asyncio.ensure_future(coroutine())

asyncio.run(main())

```

### Future

> A [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future) is a special **low-level** awaitable
>
> Future objects in asyncio are needed to allow callback-based code to be used with async/await.

## Running an asyncio program

- Using `asyncio.run(coroutine())`
- Creates an event loop and manages awaiting and closing the pool
- Only one pool allowed at the same time by thread

