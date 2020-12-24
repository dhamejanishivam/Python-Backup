"""
Question -
Input two Tuple and create a new tuple that contains all element of first tuple followed by second
"""
a = tuple(map(str,input("\nEnter the elements of Tuple A with space and press enter : \n").split()))
b = tuple(map(str,input("\nEnter the elements of Tuple B with space and press enter : \n").split()))
d = list()
for p in b:
    d.append(p)
for q in a:
    d.append(q)
e = tuple(d)
print(e)