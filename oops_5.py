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

    @classmethod
    def from_str(cls,string):
        # params = string.split(" ")
        # return cls(string.split(" ")[0],string(" ")[1],string.split(" ")[2])
        return cls(*string.split(" "))

    @staticmethod
    def printgood(string):
        return f"This is Good {string}"



shivam = Employee("Shivam",455,"Instructer")
larry = Employee("Larry",0,"Student")
karan = Employee.from_str("Karan 200 Worker")

# shivam.name = "Shivam"
# shivam.salary = 455
# shivam.role = "Instructer"

# larry.name = "Rohan"
# larry.salary = 0
# larry.role = "Student"

# print(larry.printdetails())
print(karan.printgood("Karan"))
# print(shivam.printdetails())