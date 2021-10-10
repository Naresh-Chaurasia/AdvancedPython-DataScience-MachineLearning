print('before')

try:
    var =  10/0
    print('after division by 0')
except ArithmeticError:
    print('Division by zero is not allowed..')

print('after')
