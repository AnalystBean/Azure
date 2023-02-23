from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("").getOrCreate()

df = spark.read.format("csv").option("", True).load(" ")

df = df.filter("").groupBy("").count()

df.write.format("csv").option("", True).save(" ")