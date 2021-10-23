# Ah-hah

Sovrin Foundation은 비영리 단체

Sovrin은 블록체인 스타트업 기업인 Evernym이 기원임

Indy는 Evernym으로 개발됨

Evernym은 2013년 설립된 블록체인 신원인증 솔루션 스타트업으로 미국 영국 기반의 회사이며 미국 국토안보부의 지원을 받음.

Sovrin Foundation에 소속되어 있음



<br><br><br><br>
<hr>

# TASK!


## 1. 지갑 decrypt하기
## 2. 지갑에 Private Key 얻어오기


<br><br><br><br>
<hr>

# DEMO

```cmd
git clone https://github.com/hyperledger-archives/education indy-demo
cd education/LFS171x/indy-material/nodejs
```

```cmd
# Maybe Need
sudo apt install pip
pip install --upgrade pip
```

 - `pool.dockerfile` 수정

`RUN pip install --upgrade -vv setuptools`가 추가됨

```dockerfile
FROM bcgovimages/von-image:py35-1.6-8

USER indy

RUN pip install --upgrade -vv setuptools

RUN pip install --no-cache-dir aiosqlite~=0.6.0

ENV RUST_LOG ${RUST_LOG:-warning}

RUN mkdir -p \
        $HOME/ledger/sandbox/data \
        $HOME/log \
        $HOME/.indy-cli/networks \
        $HOME/.indy_client/wallet && \
    chmod -R ug+rw $HOME/log $HOME/ledger $HOME/.indy-cli $HOME/.indy_client

ADD --chown=indy:indy indy_config.py /etc/indy/

ADD --chown=indy:indy . $HOME

RUN chmod uga+x scripts/* bin/*
```

```cmd
./manage build
./manage up
```

- 종료

```cmd
./manage down
```

#### * 데모 테스트

As the demo starts up, a series of 4 digit numbers will appear above the terminal. Those are the exposed ports of the running containers and the numbers are links to start a Browser tab accessing that port.

To go through the demonstration, click the following numbers from the list:

 - 3000 for Alice
 - 3002 for Faber College
 - 3003 for Acme Corporation

If you click the links before the Agent is active, you might get a Connection reset by peer error messages. Monitor the logs and wait longer and then try again.

The instructions for walking through the demonstration script are here: Agent Demo Script

You can also open in a browser a Blockchain Ledger Explorer:

 - 9000

Although we don't talk about them in the demo overview, there are two additional Agents running that you can access:

 - 3001 for Bob
 - 3004 for Thrift Bank

<br><br><br><br><br><br>

# indy-sdk node.js sample

https://github.com/hyperledger/indy-sdk/tree/master/samples/nodejs

8버전이 아니면 node-gyp rebuild 에러가 난다.

다운그레이드 시켜주자

 - node 8.17.0
 - npm 6.13.4


```cmd
. ~/.bashrc
cd [indy_sdk]/samples/nodejs
```
```cmd
sudo npm install -g n
sudo n install 8.17.0
//n을 적용하면서 최신버전이 안보인다..
//최신 LTS버전도 같이 설치해주자.
sudo n install 14.17.3
```
```cmd
//최신 버전을 설치하니 npm 버전이 적용이 안된다.
//원래 설치되어 있는 /usr/bin/의 nodejs를 삭제해주자
sudo apt-get purge --auto-remove nodejs
sudo n //8버전 선택
node -v
npm -v
npm install
npm run start
```

#### 파이썬 업그레이드 to 3.8

```
sudo apt install python3.8 -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 
python3 -V
<!-- sudo update-alternatives --config python3 -->
python3 -m pip install pip
pip3 -V
```