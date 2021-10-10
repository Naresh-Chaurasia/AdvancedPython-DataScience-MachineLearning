# Class Attributes. Accessing with Class Name and Instance of Class

class Employee:
    # Define an attribute called name
    name = "Ben"

    def changeName (self):
        # Change the value of the attribute within a method
        Employee.name = "Mark"

print('-----------------------------------')
print(Employee.name)
employee = Employee()
print(employee.name)
employee.changeName()
print(employee.name)
print('-----------------------------------')
print(type(employee))

