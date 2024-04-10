from pyspark.sql.functions import explode
from pyspark.sql.types import  ArrayType

def explode_column(df, column_join=str):
        """
        Funcao auxiliar destinada a abrir as colunas array para realizacao de join.
        """
        column_array = ""
        normalized_columns = []
        for column in df.columns:
          if column == column_join and isinstance(df.schema[column].dataType, ArrayType):
              column_array = column 
          else:
              normalized_columns.append(column)
        df = df.select(*normalized_columns, explode(column_array).alias(column_array))

        return df