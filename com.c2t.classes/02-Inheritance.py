class Car:
    def startEngine(self):
        print('I am in car startEngine')

class Maruti(Car):
    def display(self):
        print('I am in maruti')

class Huundai(Car):
    def displayHyundai(self):
        print('i am hyundai')

m = Maruti()
m.startEngine()
m.display()

h = Huundai()
h.startEngine()
h.displayHyundai()
