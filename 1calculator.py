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
        print("Answer is" , a / b)

    elif c == 2:
        print("Answer is" ,a * b)

    elif c == 3:
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


input("Press any key to exit")