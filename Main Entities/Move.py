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

