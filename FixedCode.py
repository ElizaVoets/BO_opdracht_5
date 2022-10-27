import time



def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.1)
    print("")

def startcode():
    s_print("Welcome!")
    time.sleep(0.7)
    s_print("Please fill in your username.")
    time.sleep(0.3)
    s_print("Warning! This cannot be changed later.")
    time.sleep(0.7)
    s_print("Do you want to start the game?")
    userconfirmation = input("yes or no:")
    while True:
        if userconfirmation == "y" or userconfirmation == "yes":
            print("STARTING GAME . . .")
            time.sleep(1)
            print()
            time.sleep(1)
            print()
            time.sleep(3)
            scene_1()
            break
        else:
            exit()

def scene_1():
    s_print("SCENE 1: THE INVASION.")
    time.sleep(1)
    print()
    s_print("It's 06:30 as you wake up.")
    time.sleep(0.7)
    s_print("You get up from your bed to grab yourself some warm syrup, and you sit down on your couch as you turn on the TV.")
    time.sleep(0.7)
    s_print("But just as you are about to take a sip, you get interrupted by a knock on your door.")
    time.sleep(0.7)
    s_print(f"[Bob]: 'Y/N! We have to leave now!'")
    time.sleep(0.7)
    s_print(f"[Y/N]: 'Woah, Bob! I am going to need an explaination first.")
    time.sleep(0.7)
    s_print("[Bob]: 'There is no time for a long explaination, But the licorice queen is attaching. We need to run!'")
    time.sleep(0.7)
    s_print("You stand there for a moment and just stare at Bob. Do you believe him?")
    while True:
        choice = input("a> 'Oh Ha ha, funny joke Bob. Now let me enjoy my morning in peace.'\nb> 'Then we will have to leave right now!'").lower().strip()
        if choice == "a":
            ArrestedAtHomeEnding()
        elif choice == "b":
            scene_2()
        else:
            print("Invalid input! expected answer is 'a' or 'b'.\n")

def ArrestedAtHomeEnding():
    s_print("[Y/N]:'Oh Ha ha, funny joke Bob. Now let me enjoy my morning in peace.'")
    s_print("[Bob]: 'Y/N, Please belie-'")
    print("SLAM")
    s_print("You slammed the door shut and went back to your couch.")
    s_print("A few moments later you hear a knock on your door once again.")
    s_print("[Y/N]: 'Bob, go away! It's not funny!")
    s_print("...")
    s_print("Suddenly, your door starts shaking.")
    s_print("[Y/N]: 'BOB, YOU ARE GOING TO BREAK MY DOOR!")
    s_print("Just as you finish your sentence, your door breaks down and soldiers come running in.")
    s_print("You realise Bob was not joking and try to make a run for it.\nSadly, you were too late.")
    s_print("you get arrested by soldiers and get killed later.")


def scene_2():
    s_print("[Y/N]: 'Then we will have to leave right now!'")
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()
    s_print()

def scene_3():
    print()

def scene_4():
    print()

def scene_5():
    print()