"""
Question -
Input Dictionary key as key and other details in values in another dictionary
print dictinory in this form -
Name:xyz , Class:xyz, Rollno:xyz
"""
n = int(input("How many values you want to enter \n"))
d = {}
for i in range(n):
    a = input("Enter the Rollno. \n")
    b = input("Enter the Name and class with space\n").split()
    name_class = f"Name : {b[0]} , Class : {b[1]} "
    d[a] = name_class
key_list = []
value_list = []
for key in d.keys():
    key_list.append(key)
for value in d.values():
    value_list.append(value)
e = 0
while True:
    print(value_list[e],end=" , ")
    print(f'Rollno. : {key_list[e]}',end="\n")
    if (len(key_list)-1)==e:
        break
    e+=1