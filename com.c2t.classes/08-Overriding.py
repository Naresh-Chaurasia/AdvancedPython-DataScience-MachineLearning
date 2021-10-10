class Animal():
    def __init__(self,color):
        self.color = color
    
    def sound(self):
        print('Animal sound...')

class Dog(Animal):
    def __init__(self,age, breed, color):
        super().__init__(color)
        #self.color = 'yellow'

    def sound(self):
        print('Dog sound...')
        #self.sound()
        
d = Dog(5,'dogs','red')
d.sound()
print(d.color)
