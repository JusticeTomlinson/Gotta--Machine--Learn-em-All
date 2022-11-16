from typing import List, Union

from Main_Entities import Team
from Main_Entities.Battle_Entities.PokemonBE import PokemonBE
from Main_Entities.Pokemon import Pokemon


class TeamBE(Team.Team):

    def __init__(self, all_pokemon: Union[Pokemon, PokemonBE]) -> None:
        super().__init__(all_pokemon)

