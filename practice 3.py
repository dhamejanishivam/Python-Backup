while(True) :
    print("Enter the year")

    a = int(input())

    b = a // 4

    c = b * 4

    if a == c:
        print("Yes it is a Leap Year")

    elif a != c:
        print("No it is not a Leap Year")

    else:print("Eror")

    print("Do you want to use it again")
    print("Press 1 for yes and 2 for no")
    d = int(input())

    if d==1 :
        continue

    elif d==2 :
        print("OK")
        break
    else: print("You entered wrong number")

input("Press any key to exit")