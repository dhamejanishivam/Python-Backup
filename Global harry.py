# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)

# l = 10
#
# def func1 (n):
#      # l = 5
#      m = 8
#      global l
#      l = l + 45
#      print(l , m)
#      print(n  , "I have printed")
#
# func1("This is me")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # a = 1
# # # print("Enter a number")
# # # b = int(input())
# # a = int(input("Enter first number"))
# # b = int(input("Enter second number"))
# #
# #
# # def func(a,b) :
# #
# #     if a==b :
# #
# #         return  print("a = b")
# #     elif a!= b :
# #         return print("a is  not equal to b")
# #
# #
# # func(a , b)
# # # func(a,b)
# # # c = int(input("Enter a number"))
# # # d = int(input("Enter another number"))
# #
# # # func(c,d)
#
#
#
#
#
#
