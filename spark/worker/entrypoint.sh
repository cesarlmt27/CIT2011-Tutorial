#!/bin/bash

# https://spark.apache.org/docs/latest/spark-standalone.html

exec ./sbin/start-worker.sh spark://spark-driver:7077 &

sleep infinity