# imports:
# Needed for slow_print
import time
# Needed to run scene 1
import os

# Prints the string letter by letter. Is used like a print statement.
def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.1)
    print("")

# Player enters username
def username():
    while True:
        s_print("Welcome!")
        time.sleep(0.7)
        s_print("Please fill in your username.")
        time.sleep(0.3)
        s_print("Warning! This cannot be changed later.")
        time.sleep(0.7)
        username = input("(no spaces):").strip()
        s_print(f"You have selected {username} as your username. Is this correct?")
        userconfirm = input("yes or no: ").lower()
        if userconfirm == "yes":
            os.system('python Scene1.py')

print(username())