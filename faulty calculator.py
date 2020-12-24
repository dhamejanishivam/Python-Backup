

while(True):

      d = input("Do you want to calculate  \n"
            "press 1 for yes \n"
            "press 2 for no \n")

      if d==1 :
            continue

      if d==2 :
            break
            print("Ok")

      print("Enter two numbers ")
      a = float(input())

      b = float(input())


      print("Type for \n"
      "1   / \n"
      "2   *  \n"
      "3   + \n"
      "4   - \n"
      "5   ^ \n"
      "6   % , a = natural number , b = how much %")
      c = int(input())

      if c==1 :
            print(a/b)

      elif c==2 :
            print(a*b)

      elif c==3 :
            print(a+b)

      elif c==4 :
            print(a-b)

      elif c==5 :
            print(a^b)

      elif c==6 :
            print(a*b/100)

      else: print("Your entered choice is wrong")

