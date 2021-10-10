class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def __init__(self, msg2):
        print('init of Car')
        self.a = msg2

    def method_super(self, val2):
        print('val2=',val2)
        print('id(val2)=', id(val2))

class Maruti(Car):

    def __init__(self,msg):
        super().__init__(msg)
        #print('super=',super)
        print('init of Maruti')

    def method_sub(self, val):
        print('id(val)=',id(val))
        print('self.a=', self.a)
        super().method_super(val)
        b = 20


m = Maruti('hello maruti')
m.method_sub(10)





