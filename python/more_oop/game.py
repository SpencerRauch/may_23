from game_classes.cowboy import Cowboy
from game_classes.kickboxer import Kickboxer
import random

cowboy = Cowboy()
kb = Kickboxer()



print('Welcome to Cowboy vs Kickboxer, you are the Cowboy!')
while cowboy.health >= 0 and kb.health >= 0:
    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input("Choose an action \n 1)Attack \n 2)Use Special \n 3)Use Buff \n >>>")
    
    if response == '1':
        cowboy.attack(kb)
    elif response == '2':
        cowboy.use_special(kb)
    else:
        cowboy.use_buff()
    kb_move = random.randint(1,3)
    if kb_move == 1:
        kb.attack(cowboy)
    elif kb_move == 2:
        kb.use_special(cowboy)
    else:
        kb.use_buff()

if cowboy.health > 0:
    print('You win! JD never saw it comin')
elif kb.health <= 0:
    print('it is a draw')
else:
    print('You lose, pilgrim')





    



