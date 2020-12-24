print("Total number of tries are 9")
a = 18
c = 0
while(True) :
    b = int(input("Guess the number \n"))
    c = c + 1

    if b==a :
        print("You won the game \n"
              "Your score is ", 9 - c)

        break

    print("Your total number of tries left are  = ",9-c)

    if c==9 :
        print("Game over ")
        break

    if b > a :
        print("Your number is greater \n")
        continue

    if b < a :
        print("Your number is smaller \n ")
        continue


