# from game_classes import fighter
from game_classes.fighter import Fighter


class Kickboxer(Fighter):
    def __init__(self):
        super().__init__()
        self.name = "Van Damme"
        self.agility += 8
        self.special = "The Splits"
        self.buff = "Defensive Stance"

    def use_special(self, target):
        target.defend(self.agility)
        print(f"{self.name} does the splits and it's amazing!")

    def use_buff(self):
        self.defense += 2
        print(f'{self.name} uses {self.buff} ')
        print(f'Defense raised to {self.defense}')


