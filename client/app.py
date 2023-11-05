from pyspark.sql import SparkSession

spark = SparkSession.builder.remote("sc://spark-driver").appName("app").getOrCreate()

logFile = "/app/test.txt"  # Archivo en el servidor de Spark
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()