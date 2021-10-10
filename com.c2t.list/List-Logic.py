'''
Accept input from user and store in list
'''

myList = []

while True:
    print('Enter the element to be stored in list...')
    element = input()
    if(element == ''):
        break
    else:
        myList = myList + [element]
        
print('myList=',myList)