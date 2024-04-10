from pyspark.sql import SparkSession
from utils.schemas import schemas
from utils.sw_class import StarWarsApi
  
spark = SparkSession.builder.master("local[*]").appName("Desafio_Globo_curated").getOrCreate()

for column_name in schemas.keys():
  run_curated = StarWarsApi(column_name, spark)
  run_curated.raw_to_curated(schemas)