import pytest
from readerApp import PokemonReader

@pytest.fixture
def pokemon_reader():
    return PokemonReader('test_pokemon.csv')

def test_pokemon_reader_load_pokemon(pokemon_reader):
    assert len(pokemon_reader.pokemon_list) == 3
    assert pokemon_reader.pokemon_list[0]['Name'] == 'Bulbasaur'
    assert pokemon_reader.pokemon_list[1]['Name'] == 'Charmander'
    assert pokemon_reader.pokemon_list[2]['Name'] == 'Squirtle'