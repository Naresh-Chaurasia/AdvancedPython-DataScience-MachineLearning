class Pet():
    def __init__(self):
        print('self=',self)

    def setValues(self, name, age):
        self.name = name
        self.age = age

    def displayValues(self):
        print('self.name=',self.name)
        print('self.age=',self.age)

p = Pet()
#p.setValues('tommy',10)
p.displayValues()