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

    print("ARRESTED AT HOME ENDING UNLOCKED.")
    print("DO YOU WANT TO RESTART?:")
    choice = input("> ").strip().lower()
    while True:
        if choice == "y" or choice == "yes":
            startcode()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid Input. Expected: 'y' or 'n'")

def arrested_in_candy_floss_forest():
    print()

def scene_2():
    s_print("[Y/N]: 'Then we will have to leave right now!'")
    s_print("You grab a few things you don't want to leave behind and leave immediately.")
    s_print("[Y/N]: 'How do you even know this?'")
    s_print("[Bob]: 'I overheard a few soldiers talking while I was walking through the town?")
    s_print("both of you make your way to the candy floss forest.")
    s_print("[Bob]: I have never been here before. It's beautiful.")
    s_print("[Y/N]: 'Don't become too attached. We won't ever see this again.")
    s_print("...")
    s_print("[Y/N]: 'Where are we even going?")
    s_print("[Bob]: We'll be going to the human world.")
    s_print("[Y/N]: 'But don't we have to wait one more month?'")
    s_print("[Bob]: 'We have no other choice. Either we get killed here and we will be a waste of food,\n Or we leave early.'")
    s_print("You two walk in silence for a moment. The feeling of sadness and fear is setting in.")
    s_print("You are leaving behind everything you know. The house you have lived you whole life in,\n Your neighbors, Everything.")
    s_print("[Y/N]: 'I'm going to miss home.'")
    s_print("[Bob]: 'Me too, Y/N.'")
    s_print("Soon, you two arrive at a part with three different paths,")
    s_print("The right path looks peacefull, The path infront of you looks very dark and the left path looks normal.")
    s_print("[Bob]: 'Where do we go now?'")
    s_print("You think for a moment, and decide to go..")
    choice = input("left, right, forward or back >").lower().strip()
    while True:
        if choice == "back":
            arrested_in_candy_floss_forest()
        elif choice == "right":
            print()
        elif choice == "left":
            print()
        elif choice == "forward":
            print()
        else:
            print()
    


def scene_3():
    print()

def scene_4():
    print()

def scene_5():
    print()