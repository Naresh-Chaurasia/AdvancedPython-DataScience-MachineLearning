# Exhibiting that one method is overriden and other is inherited
class Car:
    def startEngine(self):
        self.power = 100

    def printEngine(self):
        print('printEngine::', self.power)

class Maruti(Car):
    def startEngine(self):
        print('startEngine2')
        self.power = 200

    def engineReset(self):
        super().startEngine()

        

c = Car()
c.startEngine()
c.printEngine()

c2 = Maruti()
c2.startEngine()
c2.printEngine()
c2.engineReset()
c2.printEngine()
    
