# Rock paper sicsor game
# 1 = rock
# 2 = paper
# 3 = sicsor
from win32com.client import Dispatch



def ai(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


print("This is Rock Paper Scisor Game \n")
i  = 0
z = 0  # z is  number of time you win
y = 0
while i < 10 :
    i = i + 1
    print("Total tries left =", 10 - i)
    import random
    print("The number of time you win =", z )
    print("The number of times computer win =", y)
    print(" ")
    # print("The number of time you win ", z)
    list1 = ["1", "2", "3"]
    a = random.randint(1,3)
    # print(a)
    # input()
    print("Press 1 for rock \n"
          "Press 2 for paper \n"
          "Press 3 for siscor \n")
    b = int(input())
    if b==1 :
        print("Your choice is Rock \n")
        if a==1 :
            print("Computer's choice is Rock ")
            print("Both are same \n")
            continue
        elif a==2 :
            y = y + 1
            print("Computer's choice is Paper ")
            print("You lose \n")
            ai("You lose")
            continue
        elif a==3 :
            z = z + 1
            print("Computer's choice is Sicsor ")
            print("You win \n")
            ai("You win")
            continue

    elif b==2 :
        print("Your choice is paper \n")
        if a==1 :
            z = z + 1
            print("Computer's choice is Rock")
            print("You win \n")
            ai("You win")
            continue
        elif a==2 :
            print("Computer's choice is Paper")
            print("Both are same \n")
            continue
        elif a==3 :
            y = y + 1
            print("Computer's choice is Sicsor")
            print("You lose \n")
            continue
    elif b==3 :
        print("You choice is scisor \n")
        if a==1 :
            y = y + 1
            print("Computer's choice is Rock")
            print("You lose \n")
            continue
        elif a==2 :
            z = z + 1
            print("Computer's choice is Paper")
            print("You win \n")
        elif a==3 :
            print("Computer's choice is Scisor")
            print("Both are same \n")
            continue
    else :
        print("You entered a wrong choice or EROR \n")



print("The number of times you won " , z)
print("The number of times computer won",y)

if z>y :
    print('Game Over \n'
          'You won \n')
elif y>z :
    print('Game Over \n'
          'You lose \n')
elif y==z :
    print('Game Over \n'
          'Tie between you and computer \n')
else: print("  \n"
            "  \n")


input("Press any key to exit")

