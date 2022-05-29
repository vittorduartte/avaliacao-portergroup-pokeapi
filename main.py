from resources import PokeAPI

api = PokeAPI()
api.build_pokemon_list() 

data = api.get_pokemon_data()
print(data)