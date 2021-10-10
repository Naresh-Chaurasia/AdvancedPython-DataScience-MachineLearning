class Car:
    def startEngine(self):
        print('I am in car startEngine')

class Design:
    def callCar(self):
        c1 = Car()
        c1.startEngine()

c = Car()
d = Design()
d.callCar()




