fruits = ['orange', 'apple', 'pear', 'banana']

fruit = input('Please enter the name of fruit you want to search...')

if fruit in fruits:
    print('The ', fruit , ' is present in ', fruits)
else:
    print('The ', fruit, ' is NOT present in ', fruits)