class Pokedex:
    def __init__(self, entries: List[PokedexEntry]) -> None:
        self.entries = entries

    def __len__(self) -> int:
        return len(self.entries)
