from typing import List

from Main_Entities import Pokemon
from Main_Entities.Move import PKMNMove


class PokemonBE(Pokemon.Pokemon):

    def __init__(self, name: str, level: int, ability: str, item: str,
                 gender: str, attack: float, hp: float, defense: float,
                 special_attack: float, special_defense: float, speed: float,
                 nature: str, moves: List[PKMNMove], EVs: List[float],
                 status: str):

        super().__init__(name, level, ability, item, gender, attack, hp, defense,
                         special_attack,  special_defense, speed, nature,
                         moves, EVs)
        self.status = status





