def decorator_function(func):
    def my_inner_function():
        print('Entering inner function')
        func()
        print('Exiting inner function')
    return my_inner_function

def hello_function():
    print('I am hello function')


hello_function = decorator_function(hello_function)
print(type(hello_function))
#hello_function()