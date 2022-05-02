from pyspark.sql import SparkSession

logFile = "README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("project2").getOrCreate()

df1 = spark.read.csv("ml-latest-small/movies.csv")
df1.createOrReplaceTempView("Movies")

df2 = spark.read.csv("ml-latest-small/ratings.csv")
df2.createOrReplaceTempView("Ratings")
sqlDf = spark.sql("SELECT m._c0, m._c2, r._c2 FROM Movies AS m, Ratings as r WHERE m._c0 = r._c1")


sqlDf.show()


spark.stop()