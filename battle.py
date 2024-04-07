from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode

class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.battle_mode = battle_mode
        self.criterion = criterion

    def commence_battle(self) -> Trainer | None:
        if self.battle_mode == BattleMode.SET:
            return self.set_battle()
        elif self.battle_mode == BattleMode.ROTATE:
            return self.rotate_battle()
        elif self.battle_mode == BattleMode.OPTIMISE:
            return self.optimise_battle()
        else:
            raise ValueError("Please select valid BattleMode")
    
    def _create_teams(self) -> None:
        self.trainer_1 = PokeTeam.assemble_team
        self.trainer_2 = PokeTeam.assemble_team

    # Note: These are here for your convenience
    # If you prefer you can ignore them
    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError


if __name__ == '__main__':
    t1 = Trainer('Ash')
    t2 = Trainer('Gary')
    b = Battle(t1, t2, BattleMode.ROTATE)
    b._create_teams()
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
