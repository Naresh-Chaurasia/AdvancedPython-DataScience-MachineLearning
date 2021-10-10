class Student:
    # class attribute
    trainer = "Naresh Chaurasia"
    
    # Initializer
    def __init__(self,name,course):
        # instance attribute
        print('Inside init')
        self.name = name
        self.course = course
        age = 20

    def displayValues(self):
        print(self.name)
        print(self.course)
        print(self.age)
        print(Student.trainer)
    
s1 = Student('NC','Python')
s1.displayValues()
'''
print(Student.trainer)
print(s1.trainer)
'''


