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

    def resize(self, new_length: int) -> None:
        # Checks if the updated team exceeds the maximum team size
        if new_length > 6:
            print("Maximum team size reached (6 Pokémon).")           
        # Creates a current_team_count of the specified length, initialized with None
        current_team_count = (new_length * py_object)()
        # Fills the current_team_count with elements from the self.array, or None if the index is out of bounds
        current_team_count[:] = [self.array[i] if i < len(self.array) else None for i in range(new_length)]
        # Update the self.array to be the current_team_count
        self.array = current_team_count


    def choose_manually(self):
        #initialise array size
        self.team = ArrayR(1)
        PokemonTeam = self.team
        
        PokemonTeam.resize(len(PokemonTeam) + 1)  # Increase the length of the array by 1
        PokemonTeam[len(PokemonTeam) - 1] = user_input  # Add the user input to the end of the array








        """
               # This function's time complexity depends on the TeamMode:
       #     - TeamMode.FRONT: O(1)
       #     - TeamMode.BACK: O(1)
       #     - TeamMode.OPTIMISE: O(n), n = team size
       # Where n is the number of monsters in the team
        
        if self.init:
            self.original_team.add_to_tail(DLLNode(type(monster)))

        if self.team_mode == self.TeamMode.FRONT:
            self.team.add_to_head(DLLNode(monster))
        elif self.team_mode == self.TeamMode.BACK:
            self.team.add_to_tail(DLLNode(monster))
        elif self.team_mode == self.TeamMode.OPTIMISE:
            if len(self.team) == 0:
                self.team.add_to_head(DLLNode(monster))
                return
            
            stat_getters = {
                self.SortMode.HP: lambda m: m.get_hp(),
                self.SortMode.ATTACK: lambda m: m.get_attack(),
                self.SortMode.DEFENSE: lambda m: m.get_defense(),
                self.SortMode.SPEED: lambda m: m.get_speed(),
                self.SortMode.LEVEL: lambda m: m.get_level(),
            }
            get_stat = stat_getters[self.sort_key]
            
            for i in range(len(self.team)):
                node = self.team[i]
                if node.next() and ((get_stat(node.next().get()) <= get_stat(monster) <= get_stat(node.get())) \
                                or (get_stat(node.next().get()) >= get_stat(monster) >= get_stat(node.get()))):
                    self.team.insert_after(node, DLLNode(monster))
                    return
        """

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