from pyspark.sql import SparkSession


query = """ 
"""

def transform(spark):
    pass

def main():
    spark = SparkSession.builder \ 
    .master("local") \
    .appName("main app") \
    .getOrCreate()

    output_df = transform(spark)

    output_df.write.mode("overwrite").insertInto("players_scd")
    