from typing import List
from Pokemon import Pokemon


class Trainer:
    """
    A Pokemon Trainer.


    Attributes
    ----------
    team : List[Pokemon]
        A List of all Pokemon on the Trainer's Team.

    Methods
    -------
    show_team(self)
        Displays information about every Pokemon on the team.
    """
    def __init__(self, team: List[Pokemon]) -> None:
        self.team = team

    def show_team(self) -> None:
        """
        Displays information about every Pokemon on the team.
        """
        for pokemon in self.team:
            pokemon.display_stats()
