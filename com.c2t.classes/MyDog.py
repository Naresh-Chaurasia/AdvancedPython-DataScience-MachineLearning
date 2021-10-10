class Dog():
    def __init__(self,age, breed):
        print('i am init method')
        print('self=',self)
        self.age = age
        self.breed = breed
        
    def bark(self):
        print('i can bark')
        print('self.breed=',self.breed)
        print('self.age=',self.age)
        
        

d = Dog(5,'dogs')
d.bark()
print('d=',d)