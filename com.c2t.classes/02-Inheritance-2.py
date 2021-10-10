class Car():
    def startEngine(self):
        print('I am start Engine of Car')

class Maruti(Car):
    def pushButtonStart(self):
        print('I have pushButtonStart functionality')

class Zen(Maruti):
    def powerBrakes(self):
        print('powerBrakes')


car = Car()
car.startEngine()

maruti = Maruti()
maruti.pushButtonStart()
maruti.startEngine()

zen = Zen()
zen.startEngine()