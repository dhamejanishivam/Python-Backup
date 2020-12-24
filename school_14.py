"""
Question -
To capitlise every other letter on string
Example =  passion becomes pAsSiOn
"""


a = input("Enter the String you want to capitalise \n")
b = 0
lis = []
for item in a:
    if b%2!=0:
        item = item.upper()
        lis.append(item)
    elif b%2==0:
        lis.append(item)
    b+=1
for items in lis :
    print(items,end="")

