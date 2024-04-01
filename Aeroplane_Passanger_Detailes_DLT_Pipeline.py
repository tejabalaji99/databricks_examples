# Databricks notebook source
# MAGIC %md
# MAGIC #Aeroplane_Passanger_Detailes_DLT_Pipeline

# COMMAND ----------

import dlt

# COMMAND ----------

@dlt.create_table(
comment = 'Customer_Loyalty_History of the Aeroplane ,customer details',
table_properties= {
    "myCompanayPipeline.quality":"bronze",
    "pipelines.autoOptimize.managed":"true"
}

)

def clh_details_bronze():
    return spark.read.csv('dbfs:/FileStore/Aeroplane_data/Customer_Loyalty_History.csv',header=True)

# COMMAND ----------

@dlt.create_table(
comment = 'Customers flight Activity for travelling based details',
table_properties= {
    "myCompanayPipeline.quality":"bronze",
    "pipelines.autoOptimize.managed":"true"
}

)

def cfa_details_bronze():
    return spark.read.csv('dbfs:/FileStore/Aeroplane_data/Customer_Flight_Activity.csv',header=True)

# COMMAND ----------

from pyspark.sql.functions import col

@dlt.create_table(
    comment="Merging the both details of Aeroplane customer details and travelling activity based on Loyality Numbers",
    partition_cols=["Year"],
    table_properties={
        "myCompanyPipeline.quality": "silver",
        "pipelines.autoOptimize.managed": "true"
    }
)
def clh_cla_merge_silver():
    df = dlt.read("clh_details_bronze").alias("a").join(dlt.read("cfa_details_bronze").alias("b"),col('a.Loyalty_Number') == col('b.Loyalty_Number'),"inner").select(col('a.*'), col('b.Points_Accumulated'),col('b.Year'),col('b.Month'))
    enrollments_yearly = df.groupBy('Enrollment_Year').agg(F.count('Loyalty_Number').alias('Total_Enrollments')).orderBy('Enrollment_Year')
    cancellations_yearly = df.groupBy('Cancellation_Year').agg(F.count('Loyalty_Number').alias('Total_Cancellations')).orderBy('Cancellation_Year')
    merged_df = enrollments_yearly.join(cancellations_yearly, enrollments_yearly['Enrollment_Year'] == cancellations_yearly['Cancellation_Year'], "outer")
    return merged_df


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from clh_details_bronze

# COMMAND ----------

# df = df.withColumonRenamed('Posta_ Code','Posta_Code')
# df.printSchema()


# COMMAND ----------

# from pyspark.sql.functions import trim,rtrim,ltrim,col
# for old_col in df.columns:
#     new_col = old_col.replace(" ", " ")
#     df = df.withColumnRenamed(old_col, new_col)

# COMMAND ----------

# df = spark.read.csv('dbfs:/FileStore/Aeroplane_data/Customer_Loyalty_History.csv',header=True)
# display(df)
# df.write.saveAsTable('clh_details_bronze')

# COMMAND ----------

# df1 = spark.read.csv('dbfs:/FileStore/Aeroplane_data/Customer_Flight_Activity.csv',header=True)
# display(df1)
# df1.write.saveAsTable('cfa_details_bronze')

# COMMAND ----------

# df3 = spark.table("clh_details_bronze").alias("a").join(spark.table("cfa_details_bronze").alias("b"),col('a.Loyalty_Number') == col('b.Loyalty_Number'),"inner").select(col('a.*'), col('b.Points_Accumulated'),col('b.Year'),col('b.Month'))
# display(df3)

# COMMAND ----------

# df3 = spark.table("clh_details_bronze").alias("a").join(spark.table("cfa_details_bronze").alias("b"),col('a.Loyalty_Number') == col('b.Loyalty_Number'),"inner").select(col('a.*'), col('b.Points_Accumulated'),col('b.Year'),col('b.Month'))
# display(df3)

# COMMAND ----------

from pyspark.sql.functions import count
enrollments_yearly = df3.groupBy('Enrollment_Year', 'Month').agg(count('Loyalty_Number').alias('Enrollments'))
cancellations_yearly = df3.groupBy('Cancellation_Year', 'Month').agg(count('Loyalty_Number').alias('Cancellations'))
display(enrollments_yearly)
display(cancellations_yearly)


# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql import functions as F
enrollments_yearly = df3.groupBy('Enrollment_Year').agg(F.count('Loyalty_Number').alias('Total_Enrollments')).orderBy('Enrollment_Year')
cancellations_yearly = df3.groupBy('Cancellation_Year').agg(F.count('Loyalty_Number').alias('Total_Cancellations')).orderBy('Cancellation_Year')

joined_df = enrollments_yearly.join(cancellations_yearly, enrollments_yearly['Enrollment_Year'] == cancellations_yearly['Cancellation_Year'], "outer").withColumn("Enrollment_Percentage_Change", (F.col("Total_Enrollments") - F.lag("Total_Enrollments").over(Window.orderBy("Enrollment_Year"))) / F.lag("Total_Enrollments").over(Window.orderBy("Enrollment_Year")) * 100).withColumn("Cancellation_Percentage_Change", (F.col("Total_Cancellations") - F.lag("Total_Cancellations").over(Window.orderBy("Cancellation_Year"))) / F.lag("Total_Cancellations").over(Window.orderBy("Cancellation_Year")) * 100).orderBy('Enrollment_Year')
display(joined_df)


