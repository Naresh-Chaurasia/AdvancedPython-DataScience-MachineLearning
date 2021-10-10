class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def __init__(self, year):
        print('------------------')
        self.color = 'red'
        self.y = year

class Maruti(Car):

    def __init__(self, y):
        super().__init__(y)
        print('color=',self.color)
        self.startEngine()
        super().startEngine()

m = Maruti('2018')
print(m.color)
print(m.y)



