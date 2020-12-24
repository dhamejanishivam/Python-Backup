inp1 = int(input("Enter your first number: "))
inp2 = int(input("Enter your second number: "))
inp3 = int(input("Enter your third number: "))
if inp1 < inp2 <= inp3:
    print(inp1,"is the smallest.")
if inp2 < inp1 <= inp3:
    print(inp2,"is the smalest. ")
if inp3 < inp2 <= inp1:
    print(inp3,"is the smallest.")
if inp3 < inp1 <= inp2:
    print(inp3,"is the smallest.")
if inp2 < inp3 <= inp1:
    print(inp2,"is the smallest.")
if inp1 < inp3 <= inp2:
    print(inp1,"is the smallest.")
if inp1==inp2>inp3 :
    print("Number 1 and Number 2 are same and greator than Number 3")
if inp1==inp3>inp2:
    print("Number 1 and Number 3 are same and greator than Number 2")
if inp2==inp3>inp1:
    print("Number 2 and Number 3 are same and greator than Number 1")
input()

