#!/bin/bash

# https://spark.apache.org/docs/latest/spark-standalone.html

exec ./sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:3.5.0 &

exec ./sbin/start-master.sh &

sleep infinity