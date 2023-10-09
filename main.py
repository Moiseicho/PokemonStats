from statsApp import PokemonStats
from readerApp import PokemonReader

file_path = input("Enter the file path of the CSV file: ")
reader = PokemonReader(file_path)
pokemon_stats = PokemonStats(reader.pokemon_list)

while True:
    print("Which statistic would you like to see?")
    print("1. Total number of Pokemon")
    print("2. Average Attack")
    print("3. Average Defense")
    print("4. Average HP")
    print("5. Average Special Attack")
    print("6. Average Special Defense")
    print("7. Average Speed")
    print("8. Top 10 Pokemon by Attack")
    print("9. Top 10 Pokemon by Defense")
    print("10. Top 10 Pokemon by HP")
    print("11. Top 10 Pokemon by Special Attack")
    print("12. Top 10 Pokemon by Special Defense")
    print("13. Top 10 Pokemon by Speed")
    print("14. Print the whole CSV")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Total number of Pokemon: {pokemon_stats.get_stats()['total_pokemon']}")
    elif choice == 2:
        print(f"Average Attack: {pokemon_stats.get_stats()['avg_attack']}")
    elif choice == 3:
        print(f"Average Defense: {pokemon_stats.get_stats()['avg_defense']}")
    elif choice == 4:
        print(f"Average HP: {pokemon_stats.get_stats()['avg_hp']}")
    elif choice == 5:
        print(f"Average Special Attack: {pokemon_stats.get_stats()['avg_sp_atk']}")
    elif choice == 6:
        print(f"Average Special Defense: {pokemon_stats.get_stats()['avg_sp_def']}")
    elif choice == 7:
        print(f"Average Speed: {pokemon_stats.get_stats()['avg_speed']}")
    elif choice == 8:
        print("Top 10 Pokemon by Attack:")
        for pokemon in pokemon_stats.top_10_attack():
            print(pokemon['Name'], pokemon['Attack'])
    elif choice == 9:
        print("Top 10 Pokemon by Defense:")
        for pokemon in pokemon_stats.top_10_defense():
            print(pokemon['Name'], pokemon['Defense'])
    elif choice == 10:
        print("Top 10 Pokemon by HP:")
        for pokemon in pokemon_stats.top_10_hp():
            print(pokemon['Name'], pokemon['HP'])
    elif choice == 11:
        print("Top 10 Pokemon by Special Attack:")
        for pokemon in pokemon_stats.top_10_sp_atk():
            print(pokemon['Name'], pokemon['Sp. Atk'])
    elif choice == 12:
        print("Top 10 Pokemon by Special Defense:")
        for pokemon in pokemon_stats.top_10_sp_def():
            print(pokemon['Name'], pokemon['Sp. Def'])
    elif choice == 13:
        print("Top 10 Pokemon by Speed:")
        for pokemon in pokemon_stats.top_10_speed():
            print(pokemon['Name'], pokemon['Speed'])
    elif choice == 14:
        print("Whole CSV:")
        for pokemon in reader.pokemon_list:
            print(pokemon)
    elif choice == 15:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 15.")
    
    input("Press enter to continue...")
