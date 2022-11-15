class Item:

    def __init__(self, name: str, effect: str) -> None:
        self.name = name
        self.effect = effect

    def show_item(self) -> None:
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.effect}")
        print({'-'*40})
