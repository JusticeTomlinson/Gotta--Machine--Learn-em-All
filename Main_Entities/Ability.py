

class Ability:
    """
    The ability of a pokemon.


    Attributes
    ----------
    name : str
        The name of the Ability.
    description : str
        A decription of the Ability.
.
    Methods
    -------
    show_item(self)
        Prints the Ability name and what the Ability does.
    """
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def show_item(self) -> None:
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.description}")
        print({'-'*40})
