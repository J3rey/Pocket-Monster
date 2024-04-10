from poke_team import Trainer, PokeTeam
from enum import Enum
from battle import Battle
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
        self.my_trainer = None
        self.enemy_trainers = [] # Need to make circular init
        self.trainer_lives = 0
        self.enemy_lives = [] # Fix
        self.enemies_defeated_count = 0

    # Hint: use random.randint() for randomisation
    def set_my_trainer(self, trainer: Trainer) -> None:
        """
        Worst Case = Best Case = O(1) as all operations run constant time
        """
        self.my_trainer = trainer
        self.trainer_lives = random.randint(self.MIN_LIVES, self.MAX_LIVES) # Generates trainer lives from 1-3

    def generate_enemy_trainers(self, num_teams: int) -> None:
        for _ in range(num_teams):
            enemy_trainer = Trainer(f'Enemy_{_ + 1}')
            enemy_trainer.pick_team("Random")
            self.enemy_trainers.append(enemy_trainer) # Append needs to be circular
            self.enemy_lives.append(random.randint(self.MIN_LIVES, self.MAX_LIVES))

    def battles_remaining(self) -> bool:
        return self.trainer_lives > 0 and any(lives > 0 for lives in self.enemy_lives)

    def next_battle(self) -> Tuple[Trainer, Trainer, Trainer, int, int]:
        for i, enemy_trainer in enumerate(self.enemy_trainers):
            if self.enemy_lives[i] > 0:
                winner = Battle.rotate_battle(self.my_trainer, enemy_trainer)

                if winner == self.my_trainer:
                    self.enemies_defeated_count += 1
                    self.enemy_lives[i] -= 1
                    result = "win"
                elif winner == enemy_trainer:
                    self.trainer_lives -= 1
                    result = "loss"
                else:
                    self.trainer_lives -= 1
                    self.enemy_lives[i] -= 1
                    result = "draw"

                return (result, self.my_trainer, enemy_trainer, self.trainer_lives, self.enemy_lives[i])
                
        raise ValueError("No battles remaining")

    def enemies_defeated(self) -> int:
        return self.enemies_defeated_count