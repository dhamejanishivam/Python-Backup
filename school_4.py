"""
Question -
To print factorial of number n
"""
a = int(input("Enter the number you want to calculate Fctorial of \n"))
b = 1
result = 1
while b<=a :
    result = result * b
    b+=1
print(result)