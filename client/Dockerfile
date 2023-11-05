FROM python:3.10.12

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install pyspark[connect] pandas grpcio