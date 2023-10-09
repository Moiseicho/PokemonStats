class PokemonStats:
    def __init__(self, pokemon_list):
        self.pokemon_list = pokemon_list
    
    def get_stats(self):
        total_pokemon = len(self.pokemon_list)
        total_attack = 0
        total_defense = 0
        total_hp = 0
        total_sp_atk = 0
        total_sp_def = 0
        total_speed = 0
        for pokemon in self.pokemon_list:
            total_attack += int(pokemon["Attack"])
            total_defense += int(pokemon["Defense"])
            total_hp += int(pokemon["HP"])
            total_sp_atk += int(pokemon["Sp. Atk"])
            total_sp_def += int(pokemon["Sp. Def"])
            total_speed += int(pokemon["Speed"])
        avg_attack = total_attack / total_pokemon
        avg_defense = total_defense / total_pokemon
        avg_hp = total_hp / total_pokemon
        avg_sp_atk = total_sp_atk / total_pokemon
        avg_sp_def = total_sp_def / total_pokemon
        avg_speed = total_speed / total_pokemon
        return {
            "total_pokemon": total_pokemon,
            "avg_attack": avg_attack,
            "avg_defense": avg_defense,
            "avg_hp": avg_hp,
            "avg_sp_atk": avg_sp_atk,
            "avg_sp_def": avg_sp_def,
            "avg_speed": avg_speed
        }
    
    def top_10_attack(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["Attack"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
    
    def top_10_defense(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["Defense"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
    
    def top_10_hp(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["HP"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
    
    def top_10_sp_atk(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["Sp. Atk"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
    
    def top_10_sp_def(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["Sp. Def"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
    
    def top_10_speed(self):
        sorted_pokemon = sorted(self.pokemon_list, key=lambda x: x["Speed"], reverse=True)
        top_10 = sorted_pokemon[:10]
        return top_10
