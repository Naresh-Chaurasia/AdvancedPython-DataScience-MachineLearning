def startCoffeeMachine():
    print('warm up water')
    print('warm milk')
    print('grind coffee beans')


def getCoffee():
    print('add water')
    print('add sugar')
    print('add milk')
    return 'coffee'


val = startCoffeeMachine()
print('val=',val)

mug1 = getCoffee()
mug2 = getCoffee()
print('mug1=',mug1)
print('mug2=',mug2)