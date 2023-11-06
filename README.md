# Apache Spark - Tutorial

## More information
- [Spark Standalone Mode](https://spark.apache.org/docs/latest/spark-standalone.html).
- [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html).
- [Apache Spark packaged by Bitnami](https://github.com/bitnami/containers/tree/main/bitnami/spark).


## Scale the worker service
```bash
docker compose up --scale spark-worker=3
```


## Launch application on the cluster
```bash
docker compose exec spark-master spark-submit --master spark://spark-master:7077 app/core.py
```