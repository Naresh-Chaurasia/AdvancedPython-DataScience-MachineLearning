class Car:
    def startEngine(self):
        print('I am in car startEngine')

    def __init__(self):
        print('init of Car')
        self.a = 10
        print('self1=',self)


class Maruti(Car):

    def __init__(self):
        super().__init__()
        #print('super=',super)
        print('init of Maruti')
        print('self.a=',self.a)
        print('self2=',self)
        self.b = 100


#c = Car()
#print(c.a)


# c = Car()
# print('c=',c)
#
# print('------------------------------')

m = Maruti()
# print('m=',m)
# print('m.a=',m.a)
# print(m.b)



