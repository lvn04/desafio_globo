# Desafio Globo

## Sumário

  - [Sumário](#sumário)
  - [Envolvidos](#envolvidos)
  - [Resumo do Projeto](#resumo-do-projeto)
  - [Layers](#layers)
  - [Catálogo de Dados](#catálogo-de-dados)
  - [Output Analytics](#output-analytics)
  - [Links Úteis](#links-úteis)


&nbsp;
## Envolvidos
| Nome                           | Papel               |
|--------------------------------|---------------------|
| Lucas Viana                    | Engenheiro de dados | 


&nbsp;
## Resumo do Projeto

Projeto destinado a avaliar as habilidades técnicas de um engenheiro de dados em relação a:
* Capacidade de consumir dados de uma API pública
* Capacidade de realizar análises exploratórias de dados
* Capacidade de gerar insights a partir de dados


&nbsp;
## Layers

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
| Coluna         | Tipo de Dados |
| -------------- | ------------- |
| birth_year     | string        |
| created        | timestamp     |
| edited         | timestamp     |
| eye_color      | string        |
| films          | array[string] |
| gender         | string        |
| hair_color     | string        |
| height         | string        |
| homeworld      | string        |
| mass           | string        |
| name           | string        |
| skin_color     | string        |
| species        | array[string] |
| starships      | array[string] |
| url            | string        |
| vehicles       | array[string] |


#### planets
| Coluna            | Tipo de Dados |
| ----------------- | ------------- |
| climate           | string        |
| created           | timestamp     |
| diameter          | string        |
| edited            | timestamp     |
| films             | array[string] |
| gravity           | string        |
| name              | string        |
| orbital_period    | string        |
| population        | string        |
| residents         | array[string] |
| rotation_period   | string        |
| surface_water     | string        |
| terrain           | string        |
| url               | string        |


#### films
| Coluna           | Tipo de Dados |
| ---------------- | ------------- |
| characters       | array[string] |
| created          | timestamp     |
| director         | string        |
| edited           | timestamp     |
| episode_id       | integer       |
| opening_crawl    | string        |
| planets          | array[string] |
| producer         | string        |
| release_date     | string        |
| species          | array[string] |
| starships        | array[string] |
| title            | string        |
| url              | string        |
| vehicles         | array[string] |
 

#### species
| Coluna            | Tipo de Dados |
| ----------------- | ------------- |
| average_height    | string        |
| average_lifespan  | string        |
| classification    | string        |
| created           | timestamp     |
| designation       | string        |
| edited            | timestamp     |
| eye_colors        | string        |
| films             | array[string] |
| hair_colors       | string        |
| homeworld         | string        |
| language          | string        |
| name              | string        |
| people            | array[string] |
| skin_colors       | string        |
| url               | string        |


#### vehicles
| Coluna                    | Tipo de Dados |
| ------------------------- | ------------- |
| cargo_capacity            | string        |
| consumables               | string        |
| cost_in_credits           | string        |
| created                   | timestamp     |
| crew                      | string        |
| edited                    | timestamp     |
| films                     | array[string] |
| length                    | string        |
| manufacturer              | string        |
| max_atmosphering_speed    | string        |
| model                     | string        |
| name                      | string        |
| passengers                | string        |
| pilots                    | array[string] |
| url                       | string        |
| vehicle_class             | string        |

 

#### starships
| Coluna                    | Tipo de Dados |
| ------------------------- | ------------- |
| MGLT                      | string        |
| cargo_capacity            | string        |
| consumables               | string        |
| cost_in_credits           | string        |
| created                   | timestamp     |
| crew                      | string        |
| edited                    | timestamp     |
| films                     | array[string] |
| hyperdrive_rating         | string        |
| length                    | string        |
| manufacturer              | string        |
| max_atmosphering_speed    | string        |
| model                     | string        |
| name                      | string        |
| passengers                | string        |
| pilots                    | array[string] |
| starship_class            | string        |
| url                       | string        |


&nbsp;
## Output Analytics

* Abaixo output dos insights da camada analytics.

#### insight_1
| name           | qtd_filmes |
| -------------- | ---------- |
| Obi-Wan Kenobi | 6          |
| R2-D2          | 6          |
| C-3PO          | 6          |
| Palpatine      | 5          |
| Yoda           | 5          |
| Luke Skywalker | 4          |
| Darth Vader    | 4          |
| Leia Organa    | 4          |
| Chewbacca      | 4          |
| Han Solo       | 3          |


#### insight_2
| name      | climate     |
| --------- | ----------- |
| Tatooine  | arid        |
| Trandosha | arid        |
| Socorro   | arid        |
| Sullust   | superheated |



#### insight_3
| episode_id | title                  | name_species    | qtd_personagens |
| ---------- | ---------------------- | --------------- | --------------- |
| 1          | The Phantom Menace     | unknown species | 10              |
| 1          | The Phantom Menace     | Gungan          | 3               |
| 1          | The Phantom Menace     | Zabrak          | 2               |
| 1          | The Phantom Menace     | Droid           | 2               |
| 1          | The Phantom Menace     | Xexto           | 1               |
| 1          | The Phantom Menace     | Quermian        | 1               |
| 1          | The Phantom Menace     | Toong           | 1               |
| 1          | The Phantom Menace     | Twi'lek         | 1               |
| 1          | The Phantom Menace     | Vulptereen      | 1               |
| 1          | The Phantom Menace     | Yoda's species  | 1               |
| 1          | The Phantom Menace     | Tholothian      | 1               |
| 1          | The Phantom Menace     | Aleena          | 1               |
| 1          | The Phantom Menace     | Chagrian        | 1               |
| 1          | The Phantom Menace     | Cerean          | 1               |
| 1          | The Phantom Menace     | Hutt            | 1               |
| 1          | The Phantom Menace     | Toydarian       | 1               |
| 1          | The Phantom Menace     | Neimodian       | 1               |
| 1          | The Phantom Menace     | Dug             | 1               |
| 1          | The Phantom Menace     | Kel Dor         | 1               |
| 1          | The Phantom Menace     | Iktotchi        | 1               |
| 1          | The Phantom Menace     | Nautolan        | 1               |
| 2          | Attack of the Clones   | unknown species | 15              |
| 2          | Attack of the Clones   | Human           | 4               |
| 2          | Attack of the Clones   | Droid           | 2               |
| 2          | Attack of the Clones   | Kaminoan        | 2               |
| 2          | Attack of the Clones   | Mirialan        | 2               |
| 2          | Attack of the Clones   | Nautolan        | 1               |
| 2          | Attack of the Clones   | Geonosian       | 1               |
| 2          | Attack of the Clones   | Togruta         | 1               |
| 2          | Attack of the Clones   | Cerean          | 1               |
| 2          | Attack of the Clones   | Twi'lek         | 1               |
| 2          | Attack of the Clones   | Neimodian       | 1               |
| 2          | Attack of the Clones   | Clawdite        | 1               |
| 2          | Attack of the Clones   | Toydarian       | 1               |
| 2          | Attack of the Clones   | Chagrian        | 1               |
| 2          | Attack of the Clones   | Skakoan         | 1               |
| 2          | Attack of the Clones   | Kel Dor         | 1               |
| 2          | Attack of the Clones   | Gungan          | 1               |
| 2          | Attack of the Clones   | Muun            | 1               |
| 2          | Attack of the Clones   | Besalisk        | 1               |
| 2          | Attack of the Clones   | Yoda's species  | 1               |
| 3          | Revenge of the Sith    | unknown species | 14              |
| 3          | Revenge of the Sith    | Droid           | 2               |
| 3          | Revenge of the Sith    | Human           | 2               |
| 3          | Revenge of the Sith    | Wookie          | 2               |
| 3          | Revenge of the Sith    | Kel Dor         | 1               |
| 3          | Revenge of the Sith    | Neimodian       | 1               |
| 3          | Revenge of the Sith    | Nautolan        | 1               |
| 3          | Revenge of the Sith    | Twi'lek         | 1               |
| 3          | Revenge of the Sith    | Pau'an          | 1               |
| 3          | Revenge of the Sith    | Kaleesh         | 1               |
| 3          | Revenge of the Sith    | Tholothian      | 1               |
| 3          | Revenge of the Sith    | Yoda's species  | 1               |
| 3          | Revenge of the Sith    | Mirialan        | 1               |
| 3          | Revenge of the Sith    | Iktotchi        | 1               |
| 3          | Revenge of the Sith    | Geonosian       | 1               |
| 3          | Revenge of the Sith    | Zabrak          | 1               |
| 3          | Revenge of the Sith    | Cerean          | 1               |
| 3          | Revenge of the Sith    | Togruta         | 1               |
| 4          | A New Hope             | unknown species | 12              |
| 4          | A New Hope             | Droid           | 3               |
| 4          | A New Hope             | Hutt            | 1               |
| 4          | A New Hope             | Rodian          | 1               |
| 4          | A New Hope             | Wookie          | 1               |
| 5          | The Empire Strikes Back| unknown species | 10              |
| 5          | The Empire Strikes Back| Droid           | 3               |
| 5          | The Empire Strikes Back| Trandoshan      | 1               |
| 5          | The Empire Strikes Back| Yoda's species  | 1               |
| 5          | The Empire Strikes Back| Wookie          | 1               |
| 6          | Return of the Jedi     | unknown species | 11              |
| 6          | Return of the Jedi     | Droid           | 2               |
| 6          | Return of the Jedi     | Mon Calamari    | 1               |
| 6          | Return of the Jedi     | Hutt            | 1               |
| 6          | Return of the Jedi     | Sullustan       | 1               |
| 6          | Return of the Jedi     | Twi'lek         | 1               |
|


## Links úteis e considerações

* Os dados estão armazenados localmente no repositório, porém o ideal seria armazena-los em um banco de dados ou storage cloud, aqui estamos realizando apenas uma representação.

- [Link para representação do fluxo feito no Google Collaboratory](https://colab.research.google.com/drive/1m_5sQkZAiOr4orXY8sc0LRmU1peJpLEW?usp=sharing)
