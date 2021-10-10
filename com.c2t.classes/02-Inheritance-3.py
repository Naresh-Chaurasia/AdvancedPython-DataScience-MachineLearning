class Car():
    def startEngine(self):
        print('I am start Engine of Car')

class Maruti(Car):
    def pushButtonStart(self):
        print('I have pushButtonStart functionality')

class BMW(Car):
    def startEngine(self):
        super().startEngine()
        print('I am start Engine of Car, with more horse power')

m = Maruti()
m.startEngine()

b = BMW()
b.startEngine()