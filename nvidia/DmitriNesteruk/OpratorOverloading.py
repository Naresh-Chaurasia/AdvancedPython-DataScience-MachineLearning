class Square:
    def __init__(self, side):
        self.side = side

    def __add__(s1, s2):
        return s1.side*4 + s2.side*4


s1 = Square(10);
s2 = Square(20);   

print(s1.side)
print(s2.side)

print(s1+s2)