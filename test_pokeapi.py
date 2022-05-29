import unittest
from resources import PokeAPI

class TestPokeAPI(unittest.TestCase):
    
    def test_mapping_first_pokemon(self):
        api = PokeAPI()
        response = api.get_all_pokemons(limit=1)
        
        expected = {
            "name": "bulbasaur",
            "more_details_url": "https://pokeapi.co/api/v2/pokemon/1/",
            "weight": 69,
            "abilities": ['overgrow', 'chlorophyll'],
            "pokemon_type": ['grass', 'poison']
        }

        self.assertDictEqual(expected, response["data"][0].__dict__)

if __name__ == '__main__':
    unittest.main()
