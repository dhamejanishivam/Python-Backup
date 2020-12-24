n = int(input("Enter the range \n"))
x  = int(input("Enter the value of x \n"))
total = 0
multi=x
i = 0
while i!=n :
    total = total + multi
    multi=multi*x
    i+=1
print(f'Answer is {total+1} \n')