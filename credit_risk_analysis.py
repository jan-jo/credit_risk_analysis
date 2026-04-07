from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, avg

# Create Spark Session
spark = SparkSession.builder \
    .appName("GermanCreditRiskAnalysis") \
    .getOrCreate()

print(" Spark Session Created")

# Load Dataset
df = spark.read.csv(
    "data/german_credit_dataset.csv",
    header=True,
    inferSchema=True
)

print(" Dataset Loaded")

df.printSchema()
df.show(5)
#  Data Exploration
print("Basic Statistics")
df.describe().show()
# missing values check
print(" Basic Statistics")
df.describe().show()
#credit risk domain analysis
df.groupBy("Job") \
  .agg(avg("Credit amount").alias("avg_credit")) \
  .show()
#avreage credit amount by housing type
df.groupBy("Housing") \
  .agg(avg("Credit amount").alias("avg_credit")) \
  .show()
#credit duration analysis
df.groupBy("Duration") \
  .count() \
  .orderBy("Duration") \
  .show()
#spark sql
df.createOrReplaceTempView("credit_data")

spark.sql("""
SELECT Purpose, AVG(`Credit amount`) AS avg_credit
FROM credit_data
GROUP BY Purpose
ORDER BY avg_credit DESC
""").show()
#ruke-based credit rsik segmentation
df = df.withColumn(
    "RiskLevel",
    when((col("Credit amount") > 5000) & (col("Duration") > 24), "High Risk")
    .when((col("Credit amount") > 2000) & (col("Duration") > 12), "Medium Risk")
    .otherwise("Low Risk")
)

df.groupBy("RiskLevel").count().show()

df.groupBy("Sex", "RiskLevel").count().show()
df.groupBy("Housing", "RiskLevel").count().show()

df.write.mode("overwrite").csv("output/credit_risk_analysis_results")
print(" Results saved")
