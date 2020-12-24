# print("Enter the year")
#
# a = int(input())
#
# b = a//4
#
# c = b * 4
#
# if a==c :
#     print("Yes")
#
# elif a!=c:
#     print("No")
#
#









while (a!=0):
    r = a%10
    rev = rev*10+r
    a = a//10

z = int(rev)
print(z)





# lis = [a ]
print("Enter a no")
a = int(input())

if a%10==0:
    for item in a :
        print(item)

if a%100==0 :
    for item in a :
        print(item)