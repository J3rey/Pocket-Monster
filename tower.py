from poke_team import Trainer, PokeTeam
from enum import Enum
from battle import Battle
from battle_mode import BattleMode
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple
import random

class BattleTower:
    MIN_LIVES = 1
    MAX_LIVES = 3
    def __init__(self) -> None:
        """
        Worst Case = Best Case = O(1) as all operations run constant time
        """
        self.my_trainer = None
        self.enemy_trainers = ArraySortedList(3)
        self.trainer_lives = 0
        self.enemy_lives = ArrayStack(3)
        self.enemies_defeated_count = 0

    # Hint: use random.randint() for randomisation
    def set_my_trainer(self, trainer: Trainer) -> None:
        """
        Worst Case = Best Case = O(1) as all operations run constant time
        """
        self.my_trainer = trainer
        self.trainer_lives = random.randint(self.MIN_LIVES, self.MAX_LIVES) # Generates trainer lives from 1-3

    def generate_enemy_trainers(self, num_teams: int) -> None:
        """
        Worst Case O(N*T), where N is the length of num_teams and T is the length of the pokemon team of that trainer,
        this is because when enemy trainers are generated, it generates the length of num_teams and generates a pokemon
        team for each trainer that is the length of the pokemon team array. Enemy_trainer and lives have a defined amount
        of iterations (3). therefore they run constant time O(1) and is not accounted  

        Worst Case = Best Case as scenarios are not able to vary due to the function generating the same thing
        """
        for _ in range(num_teams): # For _ in num_teams
            enemy_trainer = Trainer(f'Enemy_{_ + 1}') # Create trainer name Enemy_x
            enemy_trainer.pick_team("Random") # Generate random team for Enemy_x
            enemy_trainer.poke_team.assemble_team(BattleMode.ROTATE) # Assemble team in Rotate battle mode
            self.enemy_trainers.add(enemy_trainer) # Adds each Enemy into ArraySortedList in enemy_trainers
            self.enemy_lives.push(random.randint(self.MIN_LIVES, self.MAX_LIVES)) # Pushes lives (1-3) to Enemy_x

        sorted_array = ArraySortedList(3) # Initialise array to sort trainers with lives
        for i in range(len(self.enemy_trainers)): 
            sorted_array.add(ListItem(self.enemy_trainers[i], self.enemy_lives[i])) # Pairs trainer with lives respectively in each array and sorts them according to size lives in ascending order

        sorted_trainers = [trainer.trainers for trainer in sorted_array] # Retrieves sorted trainers back into self.enemy_trainers
        self.enemy_trainers = sorted_trainers
        sorted_lives = [live.lives for live in sorted_array] # Retrieves sorted trainers back into self.enemy_lives
        self.enemy_lives = sorted_lives

    def battles_remaining(self) -> bool:
        """
        Worst Case is O(n), where n is the amount of rounds that trainer_lives is still positive. If the trainer keeps winning
        his battles then it will keep running
        Best Case is O(1), if trainer_lives become 0
        """
        return self.trainer_lives > 0 and any(lives > 0 for lives in self.enemy_lives) # If trainer lives > 0 and if any enemy trainer has lives > 0, return True

    def next_battle(self) -> Tuple[Trainer, Trainer, Trainer, int, int]:
        """
        Worst Case is O(N*M), where N is the amount of lives the enemy could have accumatively and M number of rounds in each battle.
        This is when the trainer would have to verse each enemy trainer for their maximum amount of lives and would have to go through
        every battle
        Best Case is O(P*M), where P is the amount of lives the trainer has and M number of rounds in each battle.
        This would happen when the trainer loses his first battle and had only one life
        """
        for i, enemy_trainer in enumerate(self.enemy_trainers): # For each enemy trainer and their position in the list of enemy trainers, check if they have more than 0 lives
            if self.enemy_lives[i] > 0:
                winner = Battle.rotate_battle(self.my_trainer, enemy_trainer) # Assigns the winner of the battle 

                if winner == self.my_trainer: # If trainer won
                    self.enemies_defeated_count += 1
                    self.enemy_lives[i] -= 1
                    result = "win"
                elif winner == enemy_trainer: # If trainer lost
                    self.trainer_lives -= 1
                    result = "loss"
                else:
                    self.trainer_lives -= 1 # If trainer and enemy drawed
                    self.enemy_lives[i] -= 1
                    result = "draw"

                return (result, self.my_trainer, enemy_trainer, self.trainer_lives, self.enemy_lives[i])
                
        raise ValueError("No battles remaining")

    def enemies_defeated(self) -> int:
        """
        Worst Case = Best Case = O(1) as all operations run constant time
        """
        return self.enemies_defeated_count