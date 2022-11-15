from typing import List


class PokedexEntry:
    """
    Contains the a repository of information about a given Pokemon.

    Attributes
    ----------
    number : int
        The number assigned to the Pokemon entry.
    name : str
        The name of the Pokemon.
    description : str
        A decription of the Pokemon.
    height : float
        The height in feet of a Pokemon.
    weight : float
        The weight in pounds of a Pokemon.
    base_stats : List[float]
        The base stats of the given Pokemon.
    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes

    """
    def __init__(self, number: int, name: str, description: str, height: float,
                 weight: float, base_stats: List[float]) -> None:
        self.number = number
        self.name = name
        self.description = description
        self.height = height
        self.weight = weight
        self.base_stats = base_stats
