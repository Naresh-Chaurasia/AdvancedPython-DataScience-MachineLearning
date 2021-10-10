class Animal():

    def makeNoise(self):
        #self.age = 2
        name = 'tommy'
        print('make noise')
        #print('self.age=',self.age)

    def eat(self):
        print('eating')
        print(self.age)


dog = Animal()
dog.makeNoise()
#print('dog.age=',dog.age)
print(dog.name)
#dog.eat()

