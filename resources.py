from json import loads
from requests import get
from models import Pokemon


class PokeAPI():
    '''
    Classe responsável pela captura dos dados via API.

        Attributes:
            base_url (str)[Optional]: Base url da API.
    '''

    def __init__(self, base_url: str = "https://pokeapi.co/api/v2/pokemon/"):
        self.base_url = base_url
        self.pokemon_data = []

    def __pokemon_object_mapping(self, pokemon) -> Pokemon:
        '''
        (Private) Método responsável por parsear os dados primários
        e consulta a url individual de mais detalhes, para 
        então mapear os dados para classe.

            Parameters:
                pokemon (dict): Dados primários obtidos dos resultados da consulta de Pokémons

            Returns:
                mapped_data (object): Objeto com os dados mapeados.  
        '''
        try:
            response = get(pokemon["url"])
            more_details = loads(response.text)
            abilities = list(
                map(lambda ability: ability["ability"]["name"], more_details["abilities"]))
            types = list(
                map(lambda type: type["type"]["name"], more_details["types"]))
            kwargs = {
                "name": pokemon["name"],
                "more_details_url": pokemon["url"],
                "weight": more_details["weight"],
                "abilities": abilities,
                "pokemon_type": types
            }

            return Pokemon(**kwargs)
        except Exception as e:
            raise e

    def build_pokemon_list(self, offset: int = 0, limit: int = 20) -> None:
        '''
        Método responsável por recuperar os dados primários 
        individuais dos Pokémons via API e os mapeiam para 
        o método de pokemon mapping.

            Parameters:
                    offset (int): Deslocamento do intervalo de resultados da consulta
                    limit (int): Limite de resultados na consulta

        '''
        try:
            response = get(f'{self.base_url}?offset={offset}&limit={limit}')
            object_response = list(
                map(self.__pokemon_object_mapping, loads(response.text)["results"]))

            self.pokemon_data = object_response
        except Exception as e:
            raise e

    def get_pokemon_data(self) -> list:
        '''
        Método responsável por retornar a lista de pokémons
        gerada a partir da consulta feita na PokeAPI.

            Returns:
                data (list): Lista de objetos Pokémons.
        '''
        return [*self.pokemon_data]
