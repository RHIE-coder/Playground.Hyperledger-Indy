# docker install 

`the official document is more accuracy`

[go site](https://docs.docker.com/engine/install/ubuntu/)

# docker : `docker engine`
## - 오래된 버전 지우기
```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

## - docker repository 준비
 - 도커 엔진을 새로운 환경에 처음 설치하기 전에 `docker repository`를 준비해야 이 레파지토리로부터 docker를 설치하거나 업데이트를 할 수 있다.

 1. Update the apt package index and install packages to allow apt to use a repository over HTTPS
```shell
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

 2. add docker's official GPG key
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

 3. Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or text(or both) after the word stable in the commands below.
 ```shell
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 ```

 4. Install Docker Engine
```shell
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo docker run hello-world
```

 5. If you would like to use docker as a non-root user, you should now consider adding your user to the 'docker' group sith something like:
 ```
sudo usermod -aG docker your-user
 ```

## - 설치 삭제

Uninstall the Docker Engine, CLI, and Containerd packages:
```shell
sudo apt-get purge docker-ce docker-ce-cli containerd.io
```

Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
```shell
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```
<br><br><br><br><br>

# docker : `docker compose`
## - 설치
Run this command to download the current stable release of Docker Compose:
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Apply executable permissions to the binary:
```shell
sudo chmod +x /usr/local/bin/docker-compose
```
```shell
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## - 설치 삭제

To uninstall Docker Compose if you installed using curl:

```shell
sudo rm /usr/local/bin/docker-compose
```

## - 설치 확인

check the version of Docker:

```shell
docker --version
```

Make sure the docker daemon is running:

```shell
sudo systemctl start docker
```

check the version of Docker Compose:

```shell
docker-compose --version
```