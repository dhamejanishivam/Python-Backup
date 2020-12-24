import time
import datetime
from pygame import mixer

print("Welcome To 20 minutes alarm  \n"
      "                            ")

def my_alarm():
    print("Alaram is starting \n")
    print("It will ring after 20 minutes \n")
    time.sleep(300)
    print("5 minutes completed 15 minutes to alarm")
    time.sleep(300)
    print("10 minutes completed 10 minutes to alarm")
    time.sleep(300)
    print("15 minutes completed 5 minutes to alarm")
    time.sleep(300)
    print("Playing alarm")
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play()
    print("If you want to stop alarm \n"
          "Press any key \n")
    a = input()

    if a=="y":
        print("Ok , Stopping the alarm \n"
              "The alarm will play after 20 minutes \n")
        mixer.music.stop()

    else :
        print("Ok , Stopping the alarm \n"
              "The alarm will play after 20 minutes \n")
        mixer.music.stop()



while(True) :

    my_alarm()