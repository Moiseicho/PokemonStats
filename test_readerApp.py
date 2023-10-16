import pytest
from readerApp import PokemonReader
from unittest.mock import patch, mock_open

@pytest.fixture
def pokemon_reader():
    with patch('builtins.open', new_callable=mock_open, read_data='Name,Type,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed\nBulbasaur,GrassPoison,318,45,49,49,65,65,45\nCharmander,Fire,309,39,52,43,60,50,65\nSquirtle,Water,314,44,48,65,50,64,43\n'):
        return PokemonReader('test_pokemon.csv')

def test_pokemon_reader_load_pokemon(pokemon_reader):
    assert len(pokemon_reader.pokemon_list) == 3
    assert pokemon_reader.pokemon_list[0]['Name'] == 'Bulbasaur'
    assert pokemon_reader.pokemon_list[1]['Name'] == 'Charmander'
    assert pokemon_reader.pokemon_list[2]['Name'] == 'Squirtle'
        
        
def test_pokemon_reader_invalid_path_mock():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            PokemonReader('invalid_path.csv')
