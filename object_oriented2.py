class Employee :
    working_hours = 8
    pass

shivam = Employee()
larry = Employee()

print(shivam.working_hours)
print(Employee.working_hours)
print(larry.working_hours)

shivam.working_hours = 9  # It will create a instance variable of shivam
# But it will not change  Employee.working_hours = 9

print(shivam.working_hours)