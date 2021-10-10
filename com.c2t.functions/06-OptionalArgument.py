#Optional argument must be last argument of the function.
#def getPersonName(fname, mname='', lname):
def getPersonName(fname, lname, mname=''):
    name = fname  + ' ' + mname + ' ' + lname
    return name
    
n = getPersonName('f','l','m')
print(n)

n = getPersonName('f','l')
print(n)