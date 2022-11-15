

class Ability:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def show_item(self) -> None:
        print({'-'*40})
        print(f"Item: {self.name}")
        print(f"Effect: {self.description}")
        print({'-'*40})
