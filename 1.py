print("Enter three number")
num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 > num2 :
    if num1 > num3 :
        print("1")

elif num2 > num1 :
    if num2 > num3 :
        print("2")


elif num3 > num1 :
    if num3 > num2 :
        print("3")
else: print("Eror")




