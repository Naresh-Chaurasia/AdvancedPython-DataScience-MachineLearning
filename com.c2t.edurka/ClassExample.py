class Animal():
    def setName(self, n):
        self.name = n
        print(self.name)

a = Animal()
a.setName('James')
print(a.name)