from pyspark.sql import SparkSession
from utils.schemas import schemas
from utils.sw_class import StarWarsApi

spark = SparkSession.builder.master("local[*]").appName("Desafio_Globo_ingestion").getOrCreate()

for name in schemas.keys():

  run_ingestion = StarWarsApi(name, spark)
  run_ingestion.ingestion_to_raw()