def function2(arg1='this is arg1', arg2='this is arg2'):
    print('arg1=',arg1)
    print('arg2=',arg2)

def function1(arg1, arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    
def functionDictionary(val1, val2=10):
    dict = {'val1':val1,  'val2':val2}
    dict['val3']='html'
    print(dict)
    
#function1(arg1='value1', arg2='value2')
#function1(arg2='value1', arg1='value2')

#function2('a','b')

#functionDictionary('java','selenium')
#functionDictionary('java')

#function2()