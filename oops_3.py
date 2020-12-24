import os
class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


shivam = Employee("Shivam",455,"Instructer")
larry = Employee("Larry",0,"Student")
# shivam.name = "Shivam"
# shivam.salary = 455
# shivam.role = "Instructer"
# larry.name = "Rohan"
# larry.salary = 0
# larry.role = "Student"
print(larry.printdetails())
os.system("cls")
print(shivam.printdetails())