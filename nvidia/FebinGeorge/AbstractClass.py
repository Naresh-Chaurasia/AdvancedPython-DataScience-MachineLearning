from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    
    @abstractmethod
    def area(self):
        return 0;

class Circle(Shape):
    def area(self):
        return 10*10

class Rectangle(Shape):
    def area(self):
        return 10*20;

c = Circle()
print(c.area())

r = Rectangle()
print(r.area())

