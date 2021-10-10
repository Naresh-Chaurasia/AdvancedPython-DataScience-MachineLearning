class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.color = 'black'
        print('self = ',self)
        print('type(self) = ', type(self))

    def display(self):
        print('self.name=', self.name)
        print('self.age=', self.age)
        print('self.color=', self.color)

d = Dog('tommy',10)
print(d.color)

d.display()