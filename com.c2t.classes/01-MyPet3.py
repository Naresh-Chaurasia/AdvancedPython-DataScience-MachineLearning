class Animal():

    def __init__(self):
        self.name = 'tommy'
        self.age = 5
        print('welcome to init')

    def makeNoise(self):
        print('self=',self)



dog1 = Animal()
print(dog1.name)
print(dog1.age)

