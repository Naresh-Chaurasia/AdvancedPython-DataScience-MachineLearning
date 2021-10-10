class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def __init__(self, y):
        self.color = 'red'
        self.year = y

class Maruti(Car):

    def __init__(self, year):
        super().__init__(year)
        print('I am in maruti')
        print('color=',self.color)
        self.power = '220cc'

class BMW(Car):
    def startEngine(self):
        print('I am in car startEngine of BMW')




bmw = BMW()



