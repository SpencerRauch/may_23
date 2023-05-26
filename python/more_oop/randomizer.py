import random
import time

groups = [

]

input("Randomizer started. Hit enter to pull up next contestant")
while(len(groups) > 0):
    print("Drum roll please",end="")
    for i in range(5):
        time.sleep(0.5)
        if i <= 3:
            print(". ", end="", flush=True)
        else:
            print(". \n")
    chosen = random.choice(groups)
    groups.remove(chosen)
    print("*" * 20)
    if len(groups) == 0:
        print(f"Lastly, we have {chosen}")
        print("*" * 20)
    else:
        print(f"Hey, Ninja {chosen} you're up!  \n Remaining ninjas: {groups}")
        print("*" * 20)
        input("Again? \n")