class student :
    def pd(self):
        return 

shivam = student()
bkl = student()

shivam.name = "Shivam"
shivam.std = 11
shivam.section = "A"
shivam.subject = ["CS" , "Maths" , "Physics"]

bkl.name = "Bhen_ka_lawda"
bkl.std = "Galli hai ye , koi student nahi"

print(shivam.subject)
print(bkl.name)
print(bkl.std)

print(shivam.__dict__) # This will print all details for name entered


