def shout(text):
    return text.upper()

def shouted(methodAsArgument):
    print(methodAsArgument('converting to upper case'))


'''
print('-------------------------------') 
print(shout('Hello'))

shoutAgain = shout
print('-------------------------------')
print(shoutAgain('Hello'))
'''

shouted(shout)

