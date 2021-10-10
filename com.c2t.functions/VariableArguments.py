def variableArguments(*values):
    print('-------------------------')
    print('values=',values)
    print('type(values)=',type(values))

    for val in values:
        print('val=',val)
        print('type(val)=', type(val))



#variableArguments(10)
#variableArguments(10,20)
variableArguments(10,'hello')
'''variableArguments(10,'hello',[10,20,30])
variableArguments()'''