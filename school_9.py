"""
Question -
x + (x^2/2) + (x^n/n)
x and n are input
"""
print(2+(2**2/2)+(2**3/3)+(2**4/4))
x = int(input("Enter the number \n"))
n = int(input("Enter the range \n"))
result = 0
ab = 1
for p in range(n):
    for q in range(1):
        result = result + (x**ab/ab)
    ab+=1
print(result)