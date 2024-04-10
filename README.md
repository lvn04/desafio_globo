# Desafio Globo

## Sumário

  - [Sumário](#sumário)
  - [Resumo do Projeto](#resumo-do-projeto)
  - [Orquestração](#orquestração)
  - [Catálogo de Dados](#catálogo-de-dados)
  - [Links Úteis](#links-úteis)


&nbsp;
## Resumo do Projeto

Projeto destinado a avaliar as habilidades técnicas de um engenheiro de dados em relação a:
* Capacidade de consumir dados de uma API pública
* Capacidade de realizar análises exploratórias de dados
* Capacidade de gerar insights a partir de dados

* Os dados estão armazenados localmente no repositório, porém o ideal seria armazena-los em um banco de dados ou storage cloud, aqui estamos realizando apenas uma representação.

* O projeto consiste da seguinte forma:

### RAW_ZONE
* Camada de entrada dos dados, onde após a ingestão, os dados permanecem em seu estado original sem alterações.

### CURATED_ZONE
* Camada de armazenamento dos dados padronizados com limpezas e formatação de schema, a ideia é que os dados dessa camada sejam consumidos para realização de reports analíticos.

### ANALYTICS
* Reports e insights gerados a partir dos dados presentes na camada curated, geralmente aplicando regras de negócio para atender as necessidades dos times analíticos.


&nbsp;
## Catálogo de Dados

### **CURATED**

#### people
 | birth_year | string | 
 | created | timestamp | 
 | edited | timestamp | 
 | eye_color | string | 
 | films | array | 
 |    | element | string | 
 | gender | string | 
 | hair_color | string | 
 | height | string | 
 | homeworld | string | 
 | mass | string | 
 | name | string | 
 | skin_color | string | 
 | species | array | 
 |    | element | string | 
 | starships | array | 
 |    | element | string | 
 | url | string | 
 | vehicles | array | 
 |    | element | string | 

#### planets
 | climate | string | 
 | created | timestamp | 
 | diameter | string | 
 | edited | timestamp | 
 | films | array | 
 |    | element | string | 
 | gravity | string | 
 | name | string | 
 | orbital_period | string | 
 | population | string | 
 | residents | array | 
 |    | element | string | 
 | rotation_period | string | 
 | surface_water | string | 
 | terrain | string | 
 | url | string | 

#### films
 | characters | array | 
 |    | element | string | 
 | created | timestamp | 
 | director | string | 
 | edited | timestamp | 
 | episode_id | integer | 
 | opening_crawl | string | 
 | planets | array | 
 |    | element | string | 
 | producer | string | 
 | release_date | string | 
 | species | array | 
 |    | element | string | 
 | starships | array | 
 |    | element | string | 
 | title | string | 
 | url | string | 
 | vehicles | array | 
 |    | element | string | 

#### species
 | average_height | string | 
 | average_lifespan | string | 
 | classification | string | 
 | created | timestamp | 
 | designation | string | 
 | edited | timestamp | 
 | eye_colors | string | 
 | films | array | 
 |    | element | string | 
 | hair_colors | string | 
 | homeworld | string | 
 | language | string | 
 | name | string | 
 | people | array | 
 |    | element | string | 
 | skin_colors | string | 
 | url | string | 

#### vehicles
 | cargo_capacity | string | 
 | consumables | string | 
 | cost_in_credits | string | 
 | created | timestamp | 
 | crew | string | 
 | edited | timestamp | 
 | films | array | 
 |    | element | string | 
 | length | string | 
 | manufacturer | string | 
 | max_atmosphering_speed | string | 
 | model | string | 
 | name | string | 
 | passengers | string | 
 | pilots | array | 
 |    | element | string | 
 | url | string | 
 | vehicle_class | string | 

#### starships
 | MGLT | string | 
 | cargo_capacity | string | 
 | consumables | string | 
 | cost_in_credits | string | 
 | created | timestamp | 
 | crew | string | 
 | edited | timestamp | 
 | films | array | 
 |    | element | string | 
 | hyperdrive_rating | string | 
 | length | string | 
 | manufacturer | string | 
 | max_atmosphering_speed | string | 
 | model | string | 
 | name | string | 
 | passengers | string | 
 | pilots | array | 
 |    | element | string | 
 | starship_class | string | 
 | url | string | 


## Links Úteis

- [Link para representação do fluxo feito no Google Collaboratory](https://colab.research.google.com/drive/1m_5sQkZAiOr4orXY8sc0LRmU1peJpLEW?usp=sharing)
