# print("Making functon")
# a = int(input())
#
# b = int(input())

def my(a,b) :
    """This function calculate your percent by entering the numbers obtained out of 80 """
    c = (a+b)
    d = c *100/160
    return d

print(my.__doc__)

print(my(float(input()),float(input())))
