https://docs.docker.com/get-started/overview/

```
docker ps -a
docker stop [container]
docker start [container]
docker rm [container]
docker images
docker run -p 8080:80 --name hello -d [image]
docker logs hello
docker push rhie/hello-world
docker tag hello-world rhie/hello-world
docker rmi rhie/hello-world
```

```
docker-compose up -d
docker-compose down
```