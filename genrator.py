
def gen(n):
    for i in range(n):
        yield i

a = gen(10)
print(a.__next__())
print(a.__next__())



# while(True):
#     b+=1
#     print(a.__next__())
#     if b>9  :
#         break