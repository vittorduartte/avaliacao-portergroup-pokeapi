# Desafio de Programação - Porter Group

Avaliação técnica da [Porter Group](https://portergroup.com.br/) para a vaga de Desenvolvedor Python Júnior.

## Descrição do projeto

Você foi contratado para desenvolver um script que vai consultar a PokéAPI e listar os 20 primeiros Pokémons. Esta lista deve ser utilizada para preenchimento de uma classe Pokémon, contendo os seguintes atributos:

* Nome;
* Url para acesso aos dados detalhados;
* Peso;
* Habilidades (pode ser uma lista);
* Tipo (pode ser uma lista);
  
Esses dados podem ser apresentados no console.

## Objetivos alcançados:

- [x] Consumir a [PokéAPI](https://pokeapi.co/);
- [x] Criar uma classe Pokémon;
- [x] Um método para buscar os Pokémons na API que retorne os objetos Pokémons criados;
- [x] Um método para imprimir os dados do Pokémon;
- [x] Deve-se utilizar a biblioteca nativa do Python requests para consumir a API.
> **Desclaimer:** o desafio especifica o uso da biblioteca [Python Requests](https://docs.python-requests.org/), no entanto o site com a documentação da biblioteca está indisponível. 

## Como utilizar

### Pokemon (_class_)

A classe Pokemon descreve o tipo as características que um Pokémon possui, que são estas:

- **name** (Nome);
- **more_details_url** (Url);
- **weight** (Peso);
- **abilities** (Habilidades);
- **pokemon_type** (Tipo do pokémon).

### PokeAPI (_class_)

A classe PokeAPI é responsável pela consulta e retorno dos dados requisitados à [PokeAPI](https://pokeapi.co/).

```python
from resources import PokeAPI

api = PokeAPI() #Criar um objeto PokeAPI;
api.build_pokemon_list(limit=5) #Solicitar uma lista de pokemons;
#Por padrão a consulta tem um limite de 20 pokemons e offset 0, o que significa dizer que ela começa do pokemon de índice 0;

data = api.get_pokemon_data() #Solicitar a lista com estes dados;
print(data)
```

## Executando o projeto

1. Verifique suas dependências:

Para execução do projeto é requerido: **> Python3.6** e a biblioteca [**requests**](https://requests.readthedocs.io/en/latest/).

2. Clone o repositório do projeto:

```
git clone https://github.com/vittorduartte/avaliacao-portergroup-pokeapi
cd avaliacao-portergroup-pokeapi
```

3. Instale as bibliotecas necessárias:

```
pip install requests
```

4. Execute o arquivo **main.py**

``` 
python main.py
```

## Bônus: Testes

Para garantir a integridade dos dados que estão sendo processados e dos objetos gerados, alguns testes (confira em **test_pokeapi.py**) foram implementados para garantir que o código estevesse comportando-se como esperado.

Execute os testes com:

```
python test_pokeapi.py
```