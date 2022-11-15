from typing import List
from PokedexEntry import PokedexEntry


class Pokedex:
    """
    A repository containing a list of entries defining every Pokemon available
    for simulation.

    Attributes
    ----------
    entries : List[PokedexEntry]
        A List of all PokedexEntries.

    Methods
    -------
    __len__(self)
        Returns the length of the Pokedex.
    """


def __init__(self, entries: List[PokedexEntry]) -> None:
    self.entries = entries


def __len__(self) -> int:
    return len(self.entries)
