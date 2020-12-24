"""
Question -
To count the frequency of given element in list
"""
print(" ")
a = list(map(str,input("Enter the elements of list with space and press enter: \n").split()))
b = input("\nEnter the character of which you want to count frequency of: \n")
c = 0

for item in a:
    if b==item:
        c+=1
    elif b!=item:
        pass
print(f'\nThe frequency of character {b} is {c}')