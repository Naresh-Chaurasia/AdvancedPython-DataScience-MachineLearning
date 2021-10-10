class Car:
   def __init__(self):
       print('I am Car')
       self.a = 10

   def m1_Car(self):
        print('m1_Car')

class Maruti(Car):
    def __init__(self):
        super().__init__()
        print('I am Maruti')
        #self.m1_Car()
        #super().m1_Car()

    def m1_Car(self):
        print('m2_Car')

m = Maruti()
print(m.a)


