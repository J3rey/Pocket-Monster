from pokemon import *
import random
from typing import List
from battle_mode import BattleMode

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = None # change None value if necessary
        self.team_count = 0

    def choose_manually(self):
        ##redo
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

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
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
        print("Current Pokemon Team:")
        pokemon_name = self.team[i].get().get_name()
        for i in range(len(self.team)):
            print(f'{pokemon_name}\n')

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