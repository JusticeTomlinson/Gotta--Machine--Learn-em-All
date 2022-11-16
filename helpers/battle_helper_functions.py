from typing import Union

from Main_Entities import Move
from Main_Entities.Move import PKMNMove
from Main_Entities.Pokemon import Pokemon
from Main_Entities.Trainer import Trainer


def check_if_winner(trainer1: Trainer, trainer2: Trainer) -> Union[None, Trainer]:
    """
    :param trainer1: Represents a Trainer in a Battle.
    :param trainer2: Represents a Trainer in a Battle.
    :return: None, if both Trainers have Pokemon who can fight left, the Object
    of the Trainer who has won if only one Trainer has pokemon.
    """
    t1_at_least_1_alive = False
    t2_at_least_1_alive = False

    for pokemon in trainer1.team.all_pokemon:
        if pokemon.hp > 0:
            t1_at_least_1_alive = True
            break

    for pokemon in trainer2.team.all_pokemon:
        if pokemon.hp > 0:
            t2_at_least_1_alive = True
            break

    if not t1_at_least_1_alive:
        return trainer2

    elif t2_at_least_1_alive:
        return trainer1

    else:
        return None


def check_effectiveness(move: PKMNMove, pokemon: Pokemon) -> float:
    move_type = move.ptype

