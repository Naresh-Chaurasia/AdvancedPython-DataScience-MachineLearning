class Car:
    def __init__(self):
        print('self1=',self)
        self.a = 10


class Maruti(Car):

    def __init__(self):
        #super().__init__()
        print('self2=',self)

c = Car()
m = Maruti()




