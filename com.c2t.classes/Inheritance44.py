class Animal:
    var = 'cat'
    
    def __init__(self):
        print('I am Animal')
    
    def makeNoise(self):
        print('cat make noise')
        #self.var = 'cat modified'
        print(__class__.var)


class Dog(Animal):
    def __init__(self):
        #super().__init__()
        print('I am Dog')    
        
animal = Animal()
animal.makeNoise()

    
'''        
myCat = Dog()
myCat.makeNoise()
print('myCat.var=',myCat.var)
print('myCat.__class__.var=',myCat.__class__.var)
print("Class cat is {}".format(myCat.__class__.var))
'''

