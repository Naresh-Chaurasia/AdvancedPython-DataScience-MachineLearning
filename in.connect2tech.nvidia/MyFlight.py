class Flight:
    def __init__(self,name):
        self.name = name

    def fly(self):
        print('id(self)=',id(self))
        print('self.name=',self.name)

f = Flight('NVIDIA')

'''
f.fly()

print('id(f)=',id(f))
print('f.name=',f.name)
'''

print(type(f))