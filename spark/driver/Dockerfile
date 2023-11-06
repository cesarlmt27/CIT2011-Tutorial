# https://spark.apache.org/docs/latest/spark-connect-overview.html

FROM ubuntu:jammy

# Establece el directorio de trabajo en /app
WORKDIR /app

COPY . /app

RUN apt update && \
    apt install -y python3 && \
    apt install -y wget && \
    apt install -y curl
RUN apt install -y openjdk-8-jdk
RUN wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
RUN tar -xvf spark-3.5.0-bin-hadoop3.tgz

WORKDIR /app/spark-3.5.0-bin-hadoop3

COPY ./spark-env.sh /app/spark-3.5.0-bin-hadoop3/conf/