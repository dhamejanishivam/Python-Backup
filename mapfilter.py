# numbers = ["3" , "34" , "64"]
# numbers = list(map(int,numbers)) #This func. changes all element of list to another element
#
# for i in range(len(numbers)) :
#     numbers[i] = int(numbers[i])
#
# numbers[1] = numbers[1] + 2
# print(numbers[2])
#
#
# def sq(a) :
#     return a*a,
# num = [2,4,5,6,8,9]
# square  = list(map(sq,num))
# print(square)


# square = lambda a:a*a
#
# cube = lambda b:b*b*b
#
#
# func = [square , cube]
#
# num = [2,4,5,6,8,9]
#
# for i in range(5) :
#     val  = list(map(lambda x:x(i) , func))
#     print(val)


# list_1  = [2,4,5,6,8,9]
# def great(num) :
#     return num>5

# Filter function =

# gr_5 = list(filter(great , list_1))
# print(gr_5)



from functools import reduce

list_1  = [1,2,3,4]


# num = 0
# for i in list_1 :
#     num = num + i

num = reduce(lambda a,b: a+b , list_1)

print(num)

