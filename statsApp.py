class PokemonStats:
    def __init__(self, pokemon_list):
        if not pokemon_list:
            raise ValueError("Pokemon list can not be empty")
        self.pokemon_list = pokemon_list
        self.total_pokemon = len(self.pokemon_list)
        self.total_attack = 0
        self.total_defense = 0
        self.total_hp = 0
        self.total_sp_atk = 0
        self.total_sp_def = 0
        self.total_speed = 0
        for pokemon in self.pokemon_list:
            try:
                pokemon['#']
                pokemon['Name']
                pokemon['Type1']
                pokemon['Type2']
                self.total_attack += int(pokemon["Attack"])
                self.total_defense += int(pokemon["Defense"])
                self.total_hp += int(pokemon["HP"])
                self.total_sp_atk += int(pokemon["Sp. Atk"])
                self.total_sp_def += int(pokemon["Sp. Def"])
                self.total_speed += int(pokemon["Speed"])
            except KeyError as e:
                raise KeyError(f"Pokemon {pokemon} is missing column {e}")
                
            
        assert(self.total_pokemon != 0)
        self.avg_attack = self.total_attack / self.total_pokemon
        self.avg_defense = self.total_defense / self.total_pokemon
        self.avg_hp = self.total_hp / self.total_pokemon
        self.avg_sp_atk = self.total_sp_atk / self.total_pokemon
        self.avg_sp_def = self.total_sp_def / self.total_pokemon
        self.avg_speed = self.total_speed / self.total_pokemon
    
    def get_stats(self):
        return {
            "total_pokemon": self.total_pokemon,
            "avg_attack": self.avg_attack,
            "avg_defense": self.avg_defense,
            "avg_hp": self.avg_hp,
            "avg_sp_atk": self.avg_sp_atk,
            "avg_sp_def": self.avg_sp_def,
            "avg_speed": self.avg_speed
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
