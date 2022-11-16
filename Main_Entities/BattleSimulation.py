from Trainer import Trainer


class BattleSimulation:
    def __init__(self, trainer1: Trainer, trainer2: Trainer, trainer1AI: bool,
                 trainer2AI: bool, trainer1AIPolicy, trainer2AIPolicy) -> None:

        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.trainer1AI = trainer1AI
        self.trainer2AI = trainer2AI
        self.trainer1AIPolicy = trainer1AIPolicy
        self.trainer2AIPolicy = trainer2AIPolicy

    def play_turn(self):
        pass


