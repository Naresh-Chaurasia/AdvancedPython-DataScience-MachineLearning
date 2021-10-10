class Car:
    def __init__(self):
        self.val1 = 10
        self.val2 = 20

    def startEngine(self):
        print('I am in car startEngine')


class BMW(Car):
    def __init__(self):
        super().__init__()
        self.val1 = 100

    def startEngine(self):
        print('I am in car startEngine of BMW')


bmw = BMW()
bmw.startEngine()
print(bmw.val1)
print(bmw.val2)



