# My number reverser -

# print("Enter a number")
# a = int(input())
# r = 0
# c = []
# while(a!=0):
#     b = a%10
#     c.append(b)
#     a = a//10
# print(c)

# Mohit's number reverser -

print("Enter a number")

a = int(input())
rev = 0
while(a!=0):
    b = a%10
    rev = rev * 10 + b
    a = a//10

print(rev)
