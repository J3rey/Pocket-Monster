from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from ctypes import py_object

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = None # change None value if necessary
        self.team_count = 0

    """
    Best case for choose_manually is is O(1), if the user is 'done' and stores no pokemon
    Worst case for choose_manually is O(n) as it iterates over user pokemon choices, appending
    valid options to self.team until the team limit has been reached the user is done
    """
    def choose_manually(self):
        # Initialise array size
        self.team = ArrayR(1)

        # While team Array is less TEAM_LIMIT (6)
        while len(self.team) < PokeTeam.TEAM_LIMIT:
            # Requests user pokemon choices
            pokemon_choice = input("Enter a Pokemon's name or 'done': ")
            # If user requests done, break
            if pokemon_choice.lower() == 'done':
                break
            # If user chose a pokemon in the pokemon list
            if pokemon_choice in PokeTeam.POKE_LIST:
                # Append pokemon to the array and increase team size by 1
                for i in range(len(self.team)):
                    self.team[i] = pokemon_choice
                    self.team += 1
            else:
                # If user inputs invalid pokemon, try again until done or reached team limit
                print("Inavlid Pokemon name, try again")


    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    
    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        """
           '''
        O(n), n = team size
        '''
           ##redo
        self.team.reset()
        self.sort_descending = True
        monster = self.original_team.get_head()
        while monster is not None:
            self.add_to_team((monster.get())())
            monster = monster.next()
        """
        raise NotImplementedError



    def assign_team(self, criterion: str = None) -> None:
        
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        #Next Task
        raise NotImplementedError

    def special(self, battle_mode: BattleMode) -> None:
        #Next Task
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError

    def __len__(self):
        return len(self.team)


    def __str__(self):
        team_str = "Pokemon Team:\n"
        for pokemon in self.team:
            team_str += f"{pokemon.name}\n"
            
        return team_str
        


class Trainer:

    def __init__(self, name) -> None:
        raise NotImplementedError

    def pick_team(self, method: str) -> None:
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def register_pokemon(self, pokemon: Pokemon) -> None:
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())