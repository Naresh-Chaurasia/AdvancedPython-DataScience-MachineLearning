class Furniture:
    color="brown"

    publicAttribute='I am Public'
    _protectedAttribute = 'I am Protected'
    __privateAttribute = "I am Private"

    def __init__(self):
        print('Inside __init__ @Furniture')
    
    def furnitureDetail(self):
        print('furnitureDetail')

class Chair(Furniture):
    
    def __init__(self):
        print('Inside __init__ @Chair')
        self.chairColor="brownish"

    def chairDetails(self):
        print('self.chairColor=',self.chairColor)
        print('self.color=',self.color)
        print('Furniture.color=',Furniture.color)

    def displayAttributes(self):
        print('self._protectedAttribute',self._protectedAttribute)
        print('self.__privateAttribute',self._Furniture__privateAttribute)

fur = Furniture()
c = Chair()
# c.chairDetails()
# c.furnitureDetail()
# print(c.color)
c.displayAttributes()
#print(c._Furniture__privateAttribute)