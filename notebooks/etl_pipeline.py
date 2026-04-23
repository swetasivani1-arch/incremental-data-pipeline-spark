# Simulated ETL pipeline using PySpark

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

# Read data
df = spark.read.csv("/input/customer_data.csv", header=True)

# Basic transformation
df_clean = df.dropDuplicates(["customer_id"])

# Write to silver layer
df_clean.write.mode("overwrite").saveAsTable("customer_silver")
