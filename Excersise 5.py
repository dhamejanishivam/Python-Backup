# Health Management System
#  Name are =  shivam , manu , harshu
while (True) :
    print("Welcome to health managment program")
    print("Do you wan to save data or retrive data")
    print("Press 1 for saving \n"
          "Press 2 for retriving\n")
    def getdate():
        import datetime
        return datetime.datetime.now ()
    b = getdate()
    p = str(b)
    # print(b) , print this to get date time
    a = int(input())
    if a==1:
        print("OK")
        print("Press 1 for Shivam \n"
              "Press 2 for Manu \n"
              "Press 3 for Harshu \n")
        c = int(input())
        print("Do you want to save in Excersise or Diet")
        print("Press 1 for excersise \n"
              "Press 2 for Diet \n")
        g = int(input())
        if c == 1 :
            if g==1 :
                d = open("shivamgym.txt" , "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you did")
                # print("Enter Time = " , b)
                e = input()
                # y = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
            if g==2 :
                d = open("shivamdiet.txt", "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you Ate")
                # print("Enter Time = ", b)
                e = input()
                # y = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
        elif c == 2 :
            if g==1 :
                d = open("manugym.txt", "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you did")
                # print("Enter Time = ", b)
                e = input()
                # y = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
            if g==2 :
                d = open("manudiet.txt", "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you Ate")
                # print("Enter Time = ", b)
                e = input()
                # y = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
        elif c==3 :
            if g==1 :
                d = open("harshugym.txt", "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you did")
                # print("Enter Time = ", b)
                e = input()
                # y = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
            if g==2 :
                d = open("harshudiet.txt", "a")
                # print(d.read(),        b)
                print()
                print()
                print()
                print("Enter what you Ate")
                e = input()
                f = d.write(e)
                v = d.write("  ")
                z = d.write(p)
                w = d.write("\n")
                d.close()
    if a==2 :
        print("Press 1 for Shivam \n"
              "Press 2 for Manu \n"
              "Press 3 for Harshu \n")
        k  = int(input())
        if k==1 :
            print("Do you want to retrive data of gym or diet")
            print("Press 1 for Gym \n"
                  "Press  2 for Diet \n")
            l = int(input())
            if l==1 :
                m = open("shivamgym.txt")
                print(m.read())
            if l==2 :
                n = open("shivamdiet.txt")
                print(n.read())
                n.close()
        elif k==2 :
            print("Do you want to retrive data of gym or diet")
            print("Press 1 for Gym \n"
                  "Press  2 for Diet \n")
            l = int(input())
            if l == 1:
                m = open("manugym.txt")
                print(m.read())
            if l == 2:
                n = open("manudiet.txt")
                print(n.read())
                n.close()
        elif k==3 :
            print("Do you want to retrive data of gym or diet")
            print("Press 1 for Gym \n"
                  "Press  2 for Diet \n")
            l = int(input())
            if l == 1:
                m = open("harshugym.txt")
                print(m.read())
            if l == 2:
                n = open("harshudiet.txt")
                print(n.read())
                n.close()
        else : print("Eror in line 180")
    print("Do you want to enter or retrive anything again")
    print("Press 1 for yes \n"
          "Press 2 for no \n")
    t = int(input())
    if t==1 :
        print("OK")
        continue
    elif t==2 :
        print("Ok Exitting")
        break
    else: print("Eror in line 197")