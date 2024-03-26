from pokemon import *
import random
from typing import List
from battle_mode import BattleMode

class Bulbasaur():
    def __init__(self):
        super().__init__()
        self.health = 45
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 14
        self.evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
        self.name = "Bulbasaur"
        self.experience = 0
        self.defence = 20
        self.speed = 4.5

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = []  # Initialize an empty list to store Pokemon instances

    def add_pokemon(self, pokemon):
        if len(self.team) < self.TEAM_LIMIT:
            self.team.append(pokemon)
        else:
            print("Team is full. Cannot add more Pokemon.")

    def __str__(self):
        team_str = "PokeTeam:\n"
        for pokemon in self.team:
            team_str += f" - {pokemon.name}\n"
        return team_str

# Example usage
my_team = PokeTeam()
my_team.add_pokemon(Bulbasaur())

print(my_team)
