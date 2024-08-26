# Databricks notebook source
# MAGIC %sql
# MAGIC use dlt

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists dev_bronze_src1 ;
# MAGIC create database if not exists dev_silver_domain1 ;
# MAGIC create database if not exists dev_gold

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists qa_bronze_src1 ;
# MAGIC create database if not exists qa_silver_domain1 ;
# MAGIC create database if not exists qa_gold

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists prod_bronze_src1 ;
# MAGIC create database if not exists prod_silver_domain1 ;
# MAGIC create database if not exists prd_gold
