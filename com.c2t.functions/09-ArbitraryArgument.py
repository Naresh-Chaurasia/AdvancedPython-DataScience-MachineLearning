def function1(*arg1):
    print('type(arg1)=',type(arg1))
    print('arg1=',arg1)
    print('len(arg1)=', len(arg1))
    for val in arg1:
        print('val=',val)
    
function1('a','b')