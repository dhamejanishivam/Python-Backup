a = int(input("Enter the number \n"))
isPrime = bool(False)
i = 1
while i!=a :
    if a%i==0:
        if i!=1 and i!=a  :
            isPrime = True
        else:
            pass
    i+=1
if isPrime==True :
    print("Entered Number is not a prime number")
else :
    print("Entered number is prime number")