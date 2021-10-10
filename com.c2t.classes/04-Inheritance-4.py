class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def method1(self, val1):
        print('val1=',val1)
        print('id(val1)=', id(val1))
        self.method2(val1)
        print('val1=',val1)

    def method2(self, val2):
        print('val2=', val2)
        print('id(val2)=', id(val2))
        val2 = 500


m = Car()
x = 10
print('id-x',id(x))
m.method1(x)






