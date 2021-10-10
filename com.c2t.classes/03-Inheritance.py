class Car:

    def __init__(self):
        self.color = 'red'

class Maruti(Car):

    def __init__(self):
        super().__init__()
        print('hello')


m = Maruti()
print(m.color)



