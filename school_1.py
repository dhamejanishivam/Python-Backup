a = int(input("Enter how many seconds \n"))
minute = 0
second = 0
c = 0
while c!=a:
    if second==60:
        minute+=1
        second=0
    elif second!=60:
        pass
    second+=1
    c+=1
if minute!=1:
    min_print = "minutes"
elif minute==1 or minute==0 :
    min_print = "minute"
if second!=1:
    sec_print = "seconds"
elif second==1 or second==0 :
    sec_print = "second"
print(f'{minute} {min_print} and {second} {sec_print}')