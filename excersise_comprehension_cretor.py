# Not able to make

# List or Dictionary or set

# List = []
# Dictionary = {}
# Set =

print("How many items you want to insert ")
a = int(input())

print("What comprehension do you want to make \n"
      "Press 1 for list \n"
      "Press 2 for Dictionary \n"
      "Press 3 for Set \n")
e = int(input())


if e==1 :
    f = []
    for c in range(a):
        print("Enter item \n")
        d = input()
        f.append(d)
    print(f)
elif e==2 :
    f={}
    for c in range(a):
        print("Enter item \n")
        d = input()

    print(f)



