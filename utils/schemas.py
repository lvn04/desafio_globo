from pyspark.sql.types import (StructType, StructField, StringType, TimestampType, ArrayType, IntegerType)

people = StructType([
        StructField("birth_year", StringType(), True),
        StructField("created", TimestampType(), True),
        StructField("edited", TimestampType(), True),
        StructField("eye_color", StringType(), True),
        StructField("films", ArrayType(StringType()), True),
        StructField("gender", StringType(), True),
        StructField("hair_color", StringType(), True),
        StructField("height", StringType(), True),
        StructField("homeworld", StringType(), True),
        StructField("mass", StringType(), True),
        StructField("name", StringType(), True),
        StructField("skin_color", StringType(), True),
        StructField("species", ArrayType(StringType()), True),  
        StructField("starships", ArrayType(StringType()), True),
        StructField("url", StringType(), True),
        StructField("vehicles", ArrayType(StringType()), True),
    ])

planets = StructType([
    StructField("climate", StringType(), True),
    StructField("created", TimestampType(), True),
    StructField("diameter", StringType(), True),
    StructField("edited", TimestampType(), True),
    StructField("films", ArrayType(StringType()), True),
    StructField("gravity", StringType(), True), 
    StructField("name", StringType(), True),
    StructField("orbital_period", StringType(), True),
    StructField("population", StringType(), True),
    StructField("residents", ArrayType(StringType()), True),
    StructField("rotation_period", StringType(), True),
    StructField("surface_water", StringType(), True), 
    StructField("terrain", StringType(), True),
    StructField("url", StringType(), True),
])

films = StructType([
    StructField("characters", ArrayType(StringType()), True),
    StructField("created", TimestampType(), True),
    StructField("director", StringType(), True),
    StructField("edited", TimestampType(), True),
    StructField("episode_id", IntegerType(), True),
    StructField("opening_crawl", StringType(), True),
    StructField("planets", ArrayType(StringType()), True),
    StructField("producer", StringType(), True),
    StructField("release_date", StringType(), True),
    StructField("species", ArrayType(StringType()), True),
    StructField("starships", ArrayType(StringType()), True),
    StructField("title", StringType(), True),
    StructField("url", StringType(), True),
    StructField("vehicles", ArrayType(StringType()), True),
])

species = StructType([
    StructField("average_height", StringType(), True),
    StructField("average_lifespan", StringType(), True),
    StructField("classification", StringType(), True),
    StructField("created", TimestampType(), True),
    StructField("designation", StringType(), True),
    StructField("edited", TimestampType(), True),
    StructField("eye_colors", StringType(), True),
    StructField("films", ArrayType(StringType()), True),
    StructField("hair_colors", StringType(), True),
    StructField("homeworld", StringType(), True),
    StructField("language", StringType(), True),
    StructField("name", StringType(), True),
    StructField("people", ArrayType(StringType()), True),
    StructField("skin_colors", StringType(), True),
    StructField("url", StringType(), True),
])

vehicles = StructType([
    StructField("cargo_capacity", StringType(), True),
    StructField("consumables", StringType(), True),
    StructField("cost_in_credits", StringType(), True),
    StructField("created", TimestampType(), True),
    StructField("crew", StringType(), True),
    StructField("edited", TimestampType(), True),
    StructField("films", ArrayType(StringType()), True),
    StructField("length", StringType(), True),
    StructField("manufacturer", StringType(), True),
    StructField("max_atmosphering_speed", StringType(), True),
    StructField("model", StringType(), True),
    StructField("name", StringType(), True),
    StructField("passengers", StringType(), True),
    StructField("pilots", ArrayType(StringType()), True),
    StructField("url", StringType(), True),
    StructField("vehicle_class", StringType(), True),
])

starships =  StructType([
    StructField("MGLT", StringType(), True),
    StructField("cargo_capacity", StringType(), True),
    StructField("consumables", StringType(), True),
    StructField("cost_in_credits", StringType(), True),
    StructField("created", TimestampType(), True),
    StructField("crew", StringType(), True),
    StructField("edited", TimestampType(), True),
    StructField("films", ArrayType(StringType()), True),
    StructField("hyperdrive_rating", StringType(), True),
    StructField("length", StringType(), True),
    StructField("manufacturer", StringType(), True),
    StructField("max_atmosphering_speed", StringType(), True),
    StructField("model", StringType(), True),
    StructField("name", StringType(), True),
    StructField("passengers", StringType(), True),
    StructField("pilots", ArrayType(StringType()), True),
    StructField("starship_class", StringType(), True),
    StructField("url", StringType(), True),
])

schemas = {"people": people,
           "planets": planets,
           "films": films,
           "species": species,
           "vehicles": vehicles,
           "starships": starships,
           }