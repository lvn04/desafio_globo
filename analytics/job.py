from analytics.insights import insight_1, insight_2, insight_3
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("Desafio_Globo_analytics").getOrCreate()

df_result_1 = insight_1(spark)
df_result_1.show(10, truncate=False)

df_result_2 = insight_2(spark)
df_result_2.show(10, truncate=False)

df_result_3 = insight_3(spark)
df_result_3.show(100, truncate=False)