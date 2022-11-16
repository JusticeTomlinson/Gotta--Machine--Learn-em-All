from typing import List

from Main_Entities.Battle_Entities.TeamBE import TeamBE
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
    def __init__(self, team: TeamBE) -> None:
        self.team = team

    def show_team(self) -> None:
        """
        Displays information about every Pokemon on the team.
        """
        for pokemon in self.team.all_pokemon:
            pokemon.display_stats()

    def determine_action(self):
        pass

    def attack(self, attack_policy, target) -> None:
        pass

    def ad_hoc_swap_pokemon(self, swap_policy, opponent_pokemon):
        pass



