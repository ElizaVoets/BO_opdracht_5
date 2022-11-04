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
            scene_1()
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
            scene_1()
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
            scene_1()
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
    print("SCENE 3: GINGERBREAD CITY.")
    time.sleep(0.7)
    s_print("You arrive at Gingerbread city. Everyone there seems to be unaware of the situation.")
    time.sleep(0.7)
    s_print("Everybody is Lunching in cafe's, Walking their gingerbread dogs, and doing whatever they to on a daily basis")
    time.sleep(0.7)
    s_print("[Bob]: 'Do these people not know about what's happening right now?'")
    time.sleep(0.7)
    s_print("[Y/N]: 'Seems like they don't.'")
    time.sleep(0.7)
    s_print("[Bob]: 'Should we warn these people?'")
    choice = input("> ").lower()

    if choice == "yes":
        s_print("You decide to go to the major of gingerbread city and tell him about the situation.")
        time.sleep(0.7)
        s_print("Just as you finished explaining, everything starts to shake.")
        time.sleep(0.7)
        s_print("You go outside and you see the licorice soldiers attacking the city. You see a building falling.")
        time.sleep(0.7)
        s_print("The problem is, You do not know if it's falling towards, or away from you.. Do you move or not?")
        choice = input(">").lower()

        if choice == "move":
            s_print("You move away and the building crashes down on the place you were just standing.")
            time.sleep(0.7)
            s_print("[Bob]: 'Y/N! Are you okay??'")
            time.sleep(0.7)
            s_print("[Y/N]: 'I'm fine..'")
            time.sleep(0.7)
            s_print("Just as you say that, you notice another building falling towards a little gingerbread girl.")
            time.sleep(0.7)
            s_print("Do you save her?")
            choice = input("> ").lower()

            if choice == "y" or choice == "yes":
                s_print("You run towards the child, but now you have to decide if you push her forward or pull her back.")
                time.sleep(0.7)
                s_print("Do you push or pull?")
                choice = input("> ").lower
            elif choice == "n" or choice == "no":
                s_print("You decide to do nothing, but Bob decides to save the child and sucessfully saves her.")
                time.sleep(0.7)
                s_print("The major thanks you and tells you to go towards the cake fields. That is the fastest way to the portal.")
                time.sleep(0.7)
                s_print("You leave the city and make your way to the fields.")
                scene_4()
                
                if choice == "push":
                    s_print("You push the girl away from the building, but realise you dont have enough time to get away.")
                    time.sleep(0.7)
                    s_print("You get crushed by the building and die.")
                    time.sleep(0.7)
                    print("\nCRUSHED BY A BUILDING WHILE SAVING A CHILD ENDING UNLOCKED!")
                    time.sleep(0.7)
                    print("DO YOU WANT TO RESTART?")
                    while True:
                        if choice == "y" or choice == "yes":
                            scene_1()
                        elif choice == "n" or choice == "no":
                            exit()
                        else:
                            print("Invalid Input. Expected: 'y' or 'n'")
                if choice == "pull":
                    s_print("You save both yourself and the girl. The whole town starts cheering and the major thanks you.")
                    s_print("He tells you the quickest way to the portal is through the cake fields")
        elif choice == "don't move":
            s_print("You decide to stay where you are. Wrong choice, the building crushes you.")
            time.sleep(0.7)
            print("\nCRUSHED BY BUILDING ENDING UNLOCKED")
            time.sleep(0.7)
            print("DO YOU WANT TO RESTART?")
            while True:
                if choice == "y" or choice == "yes":
                    scene_1()
                elif choice == "n" or choice == "no":
                    exit()
                else:
                    print("Invalid Input. Expected: 'y' or 'n'")

    elif choice == "no":
        s_print("You decide to immediately continue to the next area.")
        time.sleep(0.7)
        s_print("Distant screaming is heard in the distance. Since you didn't warn them, they were met by suprise.")
        scene_4()
def scene_4():
    print("While you two make your way over the cake fields you notice a gingerbread child following you. You talk to her and get to know her. You find out her name is Fiona you two decide to take her with you to the human world. After a while of you three walk over the cake fields you see two different cities Either you can go to Cola harbor, Halloween city or you can go in between them. If you go to Cola harbor you can take the ship to the portal, if you go to Halloween City, you encounter licorice soldiers and you will have to fight them. (see Halloween City Fight) If you go between them you have to walk around and you come across a licorice soldier. Surprisingly, she means no harm. She disagrees with the queen’s motives and is currently hiding from the queen. She tells you that if you want to leave candy land you need to go through cola harbor. You can trust her. If you don’t and you go to Halloween city instead you get met with soldiers Here you have to fight them. ")
    print("In halloween city you were supposed to have a small minigame, which i couldnt make because of a lack of time.")
    scene_5()
def scene_5():
    print("You leave to get to the island with the portal. During the trip you can see Swedish fish in the ocean and a lot of other gummy sea creatures. Once you arrive at the island you see another ship approaching. Infront of you is a giant sour roll that is all rolled out, forming a road. You have to run. Every answer that is answered correctly gives you more speed. If you answer at least 7 of the 15 questions correct you escape the soldiers. If you get 5 or 6 out of 15 right, you have to fight them. If you get less than 5 right, you get killed on the spot. Once you outrun the soldiers you arrive at the portal. You let Bob and Fiona go through first and then you go through. You wake up in a pack of gummy bears and you get eaten last. that is the good ending")

startcode()