#https://docs.python.org/3/library/functions.html#print

def localGlobal():
    global value
    #del value

    print(value)
   
    
value = 1000

localGlobal()
print(value)