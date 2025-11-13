## building

- use Docker build instead of docker-compose build (or up --build) to take advantage of layer cashing (not so sure)



## Restart

- [How to do a clean restart of a docker instance](https://docs.tibco.com/pub/mash-local/4.3.0/doc/html/docker/GUID-BD850566-5B79-4915-987E-430FC38DAAE4.html)



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



# Editing docker files / library files

> Usually no editor is present in the container

- See [this](https://stackoverflow.com/questions/30853247/how-do-i-edit-a-file-after-i-shell-to-a-docker-container)
- Install vim

  - Connect as root : `docker exec -u 0 -it mycontainer bash`
- install vim
- Use `docker cp`
