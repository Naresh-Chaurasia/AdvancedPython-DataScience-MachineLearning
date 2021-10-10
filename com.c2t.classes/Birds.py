class Bird:
    def __init__(self):
        print('i am inside init method of Bird')

    def displayBird(self):
        print('i am a bird')

    def display(self):
        print('i am display method')

class Sparrow():
    def __init__(self):
        super().__init__()
        print('i am inside init method of Sparrows')

#b = Bird()
#b.display()
s = Sparrow()
s.display()
