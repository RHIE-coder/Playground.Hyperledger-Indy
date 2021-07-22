# 환경셋팅

## 🌈Ubuntu 18.4 LTS

[Download Ubuntu 18.4](https://releases.ubuntu.com/bionic)

## 🌈VirtualBox

[Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## 🌈Putty

[Download Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

## 🌈Visual Studio Code

[Download VSCode](https://code.visualstudio.com)

## 🌈Reference Document

[Hyperledger Indy]()

## 🌈Start Setting

### 🍀원격 환경
1. VirtualBox에 Ubuntu설치하기
2. VirtualBox 게스트 확장과 한글 입력 셋팅해보기[Shift+Space]
3. putty로 리눅스 접속
 - 리눅스에 `openssh-server` 설치
```shell
sudo apt-get install openssh-server
sudo service sshd start
```
 
 - active(running) 상태인지 확인하기
```shell
sudo service sshd status
```

 - VirtualBox에 포트포워딩하기

#### 게스트OS IP확인
```shell
sudo apt install net-tools
```
```shell
ifconfig
```
#### 호스트OS IP확인
window cmd
```cmd
ipconfig
```

 - Putty로 접속

4. VSCode로 리눅스 접속

 - 확장 프로그램 설치
    - Remote - SSH

 - `F1`누르고 `Remote-SSH:Connect to Host..` 하기
```
>remotessh
```
 - 접속 하기 `[userid]@[ipaddress]`

*example*

```
rhie@192.168.56.1
```
#### 에러발생시 아래 폴더 확인
```
C:\Users\[사용자 이름]\.ssh
```

### 🍀Prerequisites
#### jq
```
sudo apt install jq
```

#### git
```
sudo apt install git
```
#### curl
```
sudo apt install curl
```

#### wget
```
wget --version
```

#### docker
[click](./background/docker/01.설치.md)

#### [node.js SDK] Python 2.7버전 있는지 확인
```
python --version
```
리눅스 Ubuntu 18.04는 기본적으로 깔려 있을 있을 것

#### [node.js SDK] Node.js 설치
PPA를 통해 최신버전 가져오기(14버전) LTS
```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
```
설치
```
sudo apt-get install -y nodejs
```
확인
```
node -v
npm -v
```
NPM의 제 기능을 위해 부가설치(npm install 에러 방지)
```
sudo apt-get install build-essential
```