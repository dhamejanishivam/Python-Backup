from win32com.client import Dispatch
def ai(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)



ai("Welcome to Rock Paper Sicsor Game \n"
   "Enjoy the game")

import random
list1 = ["rock" , "paper" , "scisor"]
a = random.choice(list1)
# print(a)
print('Welcome this is Rock Paper Scisor game')

while(True):
    # i = 0
    # i = i + 1
    print("Please type all thing in small leter \n")
    print("Press r for rock \n"
          "Press p for paper \n"
          "Press s for scisor \n"
          "")
    b = input()
    # print(a)
    if a=="rock" :
        if b=="r" :
            print("Both are same , Rock")
            break

