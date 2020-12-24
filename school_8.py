"""
Question -  s = (1)+(1+2)+(1+2+n)
"""
n = int(input("Enter the range \n"))
result = 0
ab=1
adder = 1
for p in range(n):
    for q in range(ab):
        result = result + adder
        adder+=1
    ab+=1
    adder = 1
print(result)

