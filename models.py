
class Pokemon():
    '''
    Classe Pokémon que descreve as informações
    necessárias para a descrição deste objeto
    para a aplicação.

        Attributes:
            name (str): Nome do pokémon
            more_details_url (str): Url de mais informações do pokémon
            weight (float): Informações de peso do pokémon
            abilities (list): Lista de habilidades do pokémon
            pokemon_type (list): Lista de habilidades do pokémon
    '''

    def __init__(self, name: str, more_details_url: str, weight: float, abilities: list, pokemon_type: list):
        self.name = name
        self.more_details_url = more_details_url
        self.weight = weight
        self.abilities = abilities
        self.pokemon_type = pokemon_type

    def __repr__(self):
        return f"Pokemon(name: {self.name}, more_details_url: {self.more_details_url}, weight: {self.weight}, abilities: {self.abilities}, pokemon_type: {self.pokemon_type})"
