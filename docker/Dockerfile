FROM ubuntu:20.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor University, Language Technologies Unit

LABEL maintainer="techiaith"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt update -q \
 && apt install -y -qq tzdata bash build-essential git curl wget software-properties-common \
    vim ca-certificates libffi-dev libssl-dev libsndfile1 libbz2-dev liblzma-dev locales \
    libboost-all-dev libboost-tools-dev libboost-thread-dev cmake  \
    python python3 python3-pip python3-setuptools python3-dev curl zip zlib1g-dev vim \
    ffmpeg sox alsa-utils \
 && python3 -m pip install --upgrade pip

RUN mkdir -p /code

WORKDIR /code

COPY src/python/requirements.txt /code
RUN pip3 install -r requirements.txt 

COPY src /code
