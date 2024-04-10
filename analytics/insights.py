from utils.sw_class import StarWarsApi
from utils.assistant_config import explode_column
from pyspark.sql.functions import explode, count, col, lower



def insight_1(spark_sc):
    """
    Funcao para analise dos dados que retorna os 
    personagens que apareceram em mais filmes.
    """
    df = StarWarsApi("people", spark_sc)
    people = df.get_table("curated")
    people = people.select("name",explode("films").alias("films"))
    df = people.groupBy("name").agg(count("films").alias('qtd_filmes')).orderBy(col("qtd_filmes").desc())

    return df

def insight_2(spark_sc):
    """
    Funcao para analise dos dados que retorna os 
    planetas mais quentes do universo de Star Wars.
    """
    df = StarWarsApi("planets", spark_sc)
    planets = df.get_table("curated")
    df = (planets.filter(lower(col("climate")).isin("arid","superheated"))
          .select("name", "climate")
          )

    return df

def insight_3(spark_sc):
    """
    Funcao para analise dos dados que retorna a quantidade
    personagens por especie que aparece em cada filme.
    """

    df_especies = StarWarsApi("species", spark_sc)
    species = df_especies.get_table("curated")

    df_people = StarWarsApi("people", spark_sc)
    people = df_people.get_table("curated")

    df_films = StarWarsApi("films", spark_sc)
    films = df_films.get_table("curated")

    ex_species = explode_column(species, "people")
    df_join = people.join(ex_species, people.url == ex_species.people, "left").select(species.name.alias("name_species"), people.films, people.name.alias("name_people"))

    ex_df_join = explode_column(df_join, "films")
    df_final = (ex_df_join.join(films, ex_df_join.films == films.url, "left")
                .groupBy(films.episode_id, films.title, ex_df_join.name_species)
                .agg(count(col("name_people")).alias("qtd_personagens"))
                )
    df = df_final.orderBy(col("episode_id").asc(), col("qtd_personagens").desc())

    return df