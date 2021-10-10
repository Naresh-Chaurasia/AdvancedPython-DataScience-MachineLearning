class Animal():
    def __init__(self,color):
        self.color = color
        print('i am Animal init method') 
    
    def sound(self):
        print('i am Animal')

class Dog(Animal):
    def __init__(self,age, breed, color):
        super().__init__(color)
        print('i am Dog init method')
        print('self=',self)
        self.age = age
        self.breed = breed
        
    def bark(self):
        print('i can bark')
        print('self.breed=',self.breed)
        print('self.age=',self.age)
        print('self.color=',self.color)
        
d = Dog(5,'dogs','red')
d.bark()
print('d.color=',d.color)
d.sound()
