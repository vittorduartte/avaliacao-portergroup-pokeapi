import unittest
from resources import PokeAPI
from models import Pokemon


class TestPokeAPI(unittest.TestCase):

    def test_mapping_pokemon_object(self):
        api = PokeAPI()
        api.build_pokemon_list(limit=1)
        data = api.get_pokemon_data()[0]
        expected = Pokemon(name='bulbasaur', more_details_url='https://pokeapi.co/api/v2/pokemon/1/',
                           weight=69, abilities=['overgrow', 'chlorophyll'], pokemon_type=['grass', 'poison'])

        self.assertEqual(expected.__dict__, data.__dict__)

    def test_pokemon_list_return(self):
        api = PokeAPI()
        api.build_pokemon_list(limit=2)
        data = api.get_pokemon_data()

        self.assertTrue(type(data) == list)
        
        for pokemon in data:
            self.assertTrue(type(pokemon) == Pokemon)

if __name__ == '__main__':
    unittest.main()
