from unittest.mock import patch
from arena import Arena
import io
import pytest

# Test valid inputs
@patch('builtins.input', return_value='')
@patch('sys.stdout', new_callable=io.StringIO)
def test_battle_valid_inputs(mock_stdout, mock_input):
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander']
    p2_pokemon_names = ['Pikachu', 'Squirtle']
    arena = Arena()
    arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    expected_output = "Player one takes out Bulbasaur!\nPlayer two takes out Pikachu!\nPlayer 2's Pikachu goes first!\nHe deals 12.9 damage!\nBulbasaur has 32.1 HP left\nPlayer 1's Bulbasaur retaliates!\nHe deals 11.9 damage!\nPikachu has 23.1 HP left\n\nPlayer 2's Pikachu goes first!\nHe deals 12.9 damage!\nBulbasaur has 19.1 HP left\nPlayer 1's Bulbasaur retaliates!\nHe deals 11.9 damage!\nPikachu has 11.1 HP left\n\nPlayer 2's Pikachu goes first!\nHe deals 12.9 damage!\nBulbasaur has 6.1 HP left\nPlayer 1's Bulbasaur retaliates!\nHe deals 11.9 damage!\nPikachu has fainted. 1 Pokemon left for Player 2.\nPlayer 2 takes out his next pokemon: Squirtle!\n\nPlayer 1's Bulbasaur goes first!\nHe deals 9.1 damage!\nSquirtle has 34.9 HP left\nPlayer 2's Squirtle retaliates!\nHe deals 10.6 damage!\nBulbasaur has fainted. 1 Pokemon left for Player 1.\nPlayer 1 takes out his next pokemon: Charmander!\n\nPlayer 1's Charmander goes first!\nHe deals 10.1 damage!\nSquirtle has 23.9 HP left\nPlayer 2's Squirtle retaliates!\nHe deals 11.2 damage!\nCharmander has 27.8 HP left\n\nPlayer 1's Charmander goes first!\nHe deals 10.1 damage!\nSquirtle has 12.9 HP left\nPlayer 2's Squirtle retaliates!\nHe deals 11.2 damage!\nCharmander has 15.8 HP left\n\nPlayer 1's Charmander goes first!\nHe deals 10.1 damage!\nSquirtle has 1.9 HP left\nPlayer 2's Squirtle retaliates!\nHe deals 11.2 damage!\nCharmander has 3.8 HP left\n\nPlayer 1's Charmander goes first!\nHe deals 10.1 damage!\nCharmander has defeted the opponent's last pokemon! Player 1 has won!\n\n"
    assert mock_stdout.getvalue() == expected_output

# Test stalemate
@patch('builtins.input', return_value='')
@patch('sys.stdout', new_callable=io.StringIO)
def test_battle_valid_inputs_stalemate(mock_stdout, mock_input):
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 1, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 1, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur']
    p2_pokemon_names = ['Pikachu']
    arena = Arena()
    arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    expected_output = "Player one takes out Bulbasaur!\nPlayer two takes out Pikachu!\nPlayer 2's Pikachu goes first!\nHe deals 0.0 damage!\nBulbasaur has 45.0 HP left\nPlayer 1's Bulbasaur retaliates!\nHe deals 0.0 damage!\nPikachu has 35.0 HP left\nStalemate! No one wins!\n"
    assert mock_stdout.getvalue() == expected_output



# Test invalid names
def test_battle_invalid_names():
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander', 'Squirtle']
    p2_pokemon_names = ['Pikachu', 'Jigglypuff', 'InvalidName']
    arena = Arena()
    try:
        arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    except ValueError as e:
        assert str(e) == "'InvalidName' is not in the pokemon list."

# Test invalid list (missing an attack column)
def test_battle_invalid_list_missing_column():
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander', 'Squirtle']
    p2_pokemon_names = ['Pikachu', 'Jigglypuff', 'Psyduck']
    arena = Arena()
    try:
        arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    except ValueError as e:
        assert str(e) == "Attack is missing: {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45}"


# Test invalid list (empty values)
def test_battle_invalid_list_empty_values():
    pokemon_list = [
        {'#': 1, 'Name': '', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander', 'Squirtle']
    p2_pokemon_names = ['Pikachu', 'Jigglypuff', 'Psyduck']
    arena = Arena()
    try:
        arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    except ValueError as e:
        assert str(e) == "Name is empty: {'#': 1, 'Name': '', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45}"

# Test invalid list (wrong type)
def test_battle_invalid_list_wrong_type():
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 'IM HUNGRY', 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander', 'Squirtle']
    p2_pokemon_names = ['Pikachu', 'Jigglypuff', 'Psyduck']
    arena = Arena()
    try:
        arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    except ValueError as e:
        assert str(e) == "HP must be an integer: {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 'IM HUNGRY', 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45}"


# Test invalid number of names
def test_battle_invalid_number_of_names():
    pokemon_list = [
        {'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
        {'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
        {'#': 3, 'Name': 'Squirtle', 'Type1': 'Water', 'Type2': 'None', 'Attack': 48, 'Defense': 65, 'HP': 44, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
        {'#': 4, 'Name': 'Pikachu', 'Type1': 'Electric', 'Type2': 'None', 'Attack': 55, 'Defense': 40, 'HP': 35, 'Sp. Atk': 50, 'Sp. Def': 50, 'Speed': 90},
        {'#': 5, 'Name': 'Jigglypuff', 'Type1': 'Normal', 'Type2': 'Fairy', 'Attack': 45, 'Defense': 20, 'HP': 115, 'Sp. Atk': 45, 'Sp. Def': 25, 'Speed': 20},
        {'#': 6, 'Name': 'Psyduck', 'Type1': 'Water', 'Type2': 'None', 'Attack': 52, 'Defense': 48, 'HP': 50, 'Sp. Atk': 65, 'Sp. Def': 50, 'Speed': 55}
    ]
    p1_pokemon_names = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Jigglypuff', 'Psyduck', 'InvalidName']
    p2_pokemon_names = ['Pikachu', 'Jigglypuff', 'Psyduck', 'Bulbasaur', 'Charmander', 'Squirtle', 'InvalidName']
    arena = Arena()
    try:
        arena.battle(pokemon_list, p1_pokemon_names, p2_pokemon_names)
    except ValueError as e:
        assert str(e) == "Both players must have between 1 and 6 pokemon."


@patch('builtins.input', return_value='')
@patch('sys.stdout', new_callable=io.StringIO)
def test_attack_round_print(mock_stdout, mock_input):
    attacker = [{'#': 1, 'Name': 'Bulbasaur', 'Type1': 'Grass', 'Type2': 'Poison', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45}]
    defender = [{'#': 2, 'Name': 'Charmander', 'Type1': 'Fire', 'Type2': 'None', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65}]
    lost1 = 0
    lost2 = 0
    playerName1 = 'Player 1'
    playerName2 = 'Player 2'
    Arena.attackRound(attacker, defender, lost1, lost2, playerName1, playerName2)
    expected_output = "Player 1's Bulbasaur goes first!\nHe deals 11.6 damage!\nCharmander has 27.4 HP left\nPlayer 2's Charmander retaliates!\nHe deals 11.9 damage!\nBulbasaur has 33.1 HP left\n"
    assert mock_stdout.getvalue() == expected_output

