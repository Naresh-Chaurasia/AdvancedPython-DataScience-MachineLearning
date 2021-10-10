class Animal():
    def __init__(self, color):
        self.color = color
        self.age = 10
        print('I am Animal form __init__, my color = ', self.color)

    def makeNoise(self):
        print('cat make noise=', self.color)
        print('self.age=', self.age)
        # print('color=', color)
        # print('age=', age)


animal = Animal('red')
animal.makeNoise()
print('animal.color = ', animal.color)
print('animal.age = ', animal.age)