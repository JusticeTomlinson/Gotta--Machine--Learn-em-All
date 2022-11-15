from typing import List
from Pokemon import Pokemon


class Team:
    """
    A Team of Pokemon.


    Attributes
    ----------
    all_pokemon : List[Pokemon]
        A List of all Pokemon on the team.

    Methods
    -------
    show_team(self, all_pokemon)
        Displays information about every Pokemon on the team.
    """
    def __init__(self, all_pokemon: List[Pokemon]) -> None:
        self.all_pokemon = all_pokemon


