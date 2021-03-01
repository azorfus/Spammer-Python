import pyautogui
from time import sleep
import random

# Don't complain about the error thing. i wrote the script in 5 mins for fun purposes. you can modify it
try:
    print("\n\n1) Enter whatever you want!\n2) Random words\n\nPls Keep your cursor where ever you want the bot to type\n\n")

    opt = int(input("$ "))

    timeb = float(input("Enter time in between spam: "))

    longlist = ["hello men", "What is this", "LOL", "LMAO", "KEK", "lame shit", "can i ping you", "Well whatever"]

    if opt == 1:
        enter = str(input("String: "))
        nt = int(input("Times: "))
        print("Get ready. Starting in 2 secs")
        sleep(2)
        for i in range(nt):
            sleep(timeb)
            pyautogui.typewrite(enter)
            pyautogui.typewrite("\n")

    elif opt == 2:
        print("Get ready. Starting in 2 secs")
        sleep(2)
        for i in range(20):
            sleep(timeb)
            choice = random.choice(longlist)
            pyautogui.typewrite(choice)
            pyautogui.typewrite("\n")
except:
    print("\nERROR\n")
