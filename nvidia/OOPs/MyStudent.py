class Student:
    # class attribute
    trainer = "Naresh Chaurasia"
    
    # Initializer
    def __init__(self,name,course):
        # instance attribute
        print('Inside init')
        self.name = name
        self.course = course
        self.age = 20

    def displayValues(self):
        print(self.name)
        print(self.course)
        print(self.age)
        print(Student.trainer)
    
    # Static Method
    @staticmethod
    def staticMethod():
        print('I am staticMethod')

    # Constructor
    @classmethod
    def classMethod(cls,n,c):
        print('classMethod')
        #print(cls)
        cls(n,c)

        print(cls.trainer)


'''
s1 = Student('NC','Python')
s1.displayValues()
print(Student.trainer)
print(s1.trainer)
'''

#Student.staticMethod()

obj = Student.classMethod('nares','python')

