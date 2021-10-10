class ClassObjects:
    def __init__(self):
        print('Inside __init__')
        self.name = 'Naresh'

obj1 = ClassObjects()
print(obj1.name)

obj1.course = 'Python'
print(obj1.course)