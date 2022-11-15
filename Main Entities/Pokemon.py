from typing import List
from Move import PKMNMove


class Pokemon:
    def __init(self, name: str, ability: str, item: str, gender: str,
               attack: float, hp: float, defense: float, special_attack: float,
               special_defense: float, speed: float, nature: str,
               moves: List[PKMNMove], EVs: List[float]) -> None:
        self.name = name
        self.ability = ability
        self.item = item
        self.gender = gender
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.nature = nature
        self.moves = moves
        self.EVs = EVs

    def display_stats(self) -> None:
        print({'-'*40})

        print(f"Pokemon:{self.name}")
        print(f"Ability: {self.ability}")
        print(f"Item: {self.item}")
        print(f"Gender: {self.gender}")
        print(f"HP: : {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Special Attack: {self.special_attack}")
        print(f"Special Defense: {self.special_defense}")
        print(f"Speed: {self.speed}")
        print(f"Nature: {self.nature}")
        print(f"Moves: {self.moves}")
        print({'-'*40})
