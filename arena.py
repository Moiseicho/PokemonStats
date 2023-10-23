# BEGIN: 3d5f7c9f5d9a
class Arena:
    
    def attackRound(attacker, defender, lost1, lost2, playerName1, playerName2):
        
        stalemate = True;
        print(playerName1 + "'s " + attacker[lost1]['Name'] + ' goes first!')
        
        damage = int(attacker[lost1]['Attack']) - (int(defender[lost2]['Defense'])/3)
        if damage <= 0:
            damage = 0
        else:
            stalemate = False
        defender[lost2]['HP'] = int(defender[lost2]['HP']) - (damage/3)
        
        print("He deals " + str(round(damage/3, 1)) + " damage!")
        
        if(defender[lost2]['HP'] <= 0):
            lost2 += 1
            if(lost2 < len(defender)):
                print(defender[lost2-1]['Name'] + ' has fainted. ' + str(len(defender) - lost2) + ' Pokemon left for ' + playerName2 + '.')
                print(playerName2 + " takes out his next pokemon: " + defender[lost2]['Name'] + "!")
                input()
                return lost1, lost2
            else:
                print(attacker[lost1]['Name'] + " has defeted the opponent's last pokemon! " + playerName1 + ' has won!')
                return lost1, lost2
        else:
            print(defender[lost2]['Name'] + ' has ' + str(round(defender[lost2]['HP'], 1)) + ' HP left')
            
        input()
        print(playerName2 + "'s " + defender[lost2]['Name'] + ' retaliates!')
        
        damage = int(defender[lost2]['Attack']) - (int(attacker[lost1]['Defense'])/3)
        if damage <= 0:
            damage = 0
        else:
            stalemate = False
        attacker[lost1]['HP'] = int(attacker[lost1]['HP']) - (damage/3)
        print("He deals " + str(round(damage/3, 1)) + " damage!")
        
        if(attacker[lost1]['HP'] <= 0):
            lost1 += 1
            if(lost1 < len(attacker)):
                print(attacker[lost1-1]['Name'] + ' has fainted. ' + str(len(attacker) - lost1) + ' Pokemon left for ' + playerName1 + '.')
                print(playerName1 + " takes out his next pokemon: "+ attacker[lost1]['Name'] + "!")
            else:
                print(defender[lost2]['Name'] + " has defeted the opponent's last pokemon! " + playerName2 + ' has won!')
                return lost1, lost2
        else:
            print(attacker[lost1]['Name'] + ' has ' + str(round(attacker[lost1]['HP'], 1)) + ' HP left')
        
        input()
        if stalemate: return -1, -1
        return lost1, lost2
    
    def battle(self, pokemon_list, p1_pokemon_names, p2_pokemon_names):
        if not (1 <= len(p1_pokemon_names) <= 6 and 1 <= len(p2_pokemon_names) <= 6):
            raise ValueError("Both players must have between 1 and 6 pokemon.")

        required_columns = ['Name', 'Attack', 'Defense', 'Speed', 'HP']
        for column in required_columns:
            for pokemon in pokemon_list:
                if column not in pokemon:
                    raise ValueError(column + " is missing: " + str(pokemon))
                if pokemon[column] == '':
                    raise ValueError(column + " is empty: " + str(pokemon))
                if column != 'Name' and not isinstance(pokemon[column], int):
                    raise ValueError(column + " must be an integer: " + str(pokemon))
        p1_pokemon = []
        p2_pokemon = []

        try:
            pokemon_dict = {pokemon['Name']: pokemon for pokemon in pokemon_list}
            for name in p1_pokemon_names:
                p1_pokemon.append(pokemon_dict[name])
            for name in p2_pokemon_names:
                p2_pokemon.append(pokemon_dict[name])
        except KeyError as e:
            raise ValueError(str(e) + " is not in the pokemon list.")
        lost1 = 0
        lost2 = 0
        print("Player one takes out " + p1_pokemon[lost1]['Name'] + "!")
        print("Player two takes out " + p2_pokemon[lost2]['Name'] + "!")
        while lost1 < len(p1_pokemon) and lost2 < len(p2_pokemon):
            if(p1_pokemon[lost1]['Speed'] > p2_pokemon[lost2]['Speed']):
                lost1, lost2 = Arena.attackRound(p1_pokemon, p2_pokemon, lost1, lost2, "Player 1", "Player 2")
            else:
                lost2, lost1 = Arena.attackRound(p2_pokemon, p1_pokemon, lost2, lost1, "Player 2", "Player 1")
            if lost1 == -1 and lost2 == -1:
                print("Stalemate! No one wins!")
                return
            print()
