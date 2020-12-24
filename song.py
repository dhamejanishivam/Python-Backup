from pygame import mixer
from win32com.client import Dispatch
import time


def ai(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)
i = 0

while (True):
    if i < 1:
        ai("Welcome to song player")
    else:
        pass
    print("Select song from the list \n"
          ""
          "1 for awien_hai \n"
          "2 for chenni khatam \n"
          "3 for maharani \n"
          "4 for makasam \n"
          "5 for seedha makeover \n"
          "6 for mujhe farak nahi pada \n"
          "7 for laugh now - Drake \n"
          "8 for gods_plan \n"
	  "9 for ghaziabad \n"
	  "10 for nike \n"
          "p for pausing the music \n"
          "r for resuming the music \n"
          "s to stop music  \n")
    if i < 1:
        ai("Select which song you want to play from list")
    else:
        pass
    a = input()
    if a == "1":
        mixer.init()
        mixer.music.load("awien_hai.mp3")
        mixer.music.play()
    elif a == "2":
        mixer.init()
        mixer.music.load("chenni_khatam.mp3")
        mixer.music.play()
    elif a == "3":
        mixer.init()
        mixer.music.load("maharani.mp3")
        mixer.music.play()
    elif a == "4":
        mixer.init()
        mixer.music.load("makasam.mp3")
        mixer.music.play()
    elif a == "5":
        mixer.init()
        mixer.music.load("seedha_makeover.mp3")
        mixer.music.play()
    elif a == "6":
        mixer.init()
        mixer.music.load("mujhe_farak.mp3")
        mixer.music.play()
    elif a == "7":
        mixer.init()
        mixer.music.load("drake_laugh_now.mp3")
        mixer.music.play()
    elif a == "8":
        mixer.init()
        mixer.music.load("gods_plan.mp3")
        mixer.music.play()
    elif a=="9" :
        mixer.init()
        mixer.music.load("ghaziabad_vasudev.mp3")
        mixer.music.play()
    elif a=="10" :
        mixer.init()
        mixer.music.load("nike_vasudev.mp3")
        mixer.music.play()
    elif a == "p":
        mixer.init()
        mixer.music.pause()
        ai("Music paused")
    elif a == "r":
        mixer.init()
        ai("Resuming music")
        mixer.music.unpause()
    elif a == "s":
        mixer.music.pause()
        ai("Music Stopped")
        break
    i += 1