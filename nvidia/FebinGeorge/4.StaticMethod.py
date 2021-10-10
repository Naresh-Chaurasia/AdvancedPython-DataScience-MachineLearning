class Employee:
    def employeeDetails(self):
        print(self)

    @staticmethod
    def printWelcomeMessage():
        print('Hello World')


employee = Employee()

'''
employee.employeeDetails()
Employee.employeeDetails(employee)
'''

employee.printWelcomeMessage()

