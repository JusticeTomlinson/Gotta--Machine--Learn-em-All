from typing import Dict, List


class Trainer:
    pass


class Team:
    def __init__(self, all_pokemon):
        pass




class Ability:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def show_item(self) -> None:
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.description}")
        print({'-'*40})


class Item:

    def __init__(self, name: str, effect: str) -> None:
        self.name = name
        self.effect = effect

    def show_item(self) -> None:
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.effect}")
        print({'-'*40})


class PKMNMove:
    def __init(self, name, effect, damage: float, accuracy: float, status_type: str,
               status_chance: float, pp: int):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.accuracy = accuracy
        self.status_type = status_type
        self.status_chance = status_chance
        self.pp = pp


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


class PokedexEntry:
    def __init__(self, number: int, name: str, description: str, height: float,
                 weight: float, base_stats: List[float]) -> None:
        self.number = number
        self.name = name
        self.description = description
        self.height = height
        self.weight = weight
        self.base_stats = base_stats


class Pokedex:
    def __init__(self, entries: List[PokedexEntry]) -> None:
        self.entries = entries

    def __len__(self) -> int:
        return len(self.entries)


class BattleSimulation:
    def __init__(self, trainer1: Trainer, trainer2: Trainer, trainer1AI: bool,
                 trainer2AI: bool, trainer1AIPolicy, trainer2AIPolicy) -> None:
        pass






