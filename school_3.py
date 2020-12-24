a = input("Enter The Character \n")

if a.isupper():
    print("Your entred character is Upper case")
elif a.islower():
    print("Your entred character is Lower case")
elif a.isnumeric():
    print("Your entred character is Number")
else:
    print("Your entred character is Special Character")
