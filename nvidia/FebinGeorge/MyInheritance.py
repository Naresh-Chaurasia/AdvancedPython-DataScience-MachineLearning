class Furniture:
    color="brown"
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


c = Chair()
c.chairDetails()
c.furnitureDetail()
print(c.color)