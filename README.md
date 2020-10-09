# python-microservices
Three python dockerized microservices.

# Run
There a docker-compose.yml file inside every directory.

1- docker-compose build

2- docker-compose up

The service should be availabe. 

# Run tests

docker exec -it <container> pipenv install pytest
docer exec -it <container> pipenv run python -m pytest

# Docker Network

docker network create [OPTIONS] NETWORK
docker network connect NETWORK container
