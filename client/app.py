from pyspark.sql import SparkSession

logFile = "/app/test.txt"  # Should be some file on your system
spark = SparkSession.builder.remote("sc://spark-driver").appName("app").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()