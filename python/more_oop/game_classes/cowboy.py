import random
from game_classes.fighter import Fighter

class Cowboy(Fighter):
    def __init__(self):
        super().__init__()
        self.name = "John Wayne"
        self.buff = "YeeHaww"
        self.special = "Six shooter attack"

    def use_special(self,target):
        chance = random.randint(1,2)
        if chance > 1:
            print(f'Lucky hit! {self.name} fires twice')
            target.defend(10)
            target.defend(10)
        else:
            print(f'{self.name} fires once')
            target.defend(10)

    def use_buff(self):
        print(f'{self.name} screams YEEEHAWWW!')
        self.strength += 3
        print(f'{self.name} is fired up, strength up by 3, it is now {self.strength}')