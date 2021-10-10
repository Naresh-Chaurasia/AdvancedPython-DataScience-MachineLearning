class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def method_super(self, val2):
        print('val2=',val2)
        print('id(val2)=', id(val2))

class Maruti(Car):

    def method_sub(self, val):
        print('id(val)=',id(val))
        print('self.a=', self.a)
        super().method_super(val)
        b = 20


m = Maruti('hello maruti')
m.method_sub(10)





