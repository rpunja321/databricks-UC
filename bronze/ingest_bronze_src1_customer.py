# Databricks notebook source
# MAGIC %run /Workspace/Users/rpunja@apexsystems.com/dltdemo/_common

# COMMAND ----------

# MAGIC %sql
# MAGIC use dev_bronze_src1

# COMMAND ----------

Customer_files=f'{source}'+"customer/LOAD00000001.csv"


# COMMAND ----------

df = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .load(f'{Customer_files}')

# Write the DataFrame to a Databricks table using Delta format
df.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("customers")
