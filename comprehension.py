# make list of no. /3 to 100

# List comprehension starts here -

# ls = [i for i in range(100) if i%3==0 ]


# print(ls)

# List comprehension ends here.



# ls = []
# for i in range(100) :
#     if i%3==0 :
#         ls.append(i)




#
# dic = []
# i = 0
# for i in range(100) :
#     a = f"item{i}"
#     b = dic.append(f"{i}:{a}")
#     i += 1
# print(dic)



# Dictonary comprehension starts -

# dict1 = {i:f"item{i} "  for i in range(100) if i%100=0}
dict1 = {i:f"item{i} "  for i in range(10)}
dict2 = {value:key for key, value in dict1.items()}
print(dict2)


# Genrator  -

even = (i for i in range(100) if i%2==0 )
print(type(even)) # Type = genrator
print(even.__next__())
print(even.__next__())


