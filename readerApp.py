import csv

class PokemonReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pokemon_list = []
        self.load_pokemon()

    def load_pokemon(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.pokemon_list.append(row)
