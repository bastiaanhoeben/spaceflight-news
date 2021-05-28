FROM ubuntu:latest

MAINTAINER Bastiaan Hoeben

RUN apt-get update -y && apt-get install -y python3.8 python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./code /app/

ENTRYPOINT [ "python3" ]