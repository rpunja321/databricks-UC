# Databricks notebook source
# MAGIC %sql
# MAGIC create database if not exists dlt.dev_bronze_src1 ;
# MAGIC create database if not exists dlt.dev_silver_domain1 ;
# MAGIC create database if not exists dlt.dev_gold

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists dlt.qa_bronze_src1 ;
# MAGIC create database if not exists dlt.qa_silver_domain1 ;
# MAGIC create database if not exists dlt.qa_gold

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists dlt.prod_bronze_src1 ;
# MAGIC create database if not exists dlt.prod_silver_domain1 ;
# MAGIC create database if not exists dlt.prd_gold
