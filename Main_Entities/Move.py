class PKMNMove:
    """
    A Pokemon Trainer.


    Attributes
    ----------
    name : str
        The name of the Pokemon Move.
    description : str
        A description of what the Move does.
    base_damage : float
        The amount of damage the Move does before factoring in stat boosts and
        type advantage.
    accuracy : float
        The accuracy of a given move.
    status_type : str
        The type of status that the Move may inflict.
    status_chance : float
        The chance that the Move will inflict the status.
    pp : int
        The amount of uses a move has.

    Methods
    -------
    """
    def __init(self, name: str, description: str, base_damage: float,
               ptype: str, accuracy: float, status_type: str,
               status_chance: float, pp: int):
        self.name = name
        self.description = description
        self.base_damage = base_damage
        self.ptype = ptype
        self.accuracy = accuracy
        self.status_type = status_type
        self.status_chance = status_chance
        self.pp = pp

