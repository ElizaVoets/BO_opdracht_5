#Imports
import time
#Slow Print
def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.1)
    print("")

#dict

# Main Code
class main:
    def maincode(self):
        s_print("Welcome!")
        time.sleep(0.7)
        s_print("Please fill in your username.")
        time.sleep(0.3)
        s_print("Warning! This cannot be changed later.")
        time.sleep(0.7)
        while True:
            self.username = input("(no spaces):").strip()
            s_print(f"You have selected {self.username} as your username. Is this correct?")
            userconfirm = input("yes or no: ").lower()
            if userconfirm == "yes":
                s_print("Game is starting...")
                print()
                print()
                time.sleep(3)
                scene_1()
                break
            else:
                s_print("Let's redo that then")

        # Scene 1
        def scene_1():
            s_print("SCENE 1: THE INVASION.")
            time.sleep(1)
            print()
            s_print("It's 06:30 as you wake up.")
            time.sleep(0.7)
            s_print("You get up from your bed to grab yourself some warm syrup, and you sit down on your couch as you turn on the TV.")
            time.sleep(0.7)
            s_print("But just as you are about to take a sip, you get interrupted by a knock on your door.")
            s_print(f"Bob: '{self.username}! We have to leave now!'")
            s_print(f"{self.username}: 'Woah, Bob! I am going to need an explaination first.")
            s_print("Bob:")

        def scene_2():
            print()
        def scene_3():
            print()
        def scene_4():
            print()
        def scene_5():
            print()

code = main()
code.maincode