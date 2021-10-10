class ShippingContainer:

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents


c = ShippingContainer("BOOKS",["Book1","Book2"])
print(c.owner_code)
print(c.contents)