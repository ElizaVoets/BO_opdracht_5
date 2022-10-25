import time
#Prints string letter by letter
def s_print(string):
    for char in string:
        print(char, end='', flush=True,)
        time.sleep(0.1)
    print("")

def firstscene():
    s_print("It's 06:30 as you wake up.")
    time.sleep(0.7)
    s_print("You get up from your bed to grab yourself some warm syrup, and you sit down on your couch as you turn on the TV.")
    time.sleep(0.7)
    s_print("But just as you are about to take a sip, you get interrupted by a knock on your door.")