from secrets import choice
import time



def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.05)
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
    s_print("[Bob]: 'There is no time for a long explaination, But the licorice queen is attacking. We need to run!'")
    time.sleep(0.7)
    s_print("You stand there for a moment and just stare at Bob. Do you believe him?")
    while True:
        choice = input("a> 'Oh Ha ha, funny joke Bob. Now let me enjoy my morning in peace.'\nb> 'Then we will have to leave right now!'\n").lower().strip()
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
    s_print("You decide to go back to see if there is another road")
    time.sleep(0.7)
    s_print("After walking for a bit, you two encounter licorice guards, and they immediately knock you two out")
    time.sleep(0.7)
    print("ARRESTED IN CANDY FLOSS FOREST UNLOCKED.")
    print("DO YOU WANT TO RESTART?:")
    choice = input("> ").strip().lower()
    while True:
        if choice == "y" or choice == "yes":
            startcode()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid Input. Expected: 'y' or 'n'")

def meltedEnding():
    s_print("after a while of walking, you step in something. You don't think much of it.")
    s_print("That is, until you notice your foot is stuck.")
    s_print("You look at what is the cause of your foot being stuck and you see your foot melted.")
    s_print("You call out to Bob, and he tries to get ur foot off the ground melting his own hands in the process")
    s_print("You guys are both stuck and left there to rot or melt away.")
    print("MELTED ENDING UNLOCKED")
    print("DO YOU WANT TO RESTART?:")
    choice = input("> ").strip().lower()
    while True:
        if choice == "y" or choice == "yes":
            startcode()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid Input. Expected: 'y' or 'n'")    

def scene_2():
    s_print("[Y/N]: 'Then we will have to leave right now!'")
    time.sleep(0.7)
    s_print("You grab a few things you don't want to leave behind and leave immediately.")
    time.sleep(0.7)
    s_print("[Y/N]: 'How do you even know this?'")
    time.sleep(0.7)
    s_print("[Bob]: 'I overheard a few soldiers talking while I was walking through the town.")
    time.sleep(0.7)
    s_print("both of you make your way to the candy floss forest.")
    time.sleep(0.7)
    s_print("[Bob]: I have never been here before. It's beautiful.")
    time.sleep(0.7)
    s_print("[Y/N]: 'Don't become too attached. We won't ever see this again.")
    time.sleep(0.7)
    s_print("...")
    time.sleep(0.7)
    s_print("[Y/N]: 'Where are we even going?")
    time.sleep(0.7)
    s_print("[Bob]: We'll be going to the human world.")
    time.sleep(0.7)
    s_print("[Y/N]: 'But don't we have to wait one more month?'")
    time.sleep(0.7)
    s_print("[Bob]: 'We have no other choice. Either we get killed here and we will be a waste of food,\n Or we leave early.'")
    time.sleep(0.7)
    s_print("You two walk in silence for a moment. The feeling of sadness and fear is setting in.")
    time.sleep(0.7)
    s_print("You are leaving behind everything you know. The house you have lived you whole life in,\n Your neighbors, Everything.")
    time.sleep(0.7)
    s_print("[Y/N]: 'I'm going to miss home.'")
    time.sleep(0.7)
    s_print("[Bob]: 'Me too, Y/N.'")
    time.sleep(0.7)
    s_print("Soon, you two arrive at a part with three different paths,")
    time.sleep(0.7)
    s_print("The right path looks peacefull, The path infront of you looks very dark and the left path looks normal.")
    time.sleep(0.7)
    s_print("[Bob]: 'Where do we go now?'")
    time.sleep(0.7)
    s_print("You think for a moment, and decide to go..")
    walkedincircle = 0
    while True:
        choice = input("left, right, forward or back >").lower().strip()
        if choice == "back":
            arrested_in_candy_floss_forest()
        elif choice == "right":
            s_print("You decide to go right and you walk around in a circle")
            walkedincircle = walkedincircle + 1
            if walkedincircle == 3:
                arrested_in_candy_floss_forest()
        elif choice == "left":
                s_print("You go left and after a while of walking the smell of gingerbread cookies greets you.")
                scene_3()
        elif choice == "forward":
                s_print("You decide to go forward")
                meltedEnding()
        else:
            print("Invalid Input!")
    

def scene_3():
    s_print("You arrive at Gingerbread city. Everyone there seems to be unaware of the situation.")
    s_print("Everybody is Lunching in cafe's, Walking their gingerbread dogs, and doing whatever they to on a daily basis")
    s_print("[Bob]: 'Do these people not know about what's happening right now?'")
    s_print("[Y/N]: 'Seems like they don't.'")
    s_print("[Bob]: 'Should we warn these people?'")
    choice = input("> ").lower()
    if choice == "yes":
        s_print("You decide to go to the major of gingerbread city and tell him about the situation.")
        s_print("Just as you finished explaining, everything starts to shake.")
        s_print("You go outside and you see the licorice soldiers attacking the city. You see a building falling.")
        s_print("The problem is, You do not know if it's falling towards, or away from you.. Do you move or not?")
        choice = input(">").lower()
        if choice == "move":
            s_print("You move away and the building crashes down on the place you were just standing.")
            s_print("[Bob]: 'Y/N! Are you okay??'")
            s_print("[Y/N]: 'I'm fine..'")

    elif choice == "no":
        s_print()
def scene_4():
    print()

def scene_5():
    print()

startcode()