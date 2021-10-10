def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
print(type(add_15))
 
#print(add_15(10))