# 50+98 = 138
# 60*73 = 5500
# 59/19 = 5


while (True):
    print("Enter two number")
    a = int(input())
    b = int(input())
    print("Type for \n"
      "1   / \n"
      "2   *  \n"
      "3   + \n"
      "4   - \n"
      "5   ^ \n")




    c = int(input())
    if c == 1:
        if a==59 :
            if b==19 :
                print("5")
                continue
        print("Answer is" , a / b)

    elif c == 2:
        if a==60 :
            if b==73 :
                print("5500")
                continue

        print("Answer is" ,a * b)

    elif c == 3:
        if a==50 :
            if b==98 :
                print("138")
                continue
        print("Answer is" ,a + b)

    elif c == 4:
        print("Answer is" ,a - b)

    elif c == 5:
        print("Answer is" ,a ^ b)

    else: print("The number you entered is wrong")


    print("Do you want to calculate again")
    print("Press y for yes and n for no")
    d = input()

    if d=="n" :
        print("OK Exitting")
        break

    if d=="N":
        print("Ok Exitting")
        break

    elif d=="y" :
        continue

    else :
        print("Eror")


