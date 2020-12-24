"""
Question 20 -
To create a dictinory and input name of competition winner as key and their number of wins as values
"""
a = {}
b = int(input("How many values would you like to enter \n"))
for i in range(b):
    c,d = str(input("Enter the name of competitor ")),int(input("Enter their number of wins "))
    a[c] = d
KEY = []
VALUE = []
for key in a.keys():
    KEY.append(key)
for value in a.values():
    VALUE.append(value)
e = 0
while True:
    if e==0:
        print("")
    print(KEY[e],end=" ")
    print(f"won {VALUE[e]} times ")
    if (len(KEY)-1)==e:
        break
    e+=1