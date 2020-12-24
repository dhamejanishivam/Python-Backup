# a = open("shivam.txt", "w")
# a.write("Thanos was right")
# a.close()

# file creator  -
# a = open("enter new file name here", "w")
# if you want to write anything in file -
# a.write("write here you want to write in file")
# a.close

print("File creator by input")
print("\"Enter file name to create\".txt")
a = input()
b = open(a,"w")
print("Enter what you want to write in file")
c = input()
b.write(c)
b.close()
input("Press any key to exit")

# a = open("shivam.txt","r+")
# print(a.read())
# b = a.write("Avenger won \n")
# a.close()


