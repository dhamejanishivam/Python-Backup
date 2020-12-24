# class student:
#     pass
#
# shivam = student()
# larry = student()
#
# shivam.name = "Shivam"
# shivam.std = 11
# shivam.section = 2
#
# print(shivam)


class Employee:
    no_of_leaves = 10

shivam = Employee()
larry = Employee()

shivam.name = "Shivam"
shivam.salary = 455
shivam.role = "Instructer"

larry.name = "Rohan"
larry.salary = 0
larry.role = "Student"

# print(shivam.no_of_leaves)

Employee.no_of_leaves = 9 # To change a variable defined in class we have to use class name
print(larry.no_of_leaves)
print(larry.__dict__) # It print all variable of object in form of dictinary



