from Trainer import Trainer

SWAP = 'swap'
ATTACK = 'attack'


class BattleSimulation:
    def __init__(self, trainer1: Trainer, trainer2: Trainer, trainer1AI: bool,
                 trainer2AI: bool, trainer1AIPolicy, trainer2AIPolicy) -> None:

        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.trainer1AI = trainer1AI
        self.trainer2AI = trainer2AI
        self.trainer1AIPolicy = trainer1AIPolicy
        self.trainer2AIPolicy = trainer2AIPolicy

    def play_turn(self) -> None:
        t1_move = self.trainer1.determine_action()
        t2_move = self.trainer2.determine_action()

        t1_moved = False
        t2_moved = False


        if t1_move == ATTACK and t2_move == ATTACK:
            if self.trainer1.team.all_pokemon[0].speed > self.trainer2.team.all_pokemon[0].speed:
                self.trainer1.attack()

                if self.trainer2.team.all_pokemon[0].hp <= 0:
                    self.trainer2.team.all_pokemon[0].status
                self.trainer2.attack()
            elif self.trainer1.team.all_pokemon[0].speed < self.trainer2.team.all_pokemon[0].speed:

            else:

        elif t1_move == ATTACK and t2_move == SWAP:

        elif t1_move == SWAP and t2_move == ATTACK:

        elif t1_move == SWAP and t2_move == SWAP:
            self.trainer1.ad_hoc_swap_pokemon()
            self.trainer2.ad_hoc_swap_pokemon()



    # p2_move =








