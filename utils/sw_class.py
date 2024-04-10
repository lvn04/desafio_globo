import logging
import os
import requests
import json

class StarWarsApi:

    def __init__(self, table_name=str, spark_sc=None):

        self.local_path = os.getcwd()
        self.table_name = table_name
        self.url = "https://swapi.dev/api/"
        self.spark =  spark_sc
        logging.basicConfig(filename=f'{self.local_path}/log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',  filemode='w')

    def ingestion_to_raw(self):
        """
        Funcao destinada a realizar o processo de consumo dos dados via api e salvar no banco de dados em formato json
        """

        try:
            response = requests.get(self.url)
            if response.status_code == 200:
    
                logging.info(f"Requisição realizada com sucesso Status Code{response.status_code}")
                endpoints = response.json()
                
                
                url_endpoint = endpoints[self.table_name]
                dados = []
                page = url_endpoint
                
                while page != None:
                    json_dados = requests.get(page).json()
                    for result in range(len(json_dados["results"])):
                        dados.append( json_dados["results"][result] )
                    page = json_dados["next"]
            
                with open(f"{self.local_path}/dados/raw_zone/{self.table_name}.json", "w") as file:
                    json.dump(dados, file)
            
            
                logging.info(f"Ingestão da tabela {self.table_name} concluída")
                
            else:
                logging.error(f'Falha na requisição status {response.status_code}.')
                
        except  Exception as e:
            e

    def raw_to_curated(self, schema=dict):
        """
        Funcao destinada a leitura e tratamento simples dos dados e envio para a camada curated.
        """
        try:
          df = self.get_table("raw", schema)
          df = df.na.replace({"N/A": None, "n/a": None})
          df.write.mode("overwrite").parquet(f"{self.local_path}/dados/curated_zone/{self.table_name}/")
          
          logging.info(f"Dados da tabela {self.table_name} disponiveis na camada curated")

        except  Exception as e:
          return e

    def get_table(self, layer=str, schema=None):
        """
        Funcao destinada a ler dados e retornar um dataframe.
        """
        if layer not in ("curated", "raw"):
          raise ValueError(f"Valor invalido para 'layer': {layer}. Valores permitidos: 'curated', 'raw'")

        if layer == "raw":
          if schema is None:
            raise AttributeError(f"Necessario incluir schema da tabela {self.table_name}")
          else:
            df = self.spark.read.schema(schema[self.table_name]).json(f"{self.local_path}/dados/raw_zone/{self.table_name}.json")
          
        if layer == "curated":
          df = self.spark.read.format('parquet').load(f"{self.local_path}/dados/{layer}_zone/{self.table_name}/*")

        return df