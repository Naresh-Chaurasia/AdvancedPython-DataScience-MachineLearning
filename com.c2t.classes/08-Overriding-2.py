class Animal():
    def __init__(self):
        self.color = 'red'
    
    def sound(self):
        print('Animal sound...')
        print('self.color in Animal=',self.color)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('init of Dog...')
        self.color = 'black'

    def dogSound(self):
        print('self.color in Dog=', self.color)

    def sound(self):
        super().sound()
        print('Dog sound...')
        print('self.color in Animal=',self.color)

d = Dog()
d.sound()
#print(d.color)