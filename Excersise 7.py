"""
9am - 5pm
water reminder = It will play "water.mp3" He has to give input that he drank to stop water.mp3    [in every 40 minutes to drink a 250 ml glass of water]
a log will saved it will contain that he drank water and a time stamp


eyes = eye reminder will remid person to do eye excersise in every 30 minutes
it will play eyes.mp3   he has to give input done to stop it


physical activity = reminder every 45 minutes
and it will play physical.mp3
"""


print("Welcome to Healthy Programmer's program")
print("  \n")
print("Every input should be small")
import pygame
import time
import datetime
from pygame import mixer

# eye.mp3 = maharani
# water.mp3 = awien hai
# physical.mp3 = seedha makeover

def getdate():
    import datetime
    return datetime.datetime.now()

z = str(getdate())


def allinone():
    time.sleep(1800)
    mixer.init()
    mixer.music.load("eye.mp3")
    mixer.music.set_volume(100)  # No effect
    mixer.music.play()

    print("  \n")
    print("Playing eye.mp3   \n"
          "                     \n"
          "Do some EYE excersise  \n"
          "\n")

    print(" ")
    print("If you did eye excersise  \n"
          "Press any key \n")

    a = input()
    if a == "y":
        print("Stopping music")
        mixer.music.stop()


    else:
        print("Stopping music")
        mixer.music.stop()


    time.sleep(600)  #  It is 600 [We need 2400 here] and because above time is 1800 so 600 + 1800 = 2400
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(100)  # No effect
    mixer.music.play()

    print("  \n")
    print("Playing Water.mp3   \n"
          "                     \n"
          "Go and drink a glass of water \n"
          "\n")

    print(" ")
    print("If you drinked a glass of water \n"
          "Press any key \n")

    a = input()

    if a == "y":
        print("Stopping music")
        mixer.music.stop()
        b = open("water.txt", "a")
        y = b.write("Drank water at  ")
        x = b.write("  ")
        w = b.write(z)
        v = b.write(" \n")

    else:
        print("Stopping music")
        mixer.music.stop()
        b = open("water.txt", "a")
        y = b.write("Drank water at  ")
        x = b.write("  ")
        w = b.write(z)
        v = b.write(" \n")
        b.close()


    time.sleep(300)  # It  is 300 [We need 2700 here] and because above total time is 2400 sec so 2400 + 300 = 2700 sec
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.set_volume(100)  # No effect
    mixer.music.play()
    print("  \n")
    print("Playing Physical.mp3   \n"
          "                     \n"
          "Go and do some excersise \n"
          "\n")
    print(" ")
    print("If you did Excersise  \n"
          "Press any key \n")
    a = input()

    if a == "y":
        print("Stopping music")
        mixer.music.stop()


    else:
        print("Stopping music")
        mixer.music.stop()


if __name__ == '__main__':
    print("Name is  " , __name__)

    while(True) :
        print("Hi")
        print("   \n")

        allinone()











