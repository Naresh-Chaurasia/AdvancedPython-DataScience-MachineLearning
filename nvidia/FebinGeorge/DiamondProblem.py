class A:
    pass

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')

class D(B,C):
    pass

d = D()
d.method()