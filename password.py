
def pass1(a):
    import random as r
    if a==4 :
        b = r.randint(1000,9999)
        print("Password of 4 digit is ", b)
    elif a==5 :
        b = r.randint(10000, 99999)
        print("Password of 5 digit is ", b)
    elif a==6 :
        b = r.randint(100000, 999999)
        print("Password of 6 digit is ", b)
    else: print("Sorry, your entered choice is wrong")

print("Name is " , __name__)
if __name__ == '__main__':  # I we import above function so below part will not be imported

    print("How many digits of password do you want")
    print("Enter any number from 4 to 6")

    a = int(input())
    pass1(a)