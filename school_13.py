"""
Question -
To find if a number is Armstrong or not
"""
a = int(input("Enter the number \n"))
c = a
result = 0
while a!=0 :
    b = a%10
    b = b**3
    result = result+b
    a = a//10
if c==result:
    print("Your entered number is Armstrong number \n")
else:
    print("Your entered number is not a Armstrong number \n")
