def function2(arg1='this is arg1', arg2='this is arg2'):
    print('arg1=',arg1)
    print('arg2=',arg2)

function2()
function2('one')
function2('one','two')

#SyntaxError: positional argument follows keyword argument
#function2(arg1='one','two')
function2('one',arg2='two')
function2(arg1='one',arg2='two')
