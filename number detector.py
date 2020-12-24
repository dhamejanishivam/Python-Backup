print("Enter Three Number")

a = int(input())

b = int(input())

c = int(input())

if a>b>=c :
    print("A")

elif a>c>=b :
    print("A")

elif b>a>=c :

    print("B")
elif b>c>=a :
    print("B")

elif c>a>=b :
    print("C")

elif c>b>=a :
    print("C")

else: print("Eror")