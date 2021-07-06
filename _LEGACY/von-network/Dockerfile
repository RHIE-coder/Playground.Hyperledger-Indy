FROM ubuntu:16.04

ARG uid=1000
ARG indy_stream=master

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"
ENV SHELL="/bin/bash"

ENV RUST_LOG=error
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository "ppa:deadsnakes/ppa"

# Install environment
RUN apt-get update -y && apt-get install -y \
    git \
    wget \
    python3.7 \
    python3-pip \
    python-setuptools \
    python3-nacl \
    apt-transport-https \
    ca-certificates \
    build-essential \
    pkg-config \
    cmake \
    libssl-dev \
    libsqlite3-dev \
    libsodium-dev \
    curl

RUN pip3 install -U \
    pip      \
    pipenv  \
    setuptools

# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 68DB5E88
# CE7709D068DB5E88
# RUN echo "deb https://repo.sovrin.org/deb xenial $indy_stream" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 68DB5E88
RUN echo "deb https://repo.sovrin.org/deb xenial master" >> /etc/apt/sources.list
RUN echo "deb https://repo.sovrin.org/sdk/deb xenial stable" >> /etc/apt/sources.list
RUN apt-get update

RUN useradd -ms /bin/bash -u $uid indy

RUN apt-get update -y && apt-get install -y \
    indy-plenum \
    indy-anoncreds \
    indy-node \
    python3-indy-crypto=0.4.5 \
    libindy-crypto=0.4.5 \
    libindy

USER indy
WORKDIR /home/indy

# Install rust toolchain
RUN curl -o rustup https://sh.rustup.rs
RUN chmod +x rustup
RUN ./rustup -y

USER indy
WORKDIR /home/indy

ADD bin/* /usr/local/bin/

RUN awk '{if (index($1, "NETWORK_NAME") != 0) {print("NETWORK_NAME = \"sandbox\"")} else print($0)}' /etc/indy/indy_config.py> /tmp/indy_config.py
RUN mv /tmp/indy_config.py /etc/indy/indy_config.py

ADD --chown=indy:indy . /home/indy

RUN cd server && pipenv install python3-indy==1.3.1-dev-408 von-agent==0.5.2 sanic==0.7.0

USER root
