# 환경셋팅

## 🌈Ubuntu 18.4 LTS

[Download Ubuntu 18.4](https://releases.ubuntu.com/bionic)

## 🌈VirtualBox

[Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## 🌈Putty or WSL2

[Download Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

 - how to download `WSL2`
 
```
[Powershell 관리자모드로 실행]
wsl --install
[컴퓨터 재부팅]
[Microsoft Store에서 Windows Terminal 설치]
wsl
sudo apt-get update
sudo apt-get install wget ca-certificates
logout
```

## 🌈Visual Studio Code

[Download VSCode](https://code.visualstudio.com)

## 🌈Reference Document

[Hyperledger Indy](https://github.com/hyperledger/indy-sdk)

## 🌈Start Setting

### 🍀원격 환경

#### 1. VirtualBox에 Ubuntu설치하기
#### 2. VirtualBox 게스트 확장과 한글 입력 셋팅해보기[Shift+Space]
#### 3. putty 혹은 WSL2로 리눅스 접속

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

<br><br>

#### - 게스트OS IP확인
```shell
sudo apt install net-tools
```
```shell
ifconfig
```

<br><br>

#### - 호스트OS IP확인
window cmd
```cmd
ipconfig
```

 - Putty로 접속

<br><br>

#### 4. VSCode로 리눅스 접속

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
[how to install](./background/docker(install).md)

[how to use](./background/docker(usage).md)


`Get Permission`을 하기 위해 리눅스 재부팅

#### [node.js SDK] Python 2.7버전 있는지 확인
```
python --version
```

만일 깔려있지 않다면 아래 명령어 실행

```
sudo apt install python
```

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



### 🍀Hyperledger Indy

#### Indy SDK Repository 가져오기

```cmd
git clone https://github.com/hyperledger/indy-sdk
```

#### Indy 노드풀 실행

[참고](https://github.com/hyperledger/indy-sdk/blob/master/README.md#how-to-start-local-nodes-pool-with-docker)

```cmd
cd indy-sdk
docker build -f ci/indy-pool.dockerfile -t indy_pool .
docker run --name indy_pool -itd -p 9701-9708:9701-9708 indy_pool
```

#### Indy SDK 빌드하기 (`libindy.so`)
[참고](https://github.com/hyperledger/indy-sdk/blob/master/docs/build-guides/ubuntu-build.md)

1. Install Rust and rustup

https://forge.rust-lang.org/infra/other-installation-methods.html

```cmd
curl https://sh.rustup.rs -sSf | sh
. ~/.bashrc
rustc --version
```
```cmd
rustup toolchain install 1.51.0
```

2. Install required native libraries and utilities:

```cmd
sudo apt-get update
```
```cmd
sudo apt-get install -y \
   build-essential \
   pkg-config \
   cmake \
   libssl-dev \
   libsqlite3-dev \
   libzmq3-dev \
   libncursesw5-dev
```
만일 위 명령어가 실패하면 아래 처럼 하나씩 실행하자
```cmd
sudo apt-get install -y build-essential
```
```cmd
sudo apt-get install -y pkg-config
```
```cmd
sudo apt-get install -y cmake
```
```cmd
sudo apt-get install -y libssl-dev
```
```cmd
sudo apt-get install -y libsqlite3-dev
```
```cmd
sudo apt-get install -y libzmq3-dev
```
```cmd
sudo apt-get install -y libncursesw5-dev
```

3. libindy requires the modern 1.0.14 version of libsodium but Ubuntu 16.04 does not support installation it's from apt repository. Because of this, it requires to build and install libsodium from source:

```cmd
cd /tmp
curl https://download.libsodium.org/libsodium/releases/libsodium-1.0.18.tar.gz | tar -xz
cd /tmp/libsodium-1.0.18 
./configure --disable-shared
sudo make
sudo make install 
```

 - optional

```cmd
cd ..
sudo rm -rf /tmp/libsodium-1.0.18
```

4. Build libindy

```cmd
cd [indy_sdk]/libindy/
cargo build
cd target/debug
sudo cp libindy.so /usr/local/lib/
sudo ldconfig
```

`.bashrc` 에 다음을 추가
```
vi ~/.bashrc
LD_LIBRARY_PATH=/usr/local/lib/libindy.so
```

환경변수 적용
```cmd
. ~/.bashrc
```


5. Test

 
 - `Getting Started` 실행
```cmd
cd [indy_sdk]/samples/python
sudo apt-get install python3-pip
sudo pip3 install pip --upgrade
pip -V
pip3 -V
pip3 install python3-indy
python3 -m src.getting_started
```