#   for loop can stop by two ways

#  1st way  -

lis  = ["1" , "2" , "3" , "4"]
for i in lis :
    print(i)
else:
    print("This is 1st way to end for loop  \n"
          "In this way for loop end by itself")
#  In this way for loop ended by itself , because all item from -
#  - list were finite in number and printed

#  2nd way -

for i in lis :
    if i=="4" :
        break
else: print("This for loop is stopped by a 'break' statement")


# Above for loop is stopped by a 'break' statement.