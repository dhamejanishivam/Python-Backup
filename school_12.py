"""
Question -
Check if a number is palindrome
"""
a = int(input("Enter the number \n"))
b = []
for p in str(a):
    if p!="0":
        b.append(p)
    else:pass
rev = 0
while a!=0 :
    c = a%10
    rev = rev*10 + c
    a = a // 10
d = []
for q in str(rev):
    d.append(q)
if b==d :
    print("The number is Palindrome")
else: print("The number is not Palindrome")