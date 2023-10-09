pokemon_list = [
    {'Name': 'Bulbasaur', 'Type': 'Grass', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
    {'Name': 'Charmander', 'Type': 'Fire', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
    {'Name': 'Charizard', 'Type': 'Fire', 'Attack': 84, 'Defense': 78, 'HP': 78, 'Sp. Atk': 109, 'Sp. Def': 85, 'Speed': 100},
    {'Name': 'Charmeleon', 'Type': 'Fire', 'Attack': 64, 'Defense': 58, 'HP': 58, 'Sp. Atk': 80, 'Sp. Def': 65, 'Speed': 80},
    {'Name': 'Ivysaur', 'Type': 'Grass', 'Attack': 62, 'Defense': 63, 'HP': 60, 'Sp. Atk': 75, 'Sp. Def': 80, 'Speed': 60},
    {'Name': 'Venusaur', 'Type': 'Grass', 'Attack': 82, 'Defense': 83, 'HP': 80, 'Sp. Atk': 100, 'Sp. Def': 100, 'Speed': 75}
]

pokemon_list_big = [
    {'Name': 'Bulbasaur', 'Type': 'Grass', 'Attack': 49, 'Defense': 49, 'HP': 45, 'Sp. Atk': 65, 'Sp. Def': 60, 'Speed': 45},
    {'Name': 'Charmander', 'Type': 'Fire', 'Attack': 52, 'Defense': 43, 'HP': 39, 'Sp. Atk': 60, 'Sp. Def': 50, 'Speed': 65},
    {'Name': 'Charizard', 'Type': 'Fire', 'Attack': 84, 'Defense': 78, 'HP': 78, 'Sp. Atk': 109, 'Sp. Def': 85, 'Speed': 100},
    {'Name': 'Charmeleon', 'Type': 'Fire', 'Attack': 64, 'Defense': 58, 'HP': 58, 'Sp. Atk': 80, 'Sp. Def': 65, 'Speed': 80},
    {'Name': 'Ivysaur', 'Type': 'Grass', 'Attack': 62, 'Defense': 63, 'HP': 60, 'Sp. Atk': 75, 'Sp. Def': 80, 'Speed': 60},
    {'Name': 'Venusaur', 'Type': 'Grass', 'Attack': 82, 'Defense': 83, 'HP': 80, 'Sp. Atk': 100, 'Sp. Def': 100, 'Speed': 75},
    {'Name': 'Squirtle', 'Type': 'Water', 'Attack': 44, 'Defense': 48, 'HP': 65, 'Sp. Atk': 50, 'Sp. Def': 64, 'Speed': 43},
    {'Name': 'Wartortle', 'Type': 'Water', 'Attack': 59, 'Defense': 62, 'HP': 81, 'Sp. Atk': 61, 'Sp. Def': 82, 'Speed': 58},
    {'Name': 'Blastoise', 'Type': 'Water', 'Attack': 79, 'Defense': 82, 'HP': 100, 'Sp. Atk': 85, 'Sp. Def': 105, 'Speed': 78},
    {'Name': 'Rattata', 'Type': 'Normal', 'Attack': 30, 'Defense': 56, 'HP': 35, 'Sp. Atk': 25, 'Sp. Def': 35, 'Speed': 72},
    {'Name': 'Raticate', 'Type': 'Normal', 'Attack': 55, 'Defense': 81, 'HP': 61, 'Sp. Atk': 50, 'Sp. Def': 70, 'Speed': 97}
]

from statsApp import PokemonStats

def test_get_stats_small():
    stats = PokemonStats(pokemon_list)
    result = stats.get_stats()
    
    assert isinstance(result, dict)
    assert set(result.keys()) == set(['total_pokemon', 'avg_attack', 'avg_defense', 'avg_hp', 'avg_sp_atk', 'avg_sp_def', 'avg_speed'])

    assert result['total_pokemon'] == 6
    assert result['avg_attack'] == 65.5
    assert result['avg_defense'] == 62.333333333333336
    assert result['avg_hp'] == 60
    assert result['avg_sp_atk'] == 81.5
    assert result['avg_sp_def'] == 73.33333333333333
    assert result['avg_speed'] == 70.83333333333333

def test_top_10_attack_small():
    
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_attack()
    
    assert isinstance(result, list)
    assert len(result) == 6
    
    assert result[0]['Name'] == 'Charizard'
    assert result[1]['Name'] == 'Venusaur'
    assert result[2]['Name'] == 'Charmeleon'
    assert result[3]['Name'] == 'Ivysaur'
    assert result[4]['Name'] == 'Charmander'
    assert result[5]['Name'] == 'Bulbasaur'
    
def test_top_10_defense_small():
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_defense()
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0]['Name'] == 'Venusaur'
    assert result[1]['Name'] == 'Charizard'
    assert result[2]['Name'] == 'Ivysaur'
    assert result[3]['Name'] == 'Charmeleon'
    assert result[4]['Name'] == 'Bulbasaur'
    assert result[5]['Name'] == 'Charmander'   

def test_top_10_hp_small():
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_hp()
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0]['Name'] == 'Venusaur'
    assert result[1]['Name'] == 'Charizard'
    assert result[2]['Name'] == 'Ivysaur'
    assert result[3]['Name'] == 'Charmeleon'
    assert result[4]['Name'] == 'Bulbasaur'
    assert result[5]['Name'] == 'Charmander'
    
def test_top_10_sp_atk_small():
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_sp_atk()
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0]['Name'] == 'Charizard'
    assert result[1]['Name'] == 'Venusaur'
    assert result[2]['Name'] == 'Charmeleon'
    assert result[3]['Name'] == 'Ivysaur'
    assert result[4]['Name'] == 'Bulbasaur'
    assert result[5]['Name'] == 'Charmander'

def test_top_10_sp_def_small():
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_sp_def()
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0]['Name'] == 'Venusaur'
    assert result[1]['Name'] == 'Charizard'
    assert result[2]['Name'] == 'Ivysaur'
    assert result[3]['Name'] == 'Charmeleon'
    assert result[4]['Name'] == 'Bulbasaur'
    assert result[5]['Name'] == 'Charmander'
    
def test_top_10_speed_small():
    stats = PokemonStats(pokemon_list)
    result = stats.top_10_speed()
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0]['Name'] == 'Charizard'
    assert result[1]['Name'] == 'Charmeleon'
    assert result[2]['Name'] == 'Venusaur'
    assert result[3]['Name'] == 'Charmander'
    assert result[4]['Name'] == 'Ivysaur'
    assert result[5]['Name'] == 'Bulbasaur'
    
def test_get_stats_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.get_stats()
    
    assert isinstance(result, dict)
    assert set(result.keys()) == set(['total_pokemon', 'avg_attack', 'avg_defense', 'avg_hp', 'avg_sp_atk', 'avg_sp_def', 'avg_speed'])

    assert result['total_pokemon'] == 11
    assert result['avg_attack'] == 60
    assert result['avg_defense'] == 63.90909090909091
    assert result['avg_hp'] == 63.81818181818182
    assert result['avg_sp_atk'] == 69.0909090909091
    assert result['avg_sp_def'] == 72.36363636363636
    assert result['avg_speed'] == 70.27272727272727

def test_top_10_attack_big():
    
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_attack()
    
    assert isinstance(result, list)
    assert len(result) == 10
    
    #order the list_pokemon_big by attack from highest to lowest
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["Attack"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]
    
def test_top_10_defense_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_defense()
    assert isinstance(result, list)
    assert len(result) == 10
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["Defense"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]   

def test_top_10_hp_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_hp()
    assert isinstance(result, list)
    assert len(result) == 10
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["HP"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]
    
def test_top_10_sp_atk_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_sp_atk()
    assert isinstance(result, list)
    assert len(result) == 10
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["Sp. Atk"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]

def test_top_10_sp_def_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_sp_def()
    assert isinstance(result, list)
    assert len(result) == 10
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["Sp. Def"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]
    
def test_top_10_speed_big():
    stats = PokemonStats(pokemon_list_big)
    result = stats.top_10_speed()
    assert isinstance(result, list)
    assert len(result) == 10
    sorted_pokemon = sorted(pokemon_list_big, key=lambda x: x["Speed"], reverse=True)
    
    assert result[0] == sorted_pokemon[0]
    assert result[1] == sorted_pokemon[1]
    assert result[2] == sorted_pokemon[2]
    assert result[3] == sorted_pokemon[3]
    assert result[4] == sorted_pokemon[4]
    assert result[5] == sorted_pokemon[5]
    assert result[6] == sorted_pokemon[6]
    assert result[7] == sorted_pokemon[7]
    assert result[8] == sorted_pokemon[8]
    assert result[9] == sorted_pokemon[9]