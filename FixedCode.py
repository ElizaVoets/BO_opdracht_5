import time
import random
import operator
# Endings

# main code
def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.05)
    print("")

def startcode():
    s_print("Welcome!")
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
    time.sleep(2)
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
    time.sleep(0.7)
    s_print("[Bob]: 'Y/N, Please belie-'")
    time.sleep(0.7)
    print("SLAM")
    time.sleep(0.7)
    s_print("You slammed the door shut and went back to your couch.")
    time.sleep(0.7)
    s_print("A few moments later you hear a knock on your door once again.")
    time.sleep(0.7)
    s_print("[Y/N]: 'Bob, go away! It's not funny!")
    time.sleep(0.7)
    s_print("...")
    time.sleep(0.7)
    s_print("Suddenly, your door starts shaking.")
    time.sleep(0.7)
    s_print("[Y/N]: 'BOB, YOU ARE GOING TO BREAK MY DOOR!")
    time.sleep(0.7)
    s_print("Just as you finish your sentence, your door breaks down and soldiers come running in.")
    time.sleep(0.7)
    s_print("You realise Bob was not joking and try to make a run for it.\nSadly, you were too late.")
    time.sleep(0.7)
    s_print("you get arrested by soldiers and get killed later.")
    print()
    time.sleep(0.7)
    print("ARRESTED AT HOME ENDING UNLOCKED.")
    time.sleep(0.7)
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
    time.sleep(0.7)
    s_print("That is, until you notice your foot is stuck.")
    time.sleep(0.7)
    s_print("You look at what is the cause of your foot being stuck and you see your foot melted.")
    time.sleep(0.7)
    s_print("You call out to Bob, and he tries to get ur foot off the ground melting his own hands in the process")
    time.sleep(0.7)
    s_print("You guys are both stuck and left there to rot or melt away.")
    time.sleep(0.7)
    print("MELTED ENDING UNLOCKED")
    time.sleep(0.7)
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
    s_print("[Bob]: 'I overheard a few soldiers talking while I was walking through the town.'")
    time.sleep(0.7)
    s_print("both of you make your way to the candy floss forest.")
    time.sleep(0.7)
    s_print("[Bob]: 'I have never been here before. It's beautiful.'")
    time.sleep(0.7)
    s_print("[Y/N]: 'Don't become too attached. We won't ever see this again.'")
    time.sleep(0.7)
    s_print("...")
    time.sleep(0.7)
    s_print("[Y/N]: 'Where are we even going?'")
    time.sleep(0.7)
    s_print("[Bob]: We'll be going to the human world.'")
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
        choice = input("left, right, forward or back > ").lower().strip()
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
    print("\n\n\nSCENE 3: GINGERBREAD CITY.")
    time.sleep(2)
    s_print("You arrive at Gingerbread city. Everyone there seems to be unaware of the situation.")
    time.sleep(0.7)
    s_print("Everybody is Lunching in cafe's, Walking their gingerbread dogs, and doing whatever they to on a daily basis")
    time.sleep(0.7)
    s_print("[Bob]: 'Do these people not know about what's happening right now?'")
    time.sleep(0.7)
    s_print("[Y/N]: 'Seems like they don't.'")
    time.sleep(0.7)
    s_print("[Bob]: 'Should we warn these people?'")
    choice = input("a) 'We should warn them'\nb) 'They'll figure it out themselfes\n> ").lower()

    if choice == "a":
        s_print("You decide to go to the major of gingerbread city and tell him about the situation.")
        time.sleep(0.7)
        s_print("Just as you finished explaining, everything starts to shake.")
        time.sleep(0.7)
        s_print("You go outside and you see the licorice soldiers attacking the city. You see a building falling.")
        time.sleep(0.7)
        s_print("The problem is, You do not know if it's falling towards, or away from you.. Do you move or not?")
        choice = input("> ").lower()

        if choice == "move":
            s_print("You move away and the building crashes down on the place you were just standing.")
            time.sleep(0.7)
            s_print("[Bob]: 'Y/N! Are you okay?!'")
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
                    scene_4()
           
            elif choice == "n" or choice == "no":
                s_print("You decide to do nothing, but Bob decides to save the child and sucessfully saves her.")
                time.sleep(0.7)
                s_print("The major thanks you and tells you to go towards the cake fields. That is the fastest way to the portal.")
                time.sleep(0.7)
                s_print("You leave the city and make your way to the fields.")
                scene_4()

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

    elif choice == "b":
        s_print("You decide to immediately continue to the next area.")
        time.sleep(0.7)
        s_print("Distant screaming is heard in the distance. Since you didn't warn them, they were met by suprise.")
        scene_4()

def colaharbor():
    s_print("You decide to go to Cola Harbor.")
    time.sleep(0.7)
    s_print("[Bob]: 'We will need to find a boat we can use.'")
    time.sleep(0.7)
    s_print("[Y/N]: 'How about that one?'")
    time.sleep(0.7)
    s_print("You point towards a boat with an engine.")
    time.sleep(0.7)
    s_print("[Bob]: 'That should do.'")
    time.sleep(0.7)
    s_print("You help Fiona get in the boat, and you start the engine")
    time.sleep(0.7)
    scene_5()

def colaharbor_MR():
    s_print("You arrive at Cola Harbor together.")
    time.sleep(0.7)
    s_print("[Licorice]: 'We can take this boat to go towards the island.'")
    time.sleep(0.7)
    s_print("[Y/N]: 'Again, thank you for your help.'")
    time.sleep(0.7)
    s_print("She smiles at you and starts up the engines.")
    time.sleep(0.7)
    scene_5_withlr()

# Halloween city functions
def halloweencity():
    s_print("You arrive in halloween city and get met with licorice soldiers")
    time.sleep(0.7)
    s_print("[Soldier]: 'HALT! You are under arrest.'")
    time.sleep(0.7)
    s_print("Do you fight back?")
    while True:
        choice = input("yes or no > ").lower()
        if choice == "y" or choice == "yes":
            HalloweenCity_minigame()
        elif choice == "n" or choice == "no":
            arrestedInHalloweenCity()
        else:
            s_print("Incorrect input")

def hc_met_rebel():
    s_print("You arrive in halloween city after ignoring the warning and get met with licorice soldiers")
    time.sleep(0.7)
    s_print("[Soldier]: 'HALT! You are under arrest.'")
    time.sleep(0.7)
    s_print("Do you fight back?")
    while True:
        choice = input("yes or no > ").lower()
        if choice == "y" or choice == "yes":
            HCm_met_rebel()
        elif choice == "n" or choice == "no":
            arrestedInHalloweenCity()
        else:
            s_print("Incorrect input")

def HalloweenCity_minigame():
    def math_problems():
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(list(operators.keys()))
        answer = operators.get(operation)(num1, num2)
        if answer >= 0:
            s_print(f"What is {num1} {operation} {num2}?:")
            time.sleep(0.7)

        return answer

    def ask_question():
        answer = math_problems()
        guess = float(input("> "))
        return guess == answer

    def minigame():
        print("HALLOWEEN CITY FIGHT:\n\n")
        score = 0
        correctquestions = 0
        for i in range(15):
            if ask_question() == True:
                s_print("correct answer")
                correctquestions += 1
                time.sleep(0.7)
                s_print(f"{correctquestions} out of 15 answered correctly")
                time.sleep(0.7)
                score += 1
            else:
                    s_print("incorrect!")
            
        if score >= 10:
            s_print("You defeated the Soldiers!")
            post_halloweencityfight()
        elif score >= 5 and score <= 7:
            s_print("You escaped the soldiers!")
            post_halloweencityfight()
        elif score <= 5:
            killedinhalloweencity()

    return minigame()

def HCm_met_rebel():
    def math_problems():
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(list(operators.keys()))
        answer = operators.get(operation)(num1, num2)
        if answer >= 0:
            s_print(f"What is {num1} {operation} {num2}?:")
            time.sleep(0.7)

        return answer

    def ask_question():
        answer = math_problems()
        guess = float(input("> "))
        return guess == answer

    def minigame():
        print("HALLOWEEN CITY FIGHT:\n\n")
        score = 1
        correctquestions = 0
        for i in range(15):
            if ask_question() == True:
                s_print("correct answer")
                correctquestions += 1
                time.sleep(0.7)
                s_print(f"{correctquestions} out of 15 answered correctly")
                time.sleep(0.7)
                score += 1
            else:
                    s_print("incorrect!")
            
        if score >= 10:
            s_print("You defeated the Soldiers!")
            post_halloweencityfight()
        elif score >= 5 and score <= 7:
            s_print("You escaped the soldiers!")
            post_halloweencityfight()
        elif score <= 5:
            killedinhalloweencity()

    return minigame()

def arrestedInHalloweenCity():
    s_print("You decide you cannot fight back and let them arrest you")
    time.sleep(0.7)
    s_print("You get killed by the licorice soldiers.")
    print("\n\n\nARRESTED IN HALLOWEEN CITY.")
    print("DO YOU WANT TO RESTART?")
    while True:
        choice = input("yes or no: ").lower().strip()
        if choice == "y" or choice == "yes":
            s_print("Restarting...")
            time.sleep(3.5)
            scene_1()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid input")
            time.sleep(0.7)

def killedinhalloweencity():
    s_print("The soldiers didn't even arrest you three and killed all of you.")
    print("\n\n\nKILLED IN HALLOWEEN CITY.")
    print("DO YOU WANT TO RESTART?")
    while True:
        choice = input("yes or no: ").lower().strip()
        if choice == "y" or choice == "yes":
            s_print("Restarting...")
            time.sleep(3.5)
            scene_1()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid input")
            time.sleep(0.7)

def scene_4():
    print("\n\n\nSCENE 4: THE CAKE FIELDS")
    time.sleep(2)
    s_print("You two make your way to the cake fields, and after a while of walking you hear a noise.")
    time.sleep(0.7)
    s_print("[Y/N]: 'Did you hear that?'")
    time.sleep(0.7)
    s_print("[Bob]: 'No..? '")
    time.sleep(0.7)
    s_print("You hear another noise and you look behind you.")
    time.sleep(0.7)
    s_print("There is a little gingerbread girl behind you.")
    time.sleep(0.7)
    s_print("The girl gets scared and when she tries to run she trips. The little girl starts crying.")
    time.sleep(0.7)
    s_print("[Y/N]: Hey, hey. Are you okay? We won't hurt you.")
    time.sleep(0.7)
    s_print("[???]: You won't?")
    time.sleep(0.7)
    s_print("[Bob]: Of course we wont!")
    time.sleep(0.7)
    s_print("The girl stops crying and hugs you")
    time.sleep(0.7)
    s_print("[Y/N]: 'What's your name kid? My name is Y/N'")
    time.sleep(0.7)
    s_print("[???]: 'Fiona...'")
    time.sleep(0.7)
    s_print("[Y/N]: 'Your name is Fiona?'")
    time.sleep(0.7) 
    s_print("The little girl nods. She seens very lost and you do not want to leave her here to die.")
    time.sleep(0.7)
    s_print("[Y/N]: 'You can come with us'")
    time.sleep(0.7)
    s_print("[Fiona]: 'Really?'")
    time.sleep(0.7)
    s_print("You nod and gesture her to follow you")
    time.sleep(0.7)
    s_print("After a while of walking you see two cities. On the left is Cola Harbor and on the right is Halloween city.")
    time.sleep(0.7)
    s_print("Between the two cities there is a long road.")
    time.sleep(0.7)
    s_print("Where do you go?:")
    choice = input("a) Cola Harbor\nb) The long road \n c) Halloween City")
    while True:
        if choice == "a":
            colaharbor()
        elif choice == "b":
            s_print("[Bob]: 'Look out! It's a licorice!'")
            time.sleep(0.7)
            s_print("The licorice looks paniced and puts her hands up")
            time.sleep(0.7)
            s_print("[Licorice]: 'WAIT! I come in peace! Please do not hurt me!")
            time.sleep(0.7)
            s_print("You look at the licorice and don't know wether you should trust her or not.")
            time.sleep(0.7)
            s_print("[Y/N]: And how are we supposed to trust you? Your kind has been attacking all of us.")
            time.sleep(0.7)
            s_print("The licorice looks guilty. Tears are about to spill from her eyes.")
            time.sleep(0.7)
            s_print("[Licorice]: 'I know you cannot trust me on my word. My kind's actions are horrible.")
            time.sleep(0.7)
            s_print("She takes a deep breath")
            time.sleep(0.7)
            s_print("[Licorice]: 'Look, I do not agree with the queen and her motives. Please take these weapons for self defence.")
            time.sleep(0.7)
            s_print("She hands you both a knife.")
            time.sleep(0.7)
            s_print("[Licorice]: 'There are licorice soldiers in halloween city, so i reccomend you go to Cola harbor'")
            time.sleep(0.7)
            s_print("It's silent for a moment")
            time.sleep(0.7)
            s_print("[Bob]: 'Should we trust her?'")

            while True:
                choice = input("a) 'We'll trust you. Thank you for the help'\nb) 'I do not trust you at all. We are going to halloween city.'")
                if choice == "a":
                    s_print("[Y/N] 'We'll trust you. Thank you for the help'")
                    time.sleep(0.7)
                    s_print("[Licorice]: 'No problem. I'll walk with you guys'")
                elif choice == "b":
                    s_print("[Y/N]: 'I do not trust you at all. We are going to halloween city.'")
                    time.sleep(0.7)
                    s_print("[Licorice]: 'I warned you..'")
                    hc_met_rebel()
        elif choice == "c":
            halloweencity()

def post_halloweencityfight():
    print()

def scene_5():
    print("")
    time.sleep(0.7)
    s_print("You sail across the sea while bob keeps an eye on any land.")
    time.sleep(0.7)
    s_print("You decide to take a nap and close your eyes")
    time.sleep(3)
    s_print("zZz...")
    time.sleep(2)
    s_print("[Bob]: 'Y/N! Wake up!'")
    time.sleep(0.7)
    s_print("You get woken up by Bob shaking you awake.")
    time.sleep(0.7)
    s_print("[Y/N]: '*yawn* ..What is it?")
    time.sleep(0.7)
    s_print("[Fiona]: 'We have arrived!'")
    time.sleep(0.7)
    s_print("You look up to see the huge sour roll road with the portal all the way at the very end.")
    time.sleep(0.7)
    s_print("[Y/N]: 'This is it.. We are safe!'")
    time.sleep(0.7)
    s_print("And just as you said that, another ship aproaches.")
    time.sleep(0.7)
    s_print("You look a little better and see that it's a ship filled with licorice soldiers and no one other than the queen herself.")
    time.sleep(0.7)
    s_print("[Licorice Queen]: 'GET THEM!'")
    ending()

def scene_5_withlr():
    print("")
    time.sleep(0.7)
    s_print("You sail across the sea, the licorice rebel making sure the fastest way there is taken.")
    time.sleep(0.7)
    s_print("You decide to take a nap and close your eyes")
    time.sleep(3)
    s_print("zZz...")
    time.sleep(2)
    s_print("[Bob]: 'Y/N! Wake up!'")
    time.sleep(0.7)
    s_print("You get woken up by Bob shaking you awake.")
    time.sleep(0.7)
    s_print("[Y/N]: '*yawn* ..What is it?")
    time.sleep(0.7)
    s_print("[Fiona]: 'We have arrived!'")
    time.sleep(0.7)
    s_print("You look up to see the huge sour roll road with the portal all the way at the very end.")
    time.sleep(0.7)
    s_print("[Y/N]: 'This is it.. We are safe!'")
    time.sleep(0.7)
    s_print("And just as you said that, another ship aproaches.")
    time.sleep(0.7)
    s_print("You look a little better and see that it's a ship filled with licorice soldiers and no one other than the queen herself.")
    time.sleep(0.7)
    s_print("[Licorice Queen]: 'GET THEM!'")
    ending()

def killedonsourrollroad():
    s_print("You arent fast enough and you all get killed on the spot.")
    print("\n\n\nKILLED ON SOUR ROLL ROAD.")
    print("DO YOU WANT TO RESTART?")
    while True:
        choice = input("yes or no: ").lower().strip()
        if choice == "y" or choice == "yes":
            s_print("Restarting...")
            time.sleep(3.5)
            scene_1()
        elif choice == "n" or choice == "no":
            exit()
        else:
            print("Invalid input")
            time.sleep(0.7)

def finalminigame():
    def math_problems():
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(list(operators.keys()))
        answer = operators.get(operation)(num1, num2)
        if answer >= 0:
            s_print(f"What is {num1} {operation} {num2}?:")
            time.sleep(0.7)

        return answer

    def ask_question():
        answer = math_problems()
        guess = float(input("> "))
        return guess == answer

    def minigame():
        print("HALLOWEEN CITY FIGHT:\n\n")
        score = 0
        secondscore = 0
        correctquestions = 0
        for i in range(15):
            if ask_question() == True:
                s_print("correct answer")
                correctquestions += 1
                time.sleep(0.7)
                s_print(f"{correctquestions} out of 15 answered correctly")
                time.sleep(0.7)
                score += 1
            else:
                s_print("incorrect!")
            
        if score >= 7:
            s_print("You were fast enough and ran through the portal")
            time.sleep(0.7)
            s_print("You let Fiona go through first, then bob and you go through last.")
            time.sleep(0.7)
            s_print("And then it all goes black")
            time.sleep(0.7)
            s_print("The last thing you see is plastic.")
            time.sleep(0.7)
            s_print("Not soon after, you get picked up and eaten by little timmy on the playground")

            print("\n\nYOU WON!")
            time.sleep(0.7)
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            while True:        
                choice = input("yes or no: ").lower().strip()
                if choice == "yes" or choice == "y":
                    s_print("Restarting...")
                    time.sleep(3)
                    print("\n\n\n\n")
                    startcode()
                elif choice == "no" or choice == "n":
                    print("Thank you for playing!")
                    time.sleep(0.7)
                    exit()
                else:
                    print("Invalid input")
                    time.sleep(0.7)
            
        elif score >= 5 and score <= 7:
            s_print("You werent fast enough, but can still fight them to escape.")
            for i in range(15):
                if ask_question() == True:
                    s_print("correct answer")
                    correctquestions += 1
                    time.sleep(0.7)
                    s_print(f"{correctquestions} out of 15 answered correctly")
                    time.sleep(0.7)
                    secondscore += 1
                else:
                    s_print("incorrect!")

            if secondscore == 5 or secondscore >= 3:
                s_print("You kill the soldiers and quickly escape.")
                time.sleep(0.7)
                s_print("You let Fiona go through first, then bob and you go through last.")
                time.sleep(0.7)
                s_print("And then it all goes black")
        elif score <= 5:
            killedonsourrollroad()

    return minigame()

def ending():
    s_print("You quickly pick up Fiona and You and Bob start running")
    time.sleep(0.7)

    finalminigame()
    
startcode()