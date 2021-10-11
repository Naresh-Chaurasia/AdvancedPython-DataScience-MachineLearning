def create_adder_function(x):
    def adder(y):
        return x + y
    return adder

outer_fun = create_adder_function(10)
total = outer_fun(20)
print(total)