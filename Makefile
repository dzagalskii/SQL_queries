all:
    sudo docker-compose stop
    sudo docker-compose rm
    sudo docker-compose up --build