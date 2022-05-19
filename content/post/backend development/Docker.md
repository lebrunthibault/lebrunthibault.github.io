## building

- use Docker build instead of docker-compose build (or up --build) to take advantage of layer cashing (not so sure)



## Debug

- see [this article](https://medium.com/@betz.mark/ten-tips-for-debugging-docker-containers-cde4da841a1d)

- docker exec <id> “<command>”
- docker exec <id> -it bash
- docker logs <id>
- docker ps -a : list all containers
- docker rm (-f) <id> : remove a container
- docker inspect <id>
- docker network ls



## Connecting to the database

- [Use the container name](https://stackoverflow.com/questions/49325745/how-do-i-access-postgresql-within-docker-with-sqlalchemy) and not localhost in the container

