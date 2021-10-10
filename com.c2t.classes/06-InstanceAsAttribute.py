class Car:
    def startEngine(self):
        print('I am in car startEngine')

class Design:
    def designing(self, c):
        c.startEngine()

c = Car()
d = Design()
d.designing(c)


