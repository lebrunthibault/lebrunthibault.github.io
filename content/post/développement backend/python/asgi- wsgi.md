ASGI (*Asynchronous Server Gateway Interface*) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.



Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.



# WSGI

WSGI applications are a single, synchronous callable that takes a request and returns a response; this doesn’t allow for long-lived connections, like you get with long-poll HTTP or WebSocket connections



# ASGI

ASGI is structured as a single, asynchronous callable. It takes a `scope`, which is a `dict` containing details about the specific connection, `send`, an asynchronous callable, that lets the application send event messages to the client, and `receive`, an asynchronous callable which lets the application receive event messages from the client.



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220319103752989.png" alt="image-20220319103752989" style="zoom:50%;" />

 ## FastAPI

- Uses an ASGI server, for production such as [Uvicorn](https://www.uvicorn.org/) or [Hypercorn](https://gitlab.com/pgjones/hypercorn)
- NB : You can combine asgi it with Gunicorn, to have an asynchronous multi-process server.