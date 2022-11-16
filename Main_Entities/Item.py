class Item:
    """
    An item that can be held by a Pokemon.


    Attributes
    ----------
    name : str
        The name of the Ability.
    description : str
        A description of the Item.
.
    Methods
    -------
    show_item(self)
        Prints the Item name and what the Item does.
    """

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def show_item(self) -> None:
        """
        Prints the Item name and what the Item does.
        """
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.description}")
        print({'-'*40})
