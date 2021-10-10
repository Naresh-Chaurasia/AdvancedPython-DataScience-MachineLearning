try: 
    raise NameError("Hi there")  # Raise Error
except IndexError as e:
    t = type(e)
    print(t)
    print ("An exception::",t)

print('after except...')
