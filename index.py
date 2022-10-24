# Inputs
from operator import truediv
from time import sleep

# Prints text letter for letter
def fprint(txt):
    for char in txt:
        print(char, end="", flush= True)
        sleep(0.1)

#Lists:
possible_endings = ["ARRESTED AT HOME", "LOST IN CHOCOLATE FOREST"]
unlocked_endings = [""]


active = True



#Endings
def firstdeath():
    fprint("You do not believe Bob and laugh at him.")
    sleep(0.7)
    fprint(" : 'Nice joke Bob! I'll see you later.")
    sleep(1.5)
    fprint("\n A few minutes later some knocks down your door and pins you to the floor.")
    sleep(0.7)
    print("GAME OVER! THE LICORICE QUEEN ARRESTED AND KILLED YOU!")
    sleep(0.7)
    if "ARRESTED AT HOME" not in unlocked_endings:
        print("ENDING UNLOCKED: ARRESTED AT HOME")
        unlocked_endings.append(possible_endings.pop(0))

# Non-death options

def believed():
    sleep(0.7)
    fprint("\nyou look at Bob for a second and immediately put down your cup.")
    sleep(0.7)
    fprint()
        

#scenes 
def firstscene():
    fprint("You wake up like you usually do at 6:30 AM.")
    sleep(0.7)
    fprint("\nJust as you are about to grab your delicious cup of warm syrup, Someone knocks on your door")
    sleep(0.7)
    fprint("\nIt's your friend, Bob.")
    sleep(0.7)
    fprint("\nBob: 'We have to leave now! The licorice queen is attacking!'")
    fprint("\nDo you believe him or not?")
    choice_believe = input("\n> Believe or don't believe: ").lower
    if choice_believe == "believe":
        believed()
    elif choice_believe == "don't believe":
        firstdeath()

    while active == True:
        firstscene()