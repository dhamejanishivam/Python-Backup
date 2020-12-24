print("Enter the total amount of purchase")

a = float(input())

if a<=1000 :
    print("Sorry Discount is not available on purchase of less than 1000/- ")
    print("But a Dairy Milk is free")

elif a<=5000 :
    print("10 % Discount ")
    print("On a purchase of",a)
    print("Total Amount is")
    print(a- a/10)

elif a<=10000 :
    print("20 % Discount")
    print("Total Amount is")
    print(a - a/5)

elif a>10000 :
    print("25 % Discount")
    print("Total amount is ")
    print(a - a/4)

else: print("Eror")

