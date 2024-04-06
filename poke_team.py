from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from ctypes import py_object
from data_structures.bset import BSet
from data_structures.set_adt import Set 

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = None # change None value if necessary
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
                print("Inavlid Pokemon name, try again") # If user inputs invalid pokemon, try again until done or reached team limit


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
        current_health = Pokemon.get_health()
        for pokemon in self.team:
            pokemon.health = current_health # This doesn't work but I was trying to get the original health from pokemon.py and assign it to the current pokemons health

    def assign_team(self, criterion: str = None) -> None:
        #Next Task
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        #Next Task
        raise NotImplementedError

    def special(self, battle_mode: BattleMode) -> None:
        #Next Task
        raise NotImplementedError

    def __getitem__(self, index: int):
        """
        Best Case for __getitem__ is O(1), if the user gets a successful index the first time
        Worst Case for __getitem__ is O(n), where n is the number of attempts the user inputs,
        as it will repeat n amount of times until the user get a valid index
        """
        poke_team = self.team # Makes poke_team the array
        index = int(input("Enter an index to retrieve a Pokemon: ")) # Ask user input what index
        try:
            pokemon = poke_team[index] # Tries to see if user input index is within list
            print(f"The Pokemon at index {index} is: {pokemon}") #print
        except IndexError: # If not in list, raise error
            print("Invalid index. Please enter an index within the range of the team.")
        

    def __len__(self):
        """
        Best and Worse Case is O(1) as it only returns 
        """
        return len(self.team) #returns length of team

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
            raise ValueError("Invalid input. Enter either 1 or 2.") # If input is invalid, raise error

    def get_team(self) -> PokeTeam:
        return self.poke_team # Gets current pokemon team
    
    def get_name(self) -> str:
        return self.name # Gets trainer name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        self.pokedex.add(pokemon.get_poketype().value+1) # Gets type of pokemon, assigns to a numerical value and adds a 1 to it in Pokedex


    def get_pokedex_completion(self) -> float:
        """
        Best and Worse Case is O(1) as all operations are constant time
        """
        pokedex_completion = sum(self.pokedex) / len(PokeType) # Divides current registered types with len(PokeType) (15)
        return round(pokedex_completion, 2) # Round to 2d.p

    def __str__(self) -> str:
        """
        Best and Worse Case is O(1) as just print
        """
        print(f"Trainer {Trainer.get_name}\n Pokedex Completion: {Trainer.get_pokedex_completion}%")
                
if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())