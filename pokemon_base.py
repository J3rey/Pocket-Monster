"""
This module contains PokeType, TypeEffectiveness and an abstract version of the Pokemon Class
"""
from abc import ABC
from enum import Enum
from data_structures.referential_array import ArrayR
import math

class PokeType(Enum):
    """
    This class contains all the different types that a Pokemon could belong to
    """
    FIRE = 0
    WATER = 1
    GRASS = 2
    BUG = 3
    DRAGON = 4
    ELECTRIC = 5
    FIGHTING = 6
    FLYING = 7
    GHOST = 8
    GROUND = 9
    ICE = 10
    NORMAL = 11
    POISON = 12
    PSYCHIC = 13
    ROCK = 14

class TypeEffectiveness:
    """
    Represents the type effectiveness of one Pokemon type against another.
    """

    @classmethod
    def get_effectiveness(cls, attack_type: PokeType, defend_type: PokeType) -> float:
        """
        Returns the effectiveness of one Pokemon type against another, as a float.

        Parameters:
            attack_type (PokeType): The type of the attacking Pokemon.
            defend_type (PokeType): The type of the defending Pokemon.

        Returns:
            float: The effectiveness of the attack, as a float value between 0 and 4.
        """
    
        EFFECT_TABLE = ArrayR(len(PokeType))  # Initialize the array

        with open('type_effectiveness.csv', "r") as file:
            next(file)  # Skips the first line
            for i, row in enumerate(file):
                rowlist = row.strip().split(',')
                row_array = ArrayR(len(rowlist))  # Creates a new array for this row
                for j, value in enumerate(rowlist):
                    row_array[j] = float(value)  # Converts each value to float and store it in the array
                EFFECT_TABLE[i] = row_array  # Stores the row arrays in EFFECT_TABLE
        
        cls.float = EFFECT_TABLE[attack_type.value][defend_type.value] # Gets float of enum index values
        return cls.float


    def __len__(self) -> int:
        """
        Returns the number of types of Pokemon
        """
        return len(PokeType)

class Pokemon(ABC): # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """
    Represents a base Pokemon class with properties and methods common to all Pokemon.
    """
    def __init__(self):
        """
        Initializes a new instance of the Pokemon class.
        """
        self.health = None
        self.level = None
        self.poketype = None
        self.battle_power = None
        self.evolution_line = None
        self.name = None
        self.experience = None
        self.defence = None
        self.speed = None

    def get_name(self) -> str:
        """
        Returns the name of the Pokemon.

        Returns:
            str: The name of the Pokemon.
        """
        return self.name

    def get_health(self) -> int:
        """
        Returns the current health of the Pokemon.

        Returns:
            int: The current health of the Pokemon.
        """
        return self.health

    def get_level(self) -> int:
        """
        Returns the current level of the Pokemon.

        Returns:
            int: The current level of the Pokemon.
        """
        return self.level

    def get_speed(self) -> int:
        """
        Returns the current speed of the Pokemon.

        Returns:
            int: The current speed of the Pokemon.
        """
        return self.speed

    def get_experience(self) -> int:
        """
        Returns the current experience of the Pokemon.

        Returns:
            int: The current experience of the Pokemon.
        """
        return self.experience

    def get_poketype(self) -> PokeType:
        """
        Returns the type of the Pokemon.

        Returns:
            PokeType: The type of the Pokemon.
        """
        return self.poketype

    def get_defence(self) -> int:
        """
        Returns the defence of the Pokemon.

        Returns:
            int: The defence of the Pokemon.
        """
        return self.defence

    def get_evolution(self):
        """
        Returns the evolution line of the Pokemon.

        Returns:
            list: The evolution of the Pokemon.
        """
        return self.evolution_line

    def get_battle_power(self) -> int:
        """
        Returns the battle power of the Pokemon.

        Returns:
            int: The battle power of the Pokemon.
        """
        return self.battle_power

    def attack(self, other_pokemon) -> int:
        """
        Calculates and returns the damage that this Pokemon inflicts on the
        other Pokemon during an attack.

        Args:
            other_pokemon (Pokemon): The Pokemon that this Pokemon is attacking.

        Returns:
            int: The damage that this Pokemon inflicts on the other Pokemon during an attack.
        """
        other_pokemon = Pokemon
        # Compute attack stat vs defence stat
        if other_pokemon.get_defence() < self.get_battle_power() / 2:
            damage = self.get_battle_power() - other_pokemon.get_defence()
        elif other_pokemon.get_defence() < self.get_battle_power():
            damage = math.ceil(self.get_battle_power() * 5/8 - other_pokemon.get_defence() / 4)
        else:
            damage = math.ceil(self.get_battle_power() / 4)

        # Apply type effectiveness
        damage_multiplier = TypeEffectiveness.get_effectiveness(self.get_poketype,other_pokemon.get_poketype)
        damage = damage_multiplier * damage      

        return damage

    def defend(self, damage: int) -> None:
        """
        Reduces the health of the Pokemon by the given amount of damage, after taking
        the Pokemon's defence into account.

        Args:
            damage (int): The amount of damage to be inflicted on the Pokemon.
        """
        effective_damage = damage/2 if damage < self.get_defence() else damage
        self.health = self.health - effective_damage

    def level_up(self) -> None:
        """
        Increases the level of the Pokemon by 1, and evolves the Pokemon if it has
          reached the level required for evolution.
        """

        self.level += 1
        if len(self.evolution_line) > 0 and self.evolution_line.index\
            (self.name) != len(self.evolution_line)-1:
            self._evolve()

    def _evolve(self) -> None:
        """
        Evolves the Pokemon to the next stage in its evolution line, and updates
          its attributes accordingly.
        """
        # Levels all base stats by x1.5
        # Pokemon evolves to next in line if not in final evolution
        if len(self.evolution_line) > 0 and self.evolution_line.index(self.name) != len(self.evolution_line) - 1:
            self.name = self.evolution_line[self.evolution_line.index(self.name) + 1]
            self.health *= 1.5
            self.battle_power *= 1.5
            self.speed *= 1.5
            self.defence *= 1.5

    def is_alive(self) -> bool:
        """
        Checks if the Pokemon is still alive (i.e. has positive health).

        Returns:
            bool: True if the Pokemon is still alive, False otherwise.
        """
        return self.get_health() > 0

    def __str__(self):
        """
        Return a string representation of the Pokemon instance in the format:
        <name> (Level <level>) with <health> health and <experience> experience
        """
        return f"{self.name} (Level {self.level}) with {self.get_health()} health \
                and {self.get_experience()} experience"
    
