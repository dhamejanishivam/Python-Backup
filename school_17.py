"""
Question -
Input two tupples a and b and check if every item of a is in b
"""
a = tuple(map(str,input("\nEnter the elements of Tuple A with space and press enter : \n")))
b = tuple(map(str,input("\nEnter the elements of Tuple B with space and press enter : \n")))
check = all(item in b for item in a)
if check is True:
    print("Yes")
else:
    print("No")