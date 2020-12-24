"""
Question -
To find the second highest number in list
"""

a = list(map(int,input("\nEnter the number with space and press enter: \n").split()))
b = max(a)
while max(a)==b:
    a.remove(b)
print(f"\nThe second highest number in list is {max(a)} \n")