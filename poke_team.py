from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from ctypes import py_object
from battle_mode import BattleMode
from data_structures.bset import BSet
from data_structures.set_adt import Set 
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = ArrayR(6) # Initialise array size
        self.team_count = 0

    """
    Best case for choose_manually is is O(1), if the user is 'done' and stores no pokemon
    Worst case for choose_manually is O(n), where n the number of user inputs. As it iterates 
    over user pokemon choices, appending valid options to self.team until the team limit has 
    been reached the user is done
    """
    def choose_manually(self):
        self.team = ArrayR(1) # Initialise array size
        while len(self.team) < PokeTeam.TEAM_LIMIT: # While team Array is less TEAM_LIMIT (6)
            pokemon_choice = input("Enter a Pokemon's name or 'done': ") # Requests user pokemon choices
            if pokemon_choice.lower() == 'done': # If user requests done, break
                break
            if pokemon_choice in PokeTeam.POKE_LIST: # If user chose a pokemon in the pokemon list
                for i in range(len(self.team)): # Append pokemon to the array and increase team size by 1
                    self.team[i] = pokemon_choice
                    self.team += 1
            else:
                print("Invalid Pokemon name, try again") # If user inputs invalid pokemon, try again until done or reached team limit

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1


    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        """
        Best and Worse Case is O(n), where n is the length of team
        """
        # Heals all Pokémon to their original HP
        for pokemon in self.team:
            pokemon.get_health = pokemon.health  # Resets current health to base health
            pokemon.is_alive() # Calls method to make pokemon register as alive

    def assign_team(self, criterion: str = None) -> None:
        #Next Task
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        """
        Worst Case is O(n), where n is the length of the team, as it needs to append to the new specified teams, set, rotate and optimise
        Best Case is O(n), where n is the length of the team, as it need to choose a battle_mode must be chosen
        """
        if battle_mode == BattleMode.SET: # If battlemode matches with enumerate
            set_team = ArrayStack(len(self.team)) # Initialise ArrayStack
            for pokemon in self.team:
                set_team.push(pokemon)
            self.team = set_team # New team order
        elif battle_mode == BattleMode.ROTATE: # If battlemode matches with enumerate
            rotate_team = CircularQueue(len(self.team)) # Initialise CircularQueue
            for pokemon in self.team:
                rotate_team.append(pokemon)
            self.team = rotate_team # New team order
        elif battle_mode == BattleMode.OPTIMISE: # If battlemode matches with enumerate
            optimise_team = ArraySortedList(len(self.team)) # Initialise ArraySortedList
            for pokemon in self.team:
                optimise_team.add(pokemon)
            self.team = optimise_team # New team order
    
    def special(self, battle_mode: BattleMode) -> None:

        if battle_mode == BattleMode.SET: # If battlemode matches with enumerate
            x = len(self.team) # Length of team
            temp_team = x // 2 
            half_stack = ArrayStack(temp_team) 
            for i in range(temp_team): # LIFO, pushes first 3 pokemon into temp team
                half_stack.push(self.team[i])
            for i in range(half_stack): 
                self.team[i] = half_stack.pop() # LIFO, pops first 3 pokemon into original team, reversing first 3 pokemon
            return self.team
        elif battle_mode == BattleMode.ROTATE: # If battlemode matches with enumerate
            x = len(self.team) # Length of team
            temp_team = x // 2
            temp_queue = CircularQueue(x - temp_team) # Initialises temp team, to be the length of the bottom half
            for i in range(temp_team, x): 
                temp_queue.append(temp_queue[i]) # FIFO Append bottom half of self.team into temp_queue [4, 5, 6]
            for i in range(x - 1, temp_queue - 1, -1): # Range starts at the end of the length of self.team and works itself backwards to the end of half of the team length 
                temp_queue[i] = self.team.serve()    
                return self.team
        elif battle_mode == BattleMode.OPTIMISE: # If battlemode matches with enumerate

            #idk
            raise NotImplementedError

        # OPTIMISE MODE: it toggles the sorting order (from ascending to descending and vice-versa)
        
        raise NotImplementedError

    def __getitem__(self, index: int):
        """
        Best Case for __getitem__ is O(1), if index is valid
        Worst Case for __getitem__ is O(n), where n is the number of invalid index attempts
        as it will repeat n amount of times until a valid index 
        """
        try: # Tries to see if index is within list
            pokemon = self.team[index] # Gets pokemon
            print(f"The Pokemon at index {index} is: {pokemon}") #print
        except IndexError: # If not in list, raise error
            print("Invalid index. Please enter an index within the range of the team.")

    def __len__(self):
        """
        Best and Worse Case is O(1) as it only returns 
        """
        return len(self.team) # Returns length of team

    def __str__(self):
        """
        Best Case for __str__ is O(1) if the list is empty
        Worst Case for __str__ is O(n), where n is the length of the team, as it 
        would have to loop through the team
        """
        team_str = "Pokemon Team:\n"
        # Displays all pokemon in the current team
        for pokemon in self.team:
            team_str += f"{pokemon.name}\n" 
        return team_str

class Trainer:

    def __init__(self, name) -> None:
        self.name = name # Initialises Trainer Class
        self.poke_team = PokeTeam() # Initialises Pokemon Team
        self.pokedex = BSet(len(PokeType)+1)# Initialises Trainer Class

    def pick_team(self, method: str) -> None:
        """
        Worst Case is O(1) as this function only contains return functions which are constant time
        Worst Case = Best Case = O(1)
        """
        if method == "Random":
            PokeTeam.choose_randomly()
        elif method == "Manual":
            PokeTeam.choose_manually()
        else:
            raise ValueError("Invalid input. Enter either 'Random' or 'Manual'") # If input is invalid, raise error

    def get_team(self) -> PokeTeam:
        return self.poke_team # Gets current pokemon team
    
    def get_name(self) -> str:
        return self.name # Gets trainer name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        """
        Best and Worse Case is O(1) as all operations are constant time and bit vectors do not need resizing
        """
        self.pokedex.add(pokemon.get_poketype().value+1) # Gets type of pokemon, assigns to a numerical value and adds a 1 to it in Pokedex


    def get_pokedex_completion(self) -> float:
        """
        Best and Worse Case is O(1) as all operations are constant time
        """
        pokedex_completion = len(self.pokedex) / len(PokeType) # Divides current registered types with len(PokeType) (15)
        return round(pokedex_completion, 1) # Round to 1d.p

    def __str__(self) -> str:
        completed_pokedex = int(self.get_pokedex_completion() * 100)
        return f"Trainer {self.get_name()} Pokedex Completion: {completed_pokedex}%"
              
if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())