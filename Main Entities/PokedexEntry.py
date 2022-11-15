class PokedexEntry:
    def __init__(self, number: int, name: str, description: str, height: float,
                 weight: float, base_stats: List[float]) -> None:
        self.number = number
        self.name = name
        self.description = description
        self.height = height
        self.weight = weight
        self.base_stats = base_stats
