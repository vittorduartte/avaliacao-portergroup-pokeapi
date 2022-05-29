import unittest
from resources import PokeAPI
from models import Pokemon

class TestPokeAPI(unittest.TestCase):
    
    def test_mapping_first_pokemon(self):
        api = PokeAPI()
        api.build_pokemon_list(limit=1)
        data = api.get_pokemon_data()
        expected = Pokemon(name='bulbasaur', more_details_url='https://pokeapi.co/api/v2/pokemon/1/', weight=69, abilities=['overgrow', 'chlorophyll'], pokemon_type=['grass', 'poison'])

        self.assertEqual(expected.__repr__(), data.__repr__())

if __name__ == '__main__':
    unittest.main()
